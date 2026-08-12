# Architecture overview generator

Generates the client-facing "Architecture overview" document for both
products from a single source. This answers the request that comes up in
most tenders and security reviews: components, dependencies and
integration points.

## Not part of the published documentation

This lives in `tools/`, outside `docs/`. `mkdocs.yml` leaves `docs_dir` at
its default of `docs/`, `mkdocs-soteria-plus.yml` sets it to
`soteria-plus-docs/`, and the Soteria+ CI job builds that directory by
copying `docs/*` and nothing else. Neither published site can see this
directory. **Do not move it under `docs/`.**

## Run

```bash
python3 tools/architecture/build.py --all
```

Output lands in `tools/architecture/out/`, which is gitignored:

```text
curate-architecture-overview.html    soteria-architecture-overview.html
curate-architecture-overview.pdf     soteria-architecture-overview.pdf
```

Options: `--product curate|soteria` for one product, `--no-pdf` for HTML
only. Giving neither flag is an error rather than a default build.

Python 3.10 or newer, standard library only. No `pip install`, and nothing
is added to `requirements.txt`, which belongs to mkdocs.

Each HTML file is self-contained: the CSS is inlined and the brand logo is
embedded as a data URI, once as the masthead mark and once as the favicon,
so the document survives being emailed around. The twice-embedded logo is
about two thirds of the 137KB Curate page.

### PDF

The PDF step needs headless Chrome and is best-effort. `$CHROME` is tried
first, then the usual system paths, then the puppeteer cache. If no
browser is found, or Chrome will not start, or it fails, or it is still
running after three minutes, the step prints why, the HTML is still
written and the build still succeeds. Point at a specific binary with
`CHROME=/path/to/chrome`.

A current PDF is six pages, of which page 2 is the landscape architecture
diagram. The step reads that page setup back out of the file and prints a
note if it came out any other way, which is what a browser that ignores
the named `@page` rule does. A note and not a failure: the document is
correct, the printing of it is not.

## Files

| File | Holds |
| --- | --- |
| `content.py` | Every fact, table row and block of copy, plus the brand definitions and the diagram's box tree. Knows nothing about rendering. |
| `diagram.py` | SVG primitives, the self-measuring layout engine, and the two diagrams. |
| `build.py` | The page template, the stylesheet, the seven checks, and the PDF step. |

## Editing

| To change | Edit |
| --- | --- |
| A fact, a table row, any prose | `content.py` |
| A component in the diagram | `content.ARCH_TREE`, which reflows on its own |
| A connection in the diagram | the route list in `diagram._arrows` |
| A step in the preservation pipeline diagram | `content.WORKFLOW` |
| Page layout, CSS, print rules | `build.py` |

Groups measure themselves, so adding a card reflows its group and the
canvas with no coordinate edits. Arrows are hand-routed but anchor to the
computed box registry, so their endpoints follow a reflow. A new
*component* is automatic; a new *connection* needs a route added.

A card's own height does not reflow. It is 88, or 142 with chips,
whatever the card holds, so a fourth grey line on a plain card, or a third
chip row, draws past the bottom of the card. Check 8 measures the content
against the box and fails the build rather than letting it ship.

Ids in `ARCH_TREE` are arrow anchors. Renaming one that a route
references stops the build with a `KeyError` naming the old id, so that
mistake is loud rather than silent, but the route still has to be pointed
at the new name by hand. Renaming one *onto an id already in use* was the
quiet case, since the registry is a plain dict and the later box wins;
check 8 walks the tree and fails the build on a repeated id.

The two hardcoded outside lanes, `LANE_L` and `LANE_R`, carry the tightest
clearances in the drawing and nothing checks them, so widening the boxes
they run beside means re-measuring that gap by hand. That is the one place
a change can degrade the diagram without anything complaining.

The diagrams resolve `{product}` only, in group labels, card titles and
the workflow note. A `{vendor}` or `{entity}` placed in diagram content
would not be substituted, and check 1 would fail the build.

## Naming rule

Three placeholder forms plus the literal, and the distinction matters:

| Form | Resolves to | Use for |
| --- | --- | --- |
| `{product}` | Curate / Soteria+ | every product reference |
| `{vendor}` | Penwern / Max Communications | branding surfaces only |
| `{entity}` | Penwern Limited / Max Communications | the footer |
| literal `Penwern` | never substituted | who operates or builds something |

`Penwern A3M`, `Penwern support access`, `Penwern-operated endpoint`,
`Named Penwern engineers over SSH`, the lowercase `named Penwern
engineers` in the security note, and `Penwern operated, outside the
tenant` stay as written in both builds. Nine occurrences across those six
distinct phrases survive into the Soteria+ document, in the tables, the
security note, the facts panel and the diagram. Penwern operates Soteria+
deployments too, and A3M is the name of an upstream fork rather than a
brand.

This is why the tool uses named placeholders rather than the site's global
`sed` rebrand, which cannot express the distinction. See
`penwern/curate-documentation#21`.

The vendor is never written into the page template either. It is read from
the brand, so the masthead, the "Managed by" pill and the footer cannot
carry the wrong company's name.

The masthead treatment is per-brand too, in `Brand.logo_tile`. The Penwern
mark is a pale mint glyph drawn for a dark ground, so it sits directly on
the deep teal bar with no tile. The Max Communications lockup is a dark
navy block that goes murky on that bar, so it gets a sage-to-mint gradient
tile behind it. The two marks have opposite polarity and no single
treatment serves both, which is why this is brand data rather than a rule
in the stylesheet.

## Checks

Seven checks run inside the build, numbered 1 to 8 with 6 retired. Any
failure raises, listing every problem at once, and the build exits
non-zero.

1. No `{product}`, `{vendor}` or `{entity}` survived unresolved.
2. Zero em dashes.
3. No other product's name appears anywhere in the document.
4. Both SVGs are present and parse as XML.
5. The referenced logo file exists.
6. Retired. This was the PDF's page orientation, which the PDF step now
   reports as a note of its own. A build whose HTML is correct must not
   fail over how a browser paginated it. The number is left standing so
   the two either side still mean what they have always meant.
7. No other brand's vendor names any of the three branding surfaces
   (masthead, "Managed by" pill, footer). A surface whose markup cannot be
   found fails too, so renaming a class cannot turn this into a check that
   silently cannot fire.
8. The architecture diagram's own geometry: no card draws past the box
   the layout reserved for it, and no id is used twice. Both are silent
   in the drawing, which is why they are checked. `diagram.py` measures
   them, from the same helpers that place the ink, and `build.py` reports
   them with the rest.

Checks 3 and 7 hold a build against every other brand rather than one
named opposite, so adding a third entry to `PRODUCTS` extends them on its
own.

Check 7 is deliberately narrower than check 3. A vendor name cannot be
banned document-wide the way a product name can, because literal `Penwern`
is correct in both builds wherever it names who built or operates
something. Only the three branding surfaces carry the vendor as branding,
and only there is the other brand's name a leak.

Output is written before the checks run, so a failed build leaves its
rejected files in `out/` for inspection.

Separately from the checks, `diagram.py` raises on a broken invariant in
the box tree: a group holding both cards and children, caption lines with
no label to sit under, a two-way arrow drawn with a one-way pen, a band
too shallow to run a labelled line down, and a chip chain that would break
across a row. These raise rather than assert, because `python3 -O` deletes
assertions and this tool's tests are its own runtime checks.

The checks still cannot catch most visual regressions. A card overrunning
its own box is caught; an arrow that now crosses a card, a label plaque
landing on something it should not, or a route that has stopped reading as
a connection all still need someone to open the output and look.

## Publishing

Manual and deliberate. Copy the four files to Nextcloud at
`Projects/Curate/Documentation/Architecture Diagrams/`. That directory is
a live rclone mount of the company Nextcloud, so confirm before
overwriting: the files already there are the current published version.
