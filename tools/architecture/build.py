#!/usr/bin/env python3
"""Build the client-facing architecture overview for both products.

Run from anywhere:
    python3 tools/architecture/build.py --all
"""

import argparse
import base64
import os
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from html import escape
from pathlib import Path

import content
import diagram
from content import PRODUCTS, Brand

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]              # curate-documentation/
ASSETS = REPO / "docs" / "assets"
OUT = HERE / "out"


class CheckError(Exception):
    """A build-time check failed.

    Output is written before checks run, because the PDF step prints from
    the HTML on disk and check 6 reads the resulting PDF. A failed build
    therefore leaves its rejected output in out/ for inspection, and exits
    non-zero.
    """


def resolve(text: str, brand: Brand) -> str:
    """Resolve {product}, {vendor} and {entity} against a brand.

    Only content strings pass through here. Never CSS: the stylesheet is
    full of literal braces and would raise or be mangled.
    """
    return (
        text.replace("{product}", brand.product)
        .replace("{vendor}", brand.vendor)
        .replace("{entity}", brand.entity)
    )


def _pdf_orientations(pdf: Path) -> list[str]:
    """Read each page's orientation from its /MediaBox.

    Parsed with a regex rather than a PDF library because the tool is
    standard-library only. Chrome writes one /MediaBox per page in a
    predictable form, which is all this needs to handle.
    """
    raw = pdf.read_bytes()
    boxes = re.findall(
        rb"/MediaBox\s*\[\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*\]", raw
    )
    out = []
    for x0, y0, x1, y1 in boxes:
        w = float(x1) - float(x0)
        h = float(y1) - float(y0)
        out.append("landscape" if w > h else "portrait")
    return out


# The three places the document names the vendor. Check 7 reads only
# these, because a literal vendor name is legitimate everywhere else.
_SURFACES = (
    ("masthead", r'<header class="masthead">.*?</header>'),
    ("'Managed by' pill", r"<span class=pill>Managed by[^<]*</span>"),
    ("footer", r"<footer class=doc>.*?</footer>"),
)


def _branding_surfaces(html: str) -> list[tuple[str, str]]:
    """The markup of each branding surface, paired with its name.

    A surface that matches nothing is returned with an empty string
    rather than dropped, so check 7 can fail on it: a renamed class would
    otherwise turn the check into one that silently cannot fire.

    Base64 payloads are stripped first. They are image bytes, not copy,
    and a chance run of letters inside one would be a false failure.
    """
    text = re.sub(r"data:image/png;base64,[A-Za-z0-9+/=]+", "", html)
    return [
        (name, "".join(re.findall(pat, text, flags=re.S)))
        for name, pat in _SURFACES
    ]


def check_output(html: str, brand: Brand, pdf: Path | None) -> None:
    """Run every check and raise CheckError once, listing every failure.

    Checks 2 and 3 guard failures that are silent and would reach a client.
    """
    problems = []

    # 1. No unresolved placeholder survived into the output.
    stray = sorted(set(re.findall(r"\{(product|vendor|entity)\}", html)))
    if stray:
        problems.append(f"unresolved placeholders: {stray}")

    # 2. Zero em dashes.
    if "\u2014" in html:
        n = html.count("\u2014")
        problems.append(f"{n} em dash(es) in output; use commas or colons")

    # 3. The other product's name appears nowhere.
    other = "Soteria+" if brand.key == "curate" else "Curate"
    if other in html:
        problems.append(f"{brand.key} build leaks the name {other!r}")

    # 4. Both SVGs parse as XML.
    #    stdlib ElementTree is used deliberately. The usual XXE and
    #    billion-laughs concerns need untrusted input; this parses SVG the
    #    build just generated from local source, purely to catch a
    #    malformed tag. defusedxml would be the right answer for anything
    #    externally supplied, but it is third-party and this tool is
    #    standard-library only.
    svgs = re.findall(r"<svg.*?</svg>", html, flags=re.S)
    if len(svgs) != 2:
        problems.append(f"expected 2 SVGs, found {len(svgs)}")
    for i, svg in enumerate(svgs):
        try:
            ET.fromstring(svg)
        except ET.ParseError as exc:
            problems.append(f"SVG {i} is not well-formed XML: {exc}")

    # 5. The referenced logo exists.
    if not (ASSETS / brand.logo).is_file():
        problems.append(f"missing logo asset: {ASSETS / brand.logo}")

    # 6. Exactly one landscape page, every other page portrait.
    #    Skipped when the PDF was not produced; the PDF is best-effort.
    if pdf is not None and pdf.is_file():
        orient = _pdf_orientations(pdf)
        landscape = orient.count("landscape")
        if not orient:
            problems.append("no /MediaBox found in the PDF")
        elif landscape != 1:
            problems.append(
                f"expected exactly 1 landscape page, got {landscape} "
                f"of {len(orient)}: {orient}"
            )

    # 7. The other brand's vendor names no branding surface.
    #    Deliberately not a whole-document check. Check 3 catches the
    #    other product's name anywhere, but a vendor cannot be treated
    #    the same way: literal "Penwern" is correct and required in both
    #    builds wherever it names who built or operates something
    #    ("Penwern A3M", "Penwern support access", "Named Penwern
    #    engineers"). Only the masthead, the "Managed by" pill and the
    #    footer carry the vendor as branding, and only there is the
    #    other brand's name a leak.
    other_key = "soteria" if brand.key == "curate" else "curate"
    other_vendor = PRODUCTS[other_key].vendor
    for name, surface in _branding_surfaces(html):
        if not surface:
            problems.append(f"branding surface not found in the page: {name}")
        elif other_vendor in surface:
            problems.append(
                f"{brand.key} build names the vendor {other_vendor!r} "
                f"in the {name}"
            )

    if problems:
        raise CheckError(
            f"{brand.product} build failed {len(problems)} check(s):\n  - "
            + "\n  - ".join(problems)
        )


def logo_data_uri(brand: Brand) -> str:
    """The brand logo, inlined so the document is a single portable file.

    The same image is the favicon and the masthead mark. A data URI cannot
    be shared between two elements, so the bytes appear twice: with the
    34KB Penwern logo that is roughly 90KB of the HTML, which is accepted
    for a document that has to survive being emailed around.
    """
    raw = (ASSETS / brand.logo).read_bytes()
    return "data:image/png;base64," + base64.b64encode(raw).decode("ascii")


# The stylesheet, kept as one concatenated string. It is never passed
# through .format() or resolve(): every CSS rule is a pair of literal
# braces, which .format() reads as replacement fields and raises on.
CSS = """
:root{
  --ink:#0a0f1a; --muted:#6b7280; --teal:#1a3d36; --sage:#83aba3;
  --aqua:#9fd0c7; --mint:#a6e8ce; --wash:#f6faf9; --rule:#e5e7eb;
}
*{box-sizing:border-box}
body{
  margin:0; padding:40px 24px; color:var(--ink); background:#fff;
  font-family:'Geist','Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  font-size:14.5px; line-height:1.6;
}
.wrap{max-width:1180px; margin:0 auto}

header.masthead{
  display:flex; align-items:center; gap:20px;
  background:var(--teal); border-radius:14px; padding:18px 26px;
  margin-bottom:34px; box-shadow:0 8px 24px rgba(10,15,26,.12);
}
header.masthead img{
  height:52px; width:auto; display:block;
}
header.masthead .logotile{
  border-radius:10px; padding:8px 12px; display:flex; align-items:center;
}
header.masthead .titles{display:flex; flex-direction:column}
header.masthead .eyebrow{
  font-size:.72rem; letter-spacing:.18em; text-transform:uppercase;
  color:var(--aqua); font-weight:600;
}
header.masthead .title{font-weight:700; font-size:1.15rem; color:#e8efed}

header.doc h1{font-size:1.6rem; margin:0 0 10px}
p{max-width:76ch}
p.lede{font-size:1.05rem; color:#374151; max-width:62ch}
.meta{display:flex; flex-wrap:wrap; gap:8px; margin:16px 0 4px}
.pill{
  background:var(--wash); border:1px solid var(--sage); border-radius:999px;
  padding:4px 12px; font-size:.8rem; color:var(--teal); font-weight:500;
}

h2{font-size:1.2rem; margin:38px 0 10px; padding-bottom:6px;
   border-bottom:2px solid var(--mint)}
h3{font-size:1rem; margin:26px 0 8px}

.tw{overflow-x:auto; margin:14px 0}
table{border-collapse:collapse; width:100%; min-width:720px; font-size:13px}
th,td{text-align:left; padding:9px 12px; border-bottom:1px solid var(--rule);
      vertical-align:top}
th{background:var(--wash); font-weight:600; color:var(--teal);
   border-bottom:2px solid var(--sage)}

figure{margin:18px 0}
.frame{border:1px solid var(--rule); border-radius:12px; padding:10px;
       overflow-x:auto; background:#fff}
.frame svg{display:block; width:100%; height:auto; min-width:900px}
figcaption{font-size:12.5px; color:var(--muted); margin-top:8px}

.note{background:var(--wash); border-left:4px solid var(--sage);
      border-radius:0 8px 8px 0; padding:14px 18px; margin:18px 0;
      font-size:13.5px}

.grid{display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
      gap:14px; margin:16px 0}
.fact{border:1px solid var(--rule); border-radius:10px; padding:14px 16px}
.fact .k{font-size:.72rem; letter-spacing:.12em; text-transform:uppercase;
         color:var(--sage); font-weight:600; margin-bottom:4px}
.fact .v{font-size:13.5px}

footer.doc{margin-top:44px; padding-top:16px; border-top:1px solid var(--rule);
           font-size:12.5px; color:var(--muted)}

@media print{
  @page{size:A4 portrait; margin:14mm}
  @page wide{size:A4 landscape; margin:10mm}
  html,body{-webkit-print-color-adjust:exact; print-color-adjust:exact}
  body{padding:0; font-size:12.5px}
  .wrap{max-width:none}
  header.masthead{box-shadow:none; break-inside:avoid}
  h2{break-after:avoid; page-break-after:avoid; margin-top:30px}
  h3{break-after:avoid; page-break-after:avoid}
  p,figcaption{orphans:3; widows:3}
  figure{break-inside:avoid; page-break-inside:avoid}
  .frame{break-inside:avoid; box-shadow:none; overflow:visible; padding:0;
         border:none}
  .frame svg{min-width:0; width:auto; max-width:100%; margin:0 auto}
  figure.arch{page:wide; break-before:page; break-after:page}
  figure.arch .frame svg{max-height:176mm}
  figure.flow .frame svg{max-height:60mm}
  .tw{break-inside:auto; overflow:visible}
  table{min-width:0; font-size:11.5px}
  thead{display:table-header-group}
  tr{break-inside:avoid; page-break-inside:avoid}
  .note,.fact{break-inside:avoid}
  .grid{grid-template-columns:repeat(2,1fr)}
  footer.doc{break-inside:avoid}
}
"""


def _table(headers, widths, rows, brand: Brand) -> str:
    """One table, with its column widths carried in a colgroup.

    The widths are percentages set per table rather than left to the
    browser, because auto layout gives a wide prose column to whichever
    cell happens to be longest.
    """
    cols = "".join(f'<col style="width:{w}%"/>' for w in widths)
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{resolve(c, brand)}</td>" for c in r) + "</tr>"
        for r in rows
    )
    return (
        f'<div class=tw><table><colgroup>{cols}</colgroup>'
        f"<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>"
    )


def render_page(brand: Brand) -> str:
    """The whole document, as one self-contained HTML file.

    The masthead is the only place the vendor is named, and it is taken
    from the brand rather than written down: a literal lockup here would
    ship the wrong company's name in the other product's build, and check
    3 only catches the other product's name, not the other vendor's.
    """
    p = {k: resolve(v, brand) for k, v in content.PROSE.items()}
    logo = logo_data_uri(brand)
    # The tile is wrapped around the mark only for a brand that asks for
    # one, so a brand with no tile gets no empty element either. The
    # renderer never asks which product it is drawing.
    # Brand data goes into attributes escaped. No current value contains
    # a quote, so this changes nothing today; it means a value that one
    # day does cannot break out of the attribute and mangle the markup
    # silently.
    mark = f'<img src="{logo}" alt="{escape(brand.vendor)}">'
    if brand.logo_tile:
        mark = (
            f'<div class="logotile" style="background:{escape(brand.logo_tile)}">'
            f"{mark}</div>"
        )
    pills = "".join(
        f"<span class=pill>{resolve(x, brand)}</span>" for x in content.PILLS
    )
    facts = "".join(
        f"<div class=fact><div class=k>{resolve(k, brand)}</div>"
        f"<div class=v>{resolve(v, brand)}</div></div>"
        for k, v in content.FACTS
    )

    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{brand.product} architecture overview</title>
<link rel="icon" type="image/png" href="{logo}">
<style>{CSS}</style>

<div class=wrap>

<header class="masthead">
  {mark}
  <div class="titles">
    <span class="eyebrow">{brand.vendor} &middot; {brand.product}</span>
    <span class="title">Architecture overview</span>
  </div>
</header>

<header class=doc>
  <h1>Components, dependencies and integration points</h1>
  <p class=lede>{p["lede"]}</p>
  <div class=meta>{pills}</div>
</header>

<h2>System architecture</h2>
<p>{p["arch_intro"]}</p>
<figure class=arch>
  <div class=frame>{diagram.architecture_svg(brand.product)}</div>
  <figcaption>{p["arch_caption"]}</figcaption>
</figure>

<h2>Components</h2>
<p>{p["components_intro"]}</p>
{_table(("Component", "Role", "Technology", "Data held"),
        (17, 34, 16, 33), content.COMPONENTS, brand)}

<h3>Optional connectors</h3>
<p>{p["connectors_intro"]}</p>
{_table(("Connector", "What it does", "Technology", "Notes"),
        (19, 38, 14, 29), content.CONNECTORS, brand)}

<h2>Integration points</h2>
<p>{p["integrations_intro"]}</p>
{_table(("Interface", "Direction", "Protocol", "Authentication", "Data crossing"),
        (14, 11, 16, 31, 28), content.INTEGRATIONS, brand)}

<div class=note>{p["security_note"]}</div>

<h2>Preservation workflow</h2>
<p>{p["workflow_intro"]}</p>
<figure class=flow>
  <div class=frame>{diagram.workflow_svg(brand.product)}</div>
  <figcaption>{p["workflow_caption"]}</figcaption>
</figure>

<h2>Hosting and data</h2>
<div class=grid>{facts}</div>

<footer class=doc>{p["footer"]}</footer>

</div>
"""


# Seconds to wait for Chrome. Named rather than inline so the timeout and
# the note that reports it cannot drift apart.
PDF_TIMEOUT = 180

CHROME_CANDIDATES = (
    "/usr/bin/google-chrome",
    "/usr/bin/google-chrome-stable",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
    "/snap/bin/chromium",
)


def _runnable(p: Path) -> bool:
    """A file we could actually execute.

    Existence is not enough. `$CHROME` pointing at a downloaded archive
    or a text file is the likeliest way anyone meets this code, since
    setting it is the remedy the tool itself prints when it finds no
    browser, and executing a non-executable file raises rather than
    returning a non-zero exit.
    """
    return p.is_file() and os.access(p, os.X_OK)


def find_chrome() -> Path | None:
    """$CHROME, then the usual paths, then the puppeteer cache."""
    env = os.environ.get("CHROME")
    if env and _runnable(Path(env)):
        return Path(env)
    for c in CHROME_CANDIDATES:
        if _runnable(Path(c)):
            return Path(c)
    cache = Path.home() / ".cache" / "puppeteer" / "chrome"
    if cache.is_dir():
        found = sorted(
            p for p in cache.glob("*/chrome-linux64/chrome") if _runnable(p)
        )
        if found:
            # Last by plain name sort, which is not a version sort:
            # linux-99 would beat linux-121. Good enough to pick one
            # installed browser, not a version-selection policy.
            return found[-1]
    return None


def to_pdf(html_path: Path, pdf_path: Path) -> Path | None:
    """Print the page to PDF. Returns None when no PDF could be made.

    Every way this can go wrong returns None rather than raising: no
    Chrome, a Chrome that will not start, a Chrome that fails, and a
    Chrome that hangs. The PDF is best-effort, so none of them may take
    the build down with them. Each prints a different note, because
    "not installed", "not a browser", "crashed" and "still running after
    three minutes" need different responses.
    """
    chrome = find_chrome()
    if chrome is None:
        print(
            "  no Chrome found, so no PDF. Set CHROME=/path/to/chrome, "
            "or print the HTML from a browser."
        )
        return None

    with tempfile.TemporaryDirectory() as tmp:
        cmd = [
            str(chrome),
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            f"--user-data-dir={tmp}",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            html_path.as_uri(),
        ]
        try:
            # Remove any previous PDF first. Chrome exiting 0 without
            # writing would otherwise leave the last run's file in place,
            # and it would be reported as this run's output and checked as
            # if it were. Inside the try because unlink raises too: a
            # directory at the path, or an unwritable out/.
            pdf_path.unlink(missing_ok=True)
            r = subprocess.run(
                cmd, capture_output=True, text=True, timeout=PDF_TIMEOUT
            )
        except subprocess.TimeoutExpired:
            # run() kills the child before re-raising, so nothing is left
            # behind. A hang is a failed PDF, never a failed build.
            print(
                f"  Chrome timed out after {PDF_TIMEOUT}s, so no PDF. The "
                "HTML is written; print it from a browser."
            )
            return None
        except OSError as exc:
            # Either the old PDF could not be cleared, or the process
            # could not be started at all: not executable, not a binary,
            # gone between the check and the call. PermissionError is an
            # OSError, so one clause covers all of them. The message
            # names no path of its own because every one of these
            # exceptions carries the offending filename already.
            print(f"  PDF step could not run, so no PDF: {exc}")
            return None

    if r.returncode != 0 or not pdf_path.is_file():
        print(f"  PDF step failed (exit {r.returncode}): {r.stderr.strip()[:300]}")
        return None
    return pdf_path


def build(brand: Brand, want_pdf: bool = True) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    html = render_page(brand)
    html_path = OUT / f"{brand.out}.html"
    html_path.write_text(html, encoding="utf-8")

    pdf_path = None
    if want_pdf:
        pdf_path = to_pdf(html_path, OUT / f"{brand.out}.pdf")

    check_output(html, brand, pdf_path)

    print(f"  {html_path.relative_to(REPO)}")
    if pdf_path:
        pages = len(_pdf_orientations(pdf_path))
        print(f"  {pdf_path.relative_to(REPO)} ({pages} pages)")
    return html_path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--product", choices=sorted(PRODUCTS), help="build one product"
    )
    ap.add_argument("--all", action="store_true", help="build both products")
    ap.add_argument(
        "--no-pdf", action="store_true", help="emit HTML only, skip the PDF"
    )
    args = ap.parse_args()

    if args.all:
        keys = sorted(PRODUCTS)
    elif args.product:
        keys = [args.product]
    else:
        ap.error("give --product or --all")

    try:
        for key in keys:
            build(PRODUCTS[key], want_pdf=not args.no_pdf)
    except CheckError as exc:
        print(f"\nFAILED: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
