"""SVG generation for the architecture overview diagrams.

Imports content, knows nothing about HTML. Groups measure themselves so
the canvas height is computed, never hardcoded.

Nothing here inherits paint. A card or group either states its own fill
and stroke in content.py, or it takes the single renderer default below.
A card sitting inside a teal group does not pick up teal.
"""

from dataclasses import dataclass

from content import FONT_STACK, MONO_STACK, PALETTE, Card, Group

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
