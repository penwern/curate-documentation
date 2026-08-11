"""Data and copy for the architecture overview document.

Nothing in this module knows how to render. Correcting a fact about the
architecture should mean editing this file and nothing else.
"""

from dataclasses import dataclass

# Brand colours, taken from the --pw-* custom properties in penwern-design-system.
PALETTE = {
    "ink": "#0a0f1a",
    "muted": "#6b7280",
    "teal_deep": "#1a3d36",
    "sage": "#83aba3",
    "aqua": "#9fd0c7",
    "mint": "#a6e8ce",
    "wash": "#f6faf9",
    "white": "#ffffff",
    "rule": "#e5e7eb",
}

FONT_STACK = (
    "'Geist','Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif"
)


@dataclass(frozen=True)
class Brand:
    """One product's naming and assets.

    `vendor` is the commercial entity and moves between builds. It is used
    only on branding surfaces. Literal "Penwern" in the copy names who
    operates or builds something and never moves.
    """

    key: str
    product: str
    vendor: str
    entity: str
    logo: str
    out: str


PRODUCTS = {
    "curate": Brand(
        key="curate",
        product="Curate",
        vendor="Penwern",
        entity="Penwern Limited",
        logo="Penwern Logo Large.png",
        out="curate-architecture-overview",
    ),
    "soteria": Brand(
        key="soteria",
        product="Soteria+",
        vendor="Max Communications",
        # Max Communications' legal suffix is unconfirmed, so no "Limited"
        # is assumed here. One-line change if it should carry one.
        entity="Max Communications",
        logo="Max Communications Logo Large.png",
        out="soteria-architecture-overview",
    ),
}
