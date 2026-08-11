#!/usr/bin/env python3
"""Build the client-facing architecture overview for both products.

Run from anywhere:
    python3 tools/architecture/build.py --all
"""

import argparse
import base64
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

import content
from content import PRODUCTS, Brand

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]              # curate-documentation/
ASSETS = REPO / "docs" / "assets"
OUT = HERE / "out"


class CheckError(Exception):
    """A build-time check failed. The build must not produce output."""


def resolve(text: str, brand: Brand) -> str:
    """Resolve {product} and {vendor} against a brand.

    Only content strings pass through here. Never CSS: the stylesheet is
    full of literal braces and would raise or be mangled.
    """
    return text.replace("{product}", brand.product).replace(
        "{vendor}", brand.vendor
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


def check_output(html: str, brand: Brand, pdf: Path | None) -> None:
    """Run every build-time check. Raise CheckError on the first failure.

    Checks 2 and 3 guard failures that are silent and would reach a client.
    """
    problems = []

    # 1. No unresolved placeholder survived into the output.
    stray = sorted(set(re.findall(r"\{(product|vendor)\}", html)))
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

    if problems:
        raise CheckError(
            f"{brand.product} build failed {len(problems)} check(s):\n  - "
            + "\n  - ".join(problems)
        )


def render_page(brand: Brand) -> str:
    """Stub replaced in Task 5. Exists so the checks can run from Task 1."""
    return (
        '<meta charset="utf-8">\n'
        f"<title>{brand.product} architecture overview</title>\n"
        f"<h1>{resolve('{product}', brand)}</h1>\n"
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1 1'></svg>\n"
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1 1'></svg>\n"
    )


def build(brand: Brand, want_pdf: bool = True) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    html = render_page(brand)
    html_path = OUT / f"{brand.out}.html"
    html_path.write_text(html, encoding="utf-8")

    pdf_path = None  # Task 6 fills this in.

    check_output(html, brand, pdf_path)
    print(f"  {html_path.relative_to(REPO)}")
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
