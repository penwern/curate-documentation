"""SVG generation for the architecture overview diagrams.

Imports content, knows nothing about HTML. Groups measure themselves so
the canvas height is computed, never hardcoded.

Nothing here inherits paint. A card or group either states its own fill
and stroke in content.py, or it takes the single renderer default below.
A card sitting inside a teal group does not pick up teal.
"""

import dataclasses
from dataclasses import dataclass

from content import (
    ARCH_TREE,
    FONT_STACK,
    MONO_STACK,
    PALETTE,
    WORKFLOW,
    WORKFLOW_NOTE,
    Card,
    Group,
)

CARD_H = 88
CARD_H_CHIPS = 142
CARD_GAP = 20
CHIP_H = 26
CHIP_GAP = 10
PAD = 24
LABEL_H = 42
GROUP_LINE_H = 15
GROUP_GAP = 22
CANVAS_W = 1400


def esc(s: str) -> str:
    """Escape text for an SVG text node."""
    return (
        s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    )


def _n(v):
    """Round a coordinate for the markup. Full float precision is valid
    SVG but makes the output noisy to read and to diff."""
    return round(v, 2)


def text(x, y, s, size=13, weight=None, anchor=None, fill=None, spacing=None,
         mono=False):
    a = [f'x="{_n(x)}"', f'y="{_n(y)}"']
    if anchor:
        a.append(f'text-anchor="{anchor}"')
    a.append(f'font-family="{MONO_STACK if mono else FONT_STACK}"')
    a.append(f'font-size="{size}"')
    if weight:
        a.append(f'font-weight="{weight}"')
    if spacing:
        a.append(f'letter-spacing="{spacing}"')
    a.append(f'fill="{fill or PALETTE["ink"]}"')
    return f"<text {' '.join(a)}>{esc(s)}</text>"


def rect(x, y, w, h, fill=None, stroke=None, dashed=False, rx=7, sw=1.5,
         dash="6 5"):
    """A rounded rectangle.

    `dash` is the pattern used when `dashed` is set. It is a parameter
    because the source dashes a group box more coarsely than a card, and
    the caller is the only thing that knows which it is drawing.
    """
    a = [f'x="{_n(x)}"', f'y="{_n(y)}"', f'width="{_n(w)}"',
         f'height="{_n(h)}"', f'rx="{rx}"']
    a.append(f'fill="{fill or PALETTE["white"]}"')
    if stroke:
        a.append(f'stroke="{stroke}"')
        a.append(f'stroke-width="{sw}"')
        if dashed:
            a.append(f'stroke-dasharray="{dash}"')
    return f"<rect {' '.join(a)}/>"


def chip(x, y, w, label, fill=None):
    """A pill holding one S3 bucket name inside a storage card.

    A full-height corner radius makes it a pill rather than a rounded
    rectangle. The label is monospaced because it is a literal bucket name.
    """
    return rect(x, y, w, CHIP_H, fill=fill, stroke=PALETTE["mint"],
                rx=CHIP_H / 2, sw=1.2) + text(
        x + w / 2, y + 16.5, label, size=10, anchor="middle",
        fill=PALETTE["ink"], mono=True
    )


@dataclass(frozen=True)
class Box:
    """Where something ended up. Arrows anchor to these."""

    x: float
    y: float
    w: float
    h: float

    @property
    def cx(self) -> float:
        return self.x + self.w / 2

    @property
    def cy(self) -> float:
        return self.y + self.h / 2

    @property
    def right(self) -> float:
        return self.x + self.w

    @property
    def bottom(self) -> float:
        return self.y + self.h


@dataclass
class Layout:
    """A finished diagram: its markup, its height, and where things landed."""

    svg: str
    height: float
    boxes: dict[str, Box]


def _card_height(c: Card) -> float:
    return CARD_H_CHIPS if c.chips else CARD_H


def _row_heights(cards, cols: int) -> list[float]:
    """Height of each grid row: the tallest card in it.

    Cards are not all one height, because a card carrying a chip grid is
    taller. Both measure() and render() derive row geometry from this, so
    they cannot drift apart.
    """
    rows = []
    for i in range(0, len(cards), cols):
        rows.append(max(_card_height(c) for c in cards[i:i + cols]))
    return rows


def _row_widths(children, avail: float) -> list[float]:
    """Width of each child in a row layout: its share of avail by weight.

    Both passes read row widths from here. Computed separately they could
    drift, and then measure() would size a child at one width while
    render() drew it at another, overflowing the child in silence.
    """
    total = sum(c.weight for c in children)
    gaps = GROUP_GAP * (len(children) - 1)
    return [(avail - gaps) * c.weight / total for c in children]


def _insets(group: Group) -> tuple[float, float]:
    """(head, pad) for a group.

    An unlabelled group is a pure wrapper used to stack siblings, so it
    draws no box and takes no padding. Padding it would inset its children
    twice and pull them away from the geometry the source has.

    A group's caption lines sit under its label and above its contents, so
    each one lengthens the head. Both passes read the head from here, so
    the space measure() reserves is the space render() draws into.
    """
    if not group.label:
        return 0.0, 0.0
    return LABEL_H + GROUP_LINE_H * len(group.lines), PAD


def measure(group: Group, w: float) -> float:
    """Height this group needs at the given width. Recurses into children.

    The two assertions guard content loss that no geometry check can see.
    Both passes would still agree and nothing would overlap; the content
    would simply not be drawn. render() calls measure() first, so these
    cover it too.
    """
    who = group.id or group.label or "an unidentified group"
    assert not (group.cards and group.children), (
        f"{who} carries both cards and children; the cards branch would "
        "draw the cards and silently drop the children"
    )
    assert group.label or not group.lines, (
        f"{who} is unlabelled but carries lines; lines render under a "
        "label, so they would be silently dropped"
    )

    head, pad = _insets(group)
    if group.cards:
        hs = _row_heights(group.cards, group.cols)
        return head + sum(hs) + CARD_GAP * (len(hs) - 1) + pad
    if not group.children:
        return head + pad

    avail = w - 2 * pad
    if group.layout == "row":
        tallest = max(
            measure(c, cw)
            for c, cw in zip(group.children,
                             _row_widths(group.children, avail))
        )
        return head + tallest + pad

    stacked = sum(measure(c, avail) for c in group.children)
    return head + stacked + GROUP_GAP * (len(group.children) - 1) + pad


def _card(c: Card, box: Box) -> str:
    """A card: rounded rect, bold title, then chips and/or grey lines."""
    # A dashed card is dashed more finely than a dashed group box.
    out = [rect(box.x, box.y, box.w, box.h,
                fill=c.fill or PALETTE["white"],
                stroke=c.stroke or PALETTE["sage"], dashed=c.dashed,
                dash="5 4")]

    if c.chips:
        # Title sits near the top; the chip grid fills the body below it.
        out.append(text(box.cx, box.y + 30, c.title, size=13, weight="600",
                        anchor="middle"))
        cols = c.chip_cols
        cw = (box.w - 2 * 16 - CHIP_GAP * (cols - 1)) / cols
        for i, name in enumerate(c.chips):
            col, row = i % cols, i // cols
            out.append(chip(box.x + 16 + col * (cw + CHIP_GAP),
                            box.y + 48 + row * (CHIP_H + CHIP_GAP),
                            cw, name,
                            fill=c.chip_fill or PALETTE["white"]))
        rows = (len(c.chips) + cols - 1) // cols
        ly = box.y + 48 + rows * (CHIP_H + CHIP_GAP) + 10
        for i, line in enumerate(c.lines):
            out.append(text(box.cx, ly + i * 16, line, size=10,
                            anchor="middle", fill=PALETTE["muted"]))
        return "".join(out)

    # Title sits above centre when there are lines, centred when there are none.
    ty = box.cy + (-4 if c.lines else 5)
    out.append(text(box.cx, ty, c.title, size=13, weight="600", anchor="middle"))
    for i, line in enumerate(c.lines):
        out.append(text(box.cx, ty + 18 + i * 13, line, size=10.5,
                        anchor="middle", fill=PALETTE["muted"]))
    return "".join(out)


def render(group: Group, x: float, y: float, w: float,
           boxes: dict[str, Box]) -> tuple[str, float]:
    """Draw a group at (x, y) with width w. Returns (svg, height used).

    Every element carrying an id is recorded in `boxes` so arrows can
    anchor to computed geometry instead of hardcoded coordinates.
    """
    h = measure(group, w)
    head, pad = _insets(group)
    out = []

    if group.label:
        out.append(rect(x, y, w, h, fill=group.fill or PALETTE["wash"],
                        stroke=group.stroke or PALETTE["sage"],
                        dashed=group.dashed, rx=10, sw=2, dash="6 5"))
        out.append(text(x + 16, y + 24, group.label, size=10.5, weight="600",
                        spacing="1.1", fill=PALETTE["muted"]))
        # Caption lines under the label. The tuple is flat, so the source's
        # emphasis on its closing claim is applied by position.
        for i, line in enumerate(group.lines):
            last = i == len(group.lines) - 1
            out.append(text(
                x + 16, y + 42 + i * GROUP_LINE_H, line, size=10.5,
                weight="600" if last else None,
                fill=PALETTE["teal_deep"] if last else PALETTE["muted"],
            ))

    if group.id:
        boxes[group.id] = Box(x, y, w, h)

    top = y + head
    inner_x = x + pad
    avail = w - 2 * pad

    if group.cards:
        cols = group.cols
        cw = (avail - CARD_GAP * (cols - 1)) / cols
        hs = _row_heights(group.cards, cols)
        # Row tops, accumulated from the row heights measure() used.
        tops, acc = [], top
        for rh in hs:
            tops.append(acc)
            acc += rh + CARD_GAP
        for i, c in enumerate(group.cards):
            col, row = i % cols, i // cols
            box = Box(inner_x + col * (cw + CARD_GAP), tops[row],
                      cw, _card_height(c))
            if c.id:
                boxes[c.id] = box
            out.append(_card(c, box))

    elif group.children and group.layout == "row":
        cx = inner_x
        for child, cw in zip(group.children,
                             _row_widths(group.children, avail)):
            svg, _ = render(child, cx, top, cw, boxes)
            out.append(svg)
            cx += cw + GROUP_GAP

    else:
        cy = top
        for child in group.children:
            svg, ch = render(child, inner_x, cy, avail, boxes)
            out.append(svg)
            cy += ch + GROUP_GAP

    return "".join(out), h


MARKERS = (
    '<defs>'
    '<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" '
    'markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">'
    f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{PALETTE["muted"]}"/></marker>'
    '<marker id="arrowrev" viewBox="0 0 10 10" refX="1" refY="5" '
    'markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">'
    f'<path d="M 10 0 L 0 5 L 10 10 z" fill="{PALETTE["muted"]}"/></marker>'
    '</defs>'
)


def connector(pts, dashed=False, both=False, label=None):
    """An orthogonal arrow through hand-chosen waypoints.

    `pts` is a list of (x, y). Endpoints come from the box registry; the
    intermediate points are the hand routing.
    """
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    a = [f'd="{d}"', 'fill="none"', f'stroke="{PALETTE["muted"]}"',
         'stroke-width="1.5"', 'marker-end="url(#arrow)"']
    if both:
        a.append('marker-start="url(#arrowrev)"')
    if dashed:
        a.append('stroke-dasharray="5 4"')
    out = f"<path {' '.join(a)}/>"
    if label:
        # The label sits on the middle of the route's first turn, which is
        # the segment after the short stub leaving the box. A centroid of
        # all the waypoints is not on the line at all once a route is
        # L-shaped, and on this tree it lands three labels on top of cards
        # the route never touches.
        i = 1 if len(pts) > 2 else 0
        (ax, ay), (bx, by) = pts[i], pts[i + 1]
        mx, my = (ax + bx) / 2, (ay + by) / 2
        # A plaque behind the label. Every label is centred on its own
        # route, so without one the arrow strikes through the text. The
        # width is measured from the glyphs, since there is no text
        # metric available: 0.535em per character at this size, plus 6
        # either side.
        lw = 5.35 * len(label) + 12
        out += rect(mx - lw / 2, my - 17.5, lw, 16, rx=3)
        out += text(mx, my - 6, label, size=10, anchor="middle",
                    fill=PALETTE["muted"])
    return out


# The two outside lanes. LANE_L runs in the corridor between the AWS box
# and the EC2 box; LANE_R runs outside the AWS box entirely, which is what
# keeps the support SSH path visibly separate from everything inside it.
LANE_L = 36
LANE_R = CANVAS_W - 14


def _arrows(b: dict[str, Box]) -> list[str]:
    """The twelve routes. Endpoints come from the registry, waypoints are
    hand-chosen: the left and right lanes keep long routes outside the
    boxes, and the S3 corridor is left clear."""
    # The band between the AWS box and the catalogues box below it. The
    # support route crosses the full width of the diagram, so it needs a
    # clear horizontal lane; this is the only one there is.
    below_aws = (b["aws"].bottom + b["catalogues"].y) / 2
    return [
        # 1. Users in through the reverse proxy.
        connector([(b["users"].cx, b["users"].bottom),
                   (b["users"].cx, b["nginx"].y)], label="HTTPS  ·  TLS"),
        # 2. Optional single sign-on, down the left lane into the platform.
        connector([(b["idp"].cx, b["idp"].bottom),
                   (b["idp"].cx, b["idp"].bottom + 36),
                   (LANE_L, b["idp"].bottom + 36),
                   (LANE_L, b["platform"].cy),
                   (b["platform"].x, b["platform"].cy)],
                  dashed=True, label="OIDC single sign-on"),
        # 3. Source systems, down the right lane into the connectors band.
        #    LANE_R - 22 is the corridor between the S3 column and the AWS
        #    boundary, so this stays inside AWS while the SSH route does not.
        connector([(b["sources"].cx, b["sources"].bottom),
                   (b["sources"].cx, b["sources"].bottom + 36),
                   (LANE_R - 22, b["sources"].bottom + 36),
                   (LANE_R - 22, b["connectors"].cy),
                   (b["connectors"].right, b["connectors"].cy)],
                  dashed=True, label="HTTPS  ·  per-system credentials"),
        # 4. Support SSH, its own lane outside the AWS boundary, then in
        #    under the AWS box and up into the instance from below. It
        #    cannot turn in along the right of the EC2 box: every height
        #    there is either the S3 column, AWS Backup or Monitoring.
        connector([(b["support"].cx, b["support"].bottom),
                   (b["support"].cx, b["support"].bottom + 42),
                   (LANE_R, b["support"].bottom + 42),
                   (LANE_R, below_aws),
                   (b["ec2"].cx, below_aws),
                   (b["ec2"].cx, b["ec2"].bottom)],
                  dashed=True, label="SSH  ·  key based"),
        # 5. Platform to object storage. The corridor between them is kept clear.
        connector([(b["platform"].right, b["platform"].cy),
                   (b["s3"].x, b["platform"].cy)],
                  both=True, label="S3 API  ·  IAM role"),
        # 6. Platform triggers the preservation pipeline.
        connector([(b["platform"].cx, b["platform"].bottom),
                   (b["pipeline"].cx, b["pipeline"].y)],
                  both=True, label="trigger and configure"),
        # 7. Access copies out to AtoM, down the left lane.
        connector([(b["pipeline"].x + 232, b["pipeline"].bottom),
                   (b["pipeline"].x + 232, b["pipeline"].bottom + 8),
                   (LANE_L, b["pipeline"].bottom + 8),
                   (LANE_L, b["atom"].cy),
                   (b["atom"].x, b["atom"].cy)],
                  dashed=True, label="DIP deposit  ·  SWORD 2.0"),
        # 8. Connectors publish catalogue records to ArchivesSpace. It
        #    leaves right of centre, as the source does: left of centre
        #    puts its label on top of the support route coming up into
        #    the instance.
        connector([(b["connectors"].cx + 124, b["connectors"].bottom),
                   (b["connectors"].cx + 124, b["aspace"].y - 76),
                   (b["aspace"].cx, b["aspace"].y - 76),
                   (b["aspace"].cx, b["aspace"].y)],
                  dashed=True, label="catalogue records"),
        # 9, 10. Backup and monitoring both point at the instance: they
        #        act on it rather than the other way round. They start on
        #        the left edge of their own card, which is the left edge
        #        of the S3 column, and cross the corridor.
        connector([(b["s3"].x, b["backup"].cy),
                   (b["ec2"].right, b["backup"].cy)]),
        connector([(b["s3"].x, b["monitor"].cy),
                   (b["ec2"].right, b["monitor"].cy)]),
        # 11, 12. The quarantine to appraisal to archive promotion chain,
        #         drawn between the chips of the lifecycle card.
        *_chip_chain(b["lifecycle"], 3),
    ]


def _chip_chain(card: Box, n: int) -> list[str]:
    """Short arrows between consecutive chips in a card's single chip row."""
    inset, gap = 16, CHIP_GAP
    cw = (card.w - 2 * inset - gap * (n - 1)) / n
    y = card.y + 48 + CHIP_H / 2
    out = []
    for i in range(n - 1):
        x = card.x + inset + (i + 1) * cw + i * gap
        out.append(connector([(x, y), (x + gap, y)]))
    return out


def _resolved_tree(product: str) -> Group:
    """A copy of the tree with {product} resolved and group labels upper-cased.

    Built with dataclasses.replace so the module-level ARCH_TREE is never
    mutated: two builds run in one process and the second must not see the
    first product's name.
    """
    def fix(g: Group) -> Group:
        return dataclasses.replace(
            g,
            label=g.label.replace("{product}", product).upper() if g.label else "",
            cards=tuple(
                dataclasses.replace(c, title=c.title.replace("{product}", product))
                for c in g.cards
            ),
            children=tuple(fix(k) for k in g.children),
        )
    return fix(ARCH_TREE)


def architecture_svg(product: str) -> str:
    """The deployment architecture. Canvas height is computed, not fixed."""
    inner_w = CANVAS_W - 48
    boxes: dict[str, Box] = {}
    body, h = render(_resolved_tree(product), 24, 24, inner_w, boxes)
    height = h + 48

    arrows = _arrows(boxes)

    return (
        f'<svg viewBox="0 0 {CANVAS_W} {height:.0f}" '
        'xmlns="http://www.w3.org/2000/svg" role="img" '
        f'aria-label="{esc(product)} architecture: components, dependencies '
        'and integration points">'
        f'{MARKERS}'
        f'{rect(0, 0, CANVAS_W, height, rx=0)}'
        f'{body}{"".join(arrows)}'
        "</svg>"
    )


_NUMBERS = ("zero", "one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten")


def workflow_svg(product: str) -> str:
    """The preservation pipeline, one card per step.

    The step count in the label is derived from the content, not written
    down: the source document says "six steps" over a seven-step diagram.
    """
    n = len(WORKFLOW)
    label = f"Preservation workflow, {_NUMBERS[n] if n < len(_NUMBERS) else n} steps"

    pad, gap, top, ch = 40, 16, 42, 110
    cw = (CANVAS_W - 2 * pad - gap * (n - 1)) / n

    out = []
    for i, (title, l1, l2) in enumerate(WORKFLOW):
        x = pad + i * (cw + gap)
        optional = l2 == "Optional"
        # A dashed card is dashed more finely than a dashed group box.
        out.append(rect(x, top, cw, ch, stroke=PALETTE["sage"], dashed=optional,
                        dash="5 4"))
        out.append(text(x + 12, top + 22, str(i + 1), size=11, weight="700",
                        fill=PALETTE["sage"]))
        out.append(text(x + cw / 2, top + 50, title, size=13, weight="600",
                        anchor="middle"))
        out.append(text(x + cw / 2, top + 70, l1, size=10.5, anchor="middle",
                        fill=PALETTE["muted"]))
        out.append(text(x + cw / 2, top + 83, l2, size=10.5, anchor="middle",
                        fill=PALETTE["muted"]))
        if i:
            # The arrow sits in the gap between two cards, clear of both.
            xs = x - 3
            out.append(connector([(xs - gap + 6, top + ch / 2), (xs, top + ch / 2)],
                                 dashed=optional))

    out.append(text(pad, 228, WORKFLOW_NOTE.replace("{product}", product),
                    size=12.5, fill=PALETTE["muted"]))

    return (
        f'<svg viewBox="0 0 {CANVAS_W} 262" xmlns="http://www.w3.org/2000/svg" '
        f'role="img" aria-label="{esc(label)}">'
        f'{MARKERS}{rect(0, 0, CANVAS_W, 262, rx=0)}{"".join(out)}</svg>'
    )
