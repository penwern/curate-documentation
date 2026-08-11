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

# Bucket names are set in the brand's monospace face, so they read as the
# literal identifiers they are.
MONO_STACK = (
    "'Geist Mono','JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,"
    "Consolas,monospace"
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


@dataclass(frozen=True)
class Card:
    """One labelled box.

    `lines` are the small grey lines under the title. `chips` are the
    small pill labels used for S3 bucket names inside the two storage
    cards. A card may carry both: "Preservation lifecycle" has three
    chips and two explanatory lines beneath them.

    `fill` and `stroke` are empty only where the source paint happens to
    equal the renderer's own default. Nothing inherits: a card sitting in
    a teal group does not pick up teal, so any card the source paints
    differently from that single default states its colour here.

    `chip_fill` is stated for the same reason. Every chip in a card shares
    one fill, but it is not the card's fill: the source tints both chip
    cards differently from the card behind them, so the value is written
    down here rather than taken from the card.
    """

    title: str
    lines: tuple[str, ...] = ()
    chips: tuple[str, ...] = ()
    chip_cols: int = 3
    chip_fill: str = ""
    fill: str = ""
    stroke: str = ""
    dashed: bool = False
    id: str = ""


@dataclass(frozen=True)
class Group:
    """A labelled container holding either a grid of cards or sub-groups.

    A group computes its own height from its contents, so adding a card
    reflows the group and everything below it without a coordinate edit.

    layout: "stack" places children top to bottom, "row" places them side
    by side sharing the width in proportion to their `weight`.

    `lines` are caption lines drawn beneath the group label and above the
    group's contents, belonging to the group rather than to any card. The
    source emphasises the last of them, which is the single-tenancy claim.

    `fill` and `stroke` work as they do on `Card`: empty means the
    renderer default. Every labelled group states both, because the source
    gives each one its own paint and that tinting is information, not
    decoration. Nothing inherits, here or on `Card`: a colour is either
    written down or it is the renderer's default.
    """

    label: str
    lines: tuple[str, ...] = ()
    cards: tuple[Card, ...] = ()
    children: tuple["Group", ...] = ()
    cols: int = 4
    fill: str = ""
    stroke: str = ""
    dashed: bool = False
    layout: str = "stack"
    weight: float = 1.0
    id: str = ""


# Table 1: what a deployment contains. Columns are
# (component, role, technology, data held).
COMPONENTS = [
    (
        "Nginx",
        "TLS termination and request routing",
        "Nginx",
        "None, transit only",
    ),
    (
        "Pydio Cells",
        "File management, workspaces, permissions, search",
        "Go",
        "File metadata, user accounts, permissions",
    ),
    (
        "{product} JS",
        "{product} user interface extensions",
        "JavaScript",
        "None, runs in the browser",
    ),
    ("JS Workers", "Scheduled and background tasks", "Node.js", "None"),
    (
        "MySQL",
        "Core platform metadata",
        "MySQL",
        "Users, workspaces, permissions, node index",
    ),
    (
        "MongoDB",
        "Document store and search index",
        "MongoDB",
        "Indexed content metadata",
    ),
    (
        "NATS",
        "Internal event messaging between services",
        "NATS",
        "Transient events",
    ),
    ("ClamAV", "Virus scanning on ingest", "ClamAV", "None"),
    ("Siegfried", "File format characterisation against PRONOM", "Go", "None"),
    (
        "Email archives",
        "Unpacks uploaded MBOX and PST files into individual messages and "
        "attachments for appraisal",
        "Python",
        "The email archives you upload",
    ),
    (
        "Reporting dashboards",
        "File format and storage reporting inside {product}",
        "Python",
        "Aggregate statistics only",
    ),
    (
        "Preservation API",
        "Preservation configuration service",
        "Go",
        "Preservation configurations, SQLite",
    ),
    (
        "Preservation Core",
        "Preservation workflow orchestration",
        "Go",
        "Transient working copies during processing",
    ),
    (
        "Penwern A3M",
        "AIP creation and PREMIS metadata generation",
        "Python, in Docker",
        "Transient working copies during processing",
    ),
    (
        "Amazon S3",
        "Object storage for all content",
        "AWS S3",
        "All archival content and working files",
    ),
]


# Table 2: optional connectors, installed only for systems the customer
# runs. Columns are (connector, what it does, technology, notes).
CONNECTORS = [
    (
        "Pure connector",
        "Harvests research outputs and their metadata from Elsevier Pure",
        "Python",
        "Runs to a daily schedule",
    ),
    (
        "CALM connector",
        "Ingests catalogue records and attached files from CALM",
        "Python",
        "Uses the CALM SOAP interface",
    ),
    (
        "SharePoint connector",
        "Ingests documents from SharePoint or OneDrive",
        "Python",
        "Uses the Microsoft Graph API",
    ),
    (
        "ArchivesSpace connector",
        "Publishes to ArchivesSpace after preservation, creating the archival "
        "and digital object records that link each catalogue entry to its AIP",
        "Python",
        "You choose the target in the resource tree beforehand",
    ),
    (
        "AtoM deposit",
        "Publishes access copies to an AtoM catalogue",
        "SWORD 2.0",
        "Requires an AtoM instance",
    ),
]


# Table 3: every connection crossing the deployment boundary. Columns
# are (interface, direction, protocol, authentication, data crossing).
INTEGRATIONS = [
    (
        "User web access",
        "Inbound",
        "HTTPS, TLS",
        "{product} account, or client single sign-on via OIDC",
        "All user content and metadata",
    ),
    (
        "Single sign-on",
        "Outbound",
        "OIDC",
        "Client identity provider, standard OIDC flow",
        "Identity assertions only, no content",
    ),
    (
        "Preservation API",
        "Inbound via Nginx",
        "HTTPS, REST",
        "OIDC bearer token validated against {product}, with a "
        "trusted-address allowance for host-local calls",
        "Preservation configuration",
    ),
    (
        "Reporting dashboards",
        "Inbound via Nginx",
        "HTTPS, REST",
        "OIDC session verified by Nginx against {product}",
        "Aggregate statistics only",
    ),
    (
        "Object storage",
        "Outbound",
        "S3 API over HTTPS",
        "AWS IAM instance role, no static keys on the host",
        "All content, encrypted in transit and at rest",
    ),
    (
        "Pure, CALM or SharePoint",
        "Outbound. {product} reads from your system",
        "HTTPS REST, or SOAP for CALM",
        "An account on your system that you create for {product} and can "
        "revoke at any time",
        "Catalogue records, descriptive metadata and files that {product} "
        "ingests from that system",
    ),
    (
        "ArchivesSpace",
        "Outbound. {product} writes to your catalogue",
        "HTTPS REST",
        "An ArchivesSpace account you create for {product} and can revoke at "
        "any time",
        "Archival and digital object records describing preserved content. No "
        "files are sent",
    ),
    (
        "AtoM deposit",
        "Outbound",
        "SWORD 2.0 over HTTPS, plus rsync",
        "AtoM API key and a dedicated deposit account",
        "Access copies and descriptive metadata",
    ),
    (
        "Penwern support access",
        "Inbound",
        "SSH",
        "Named engineers, key based, no shared accounts",
        "Administrative access to the instance",
    ),
    (
        "Monitoring",
        "Outbound",
        "HTTPS",
        "Penwern-operated endpoint",
        "Availability and resource signals, no content",
    ),
    (
        "Backup",
        "Internal to AWS",
        "AWS Backup",
        "AWS IAM service role",
        "EC2 volume snapshots, held in the same region",
    ),
]


# The deployment facts panel, as (label, value) pairs.
FACTS = [
    (
        "Region",
        "AWS eu-west-2 (London) by default, so content and backups remain in "
        "the United Kingdom. We can deploy to your local AWS region instead "
        "where residency requires it.",
    ),
    (
        "Tenancy",
        "Dedicated EC2 instance and dedicated S3 buckets. No storage or "
        "compute is shared between customers.",
    ),
    (
        "Encryption",
        "TLS in transit. AES256 at rest on all buckets, with "
        "customer-supplied-key uploads refused.",
    ),
    (
        "Public access",
        "Blocked at bucket level on every bucket, with all four S3 public "
        "access controls enabled.",
    ),
    (
        "Backup",
        "Daily snapshots of the instance, retained for seven days, held in "
        "the same region.",
    ),
    (
        "Operating hours",
        "A daily operating window agreed with you, covering your working day. "
        "Running only when needed keeps the environment efficient and the "
        "cost predictable.",
    ),
    (
        "Deployment",
        "Provisioned and configured entirely from version-controlled "
        "Terraform and Ansible, so environments are reproducible.",
    ),
    (
        "Support access",
        "Named Penwern engineers over SSH using individual keys. No shared "
        "accounts.",
    ),
]


# The four summary pills under the lede.
PILLS = [
    "Single-tenant",
    "UK hosted by default",
    "Encrypted at rest and in transit",
    "Managed by {vendor}",
]


# The architecture diagram, as a box tree. Every id below is an arrow
# anchor, so renaming one silently detaches an arrow.
ARCH_TREE = Group(
    label="",
    layout="stack",
    children=(
        Group(
            id="client", label="CLIENT ENVIRONMENT", cols=4,
            fill="#f6faf9", stroke="#83aba3", dashed=True,
            cards=(
                Card(id="idp", title="Identity provider",
                     lines=("Azure AD or equivalent",
                            "Optional single sign-on")),
                Card(id="users", title="Users",
                     lines=("Archivists, researchers,", "depositors")),
                Card(id="sources", title="Your source systems",
                     lines=("Pure, CALM, SharePoint",
                            "Optional, one connector per system you use")),
                Card(id="support", title="Penwern support access",
                     lines=("Named engineers, SSH key based",
                            "Monitoring and maintenance")),
            ),
        ),
        Group(
            id="aws", label="AWS  ·  EU-WEST-2 (LONDON) BY DEFAULT",
            layout="row", fill="#fbfdfd", stroke="#83aba3",
            children=(
                Group(id="ec2", label="EC2 INSTANCE", weight=2.0,
                      fill="#ffffff", stroke="#6b7280", children=(
                    Group(id="edge", label="", cols=1, cards=(
                        Card(id="nginx", title="Nginx",
                             fill="#f5f7f7", stroke="#6b7280",
                             lines=("TLS termination and request routing",)),
                    )),
                    Group(id="platform", label="{product} PLATFORM", cols=4,
                          fill="#fcfefe", stroke="#9fd0c7",
                          cards=(
                        Card(id="cells", title="Pydio Cells",
                             stroke="#9fd0c7",
                             lines=("Files, workspaces,",
                                    "permissions, search")),
                        Card(id="curatejs", title="{product} JS",
                             stroke="#9fd0c7",
                             lines=("User interface", "extensions")),
                        Card(id="jsworkers", title="JS Workers",
                             stroke="#9fd0c7",
                             lines=("Scheduled and", "background tasks")),
                        Card(id="nats", title="NATS",
                             stroke="#9fd0c7",
                             lines=("Internal event", "messaging")),
                        # The six tinted cards: supporting services, set
                        # apart from the four white cards above them.
                        Card(id="mysql", title="MySQL",
                             fill="#f2fbf7", stroke="#a6e8ce",
                             lines=("Core platform", "metadata")),
                        Card(id="mongodb", title="MongoDB",
                             fill="#f2fbf7", stroke="#a6e8ce",
                             lines=("Document store", "and search index")),
                        Card(id="clamav", title="ClamAV",
                             fill="#f2fbf7", stroke="#a6e8ce",
                             lines=("Virus scanning", "on ingest")),
                        Card(id="siegfried", title="Siegfried",
                             fill="#f2fbf7", stroke="#a6e8ce",
                             lines=("Format characterisation",
                                    "against PRONOM")),
                        Card(id="email", title="Email archives",
                             fill="#f2fbf7", stroke="#a6e8ce",
                             lines=("Unpacks uploaded",
                                    "MBOX and PST files")),
                        Card(id="reporting", title="Reporting dashboards",
                             fill="#f2fbf7", stroke="#a6e8ce",
                             lines=("File format and", "storage statistics")),
                    )),
                    Group(id="pipeline", label="PRESERVATION PIPELINE", cols=4,
                          fill="#f7fcfb", stroke="#83aba3",
                          cards=(
                        Card(id="presapi", title="Preservation API",
                             lines=("Configuration", "service")),
                        Card(id="sqlite", title="SQLite",
                             lines=("Preservation", "configurations")),
                        Card(id="prescore", title="Preservation Core",
                             lines=("Workflow", "orchestration")),
                        Card(id="a3m", title="Penwern A3M",
                             lines=("AIP creation and", "PREMIS metadata")),
                    )),
                    Group(id="connectors",
                          label="OPTIONAL CONNECTORS  ·  INSTALLED ONLY FOR "
                                "SYSTEMS YOU USE",
                          fill="#fafafa", stroke="#9ca3af",
                          dashed=True, cols=1, cards=(
                        Card(id="conncard",
                             title="Source and catalogue connectors",
                             stroke="#9ca3af", dashed=True,
                             lines=("Pure, CALM and SharePoint bring records "
                                    "in.  ArchivesSpace publishes out.",
                                    "One service per system you use")),
                    )),
                )),
                # Right column stacks three siblings, not one S3 box.
                Group(id="right", label="", weight=1.0, children=(
                    Group(id="s3", label="AMAZON S3  ·  OBJECT STORAGE",
                          lines=("Encrypted at rest (AES256) · public "
                                 "access blocked",
                                 "Every bucket is dedicated to you, "
                                 "never shared"),
                          fill="#f2fbf7", stroke="#a6e8ce",
                          cols=1, cards=(
                        Card(id="working", title="Working storage",
                             stroke="#a6e8ce", chip_cols=3,
                             chips=("cells", "pydiods1", "personal",
                                    "thumbs", "versions", "binaries")),
                        Card(id="lifecycle", title="Preservation lifecycle",
                             stroke="#a6e8ce", chip_cols=3,
                             chip_fill="#f2fbf7",
                             chips=("quarantine", "appraisal", "archive"),
                             lines=("Virus scan and format characterisation",
                                    "on the way through")),
                    )),
                    # Both grey, because both sit outside the tenant. The
                    # groups around them draw no box, so the stroke cannot
                    # be inherited and has to be stated.
                    Group(id="backupg", label="", cols=1, cards=(
                        Card(id="backup", title="AWS Backup",
                             fill="#f5f7f7", stroke="#6b7280",
                             lines=("Daily EC2 snapshots, 7 day retention",
                                    "Managed in the same region")),
                    )),
                    Group(id="monitorg", label="", cols=1, cards=(
                        Card(id="monitor", title="Monitoring",
                             fill="#f5f7f7", stroke="#6b7280",
                             lines=("Penwern operated, outside the tenant",
                                    "Availability and resource checks")),
                    )),
                )),
            ),
        ),
        Group(
            id="catalogues", label="YOUR CATALOGUE SYSTEMS  ·  OPTIONAL",
            fill="#f6faf9", stroke="#83aba3", dashed=True, cols=1,
            cards=(
                # Solid in the source: the dashed group box around them
                # already carries the optionality, and its label says so.
                Card(id="aspace", title="ArchivesSpace",
                     lines=("Archival objects linked to each preserved AIP",)),
                Card(id="atom", title="AtoM",
                     lines=("Archival access and public catalogue",)),
            ),
        ),
    ),
)


# The preservation pipeline diagram, as (title, line 1, line 2).
WORKFLOW = [
    ("Trigger", "A user selects content", "and chooses Preserve"),
    ("Retrieve", "Package copied to the", "processing area"),
    ("Pre-processing", "Transfer assembled,", "your metadata attached"),
    ("Penwern A3M", "Characterisation,", "normalisation, PREMIS"),
    ("Post-processing", "AIP assembled, and", "compressed if configured"),
    ("Store", "AIP written to the", "Archive workspace"),
    ("Access copy", "DIP deposited to AtoM", "Optional"),
]

WORKFLOW_NOTE = (
    "Preservation status is written back to the item in {product} at each "
    "step, so progress and failures are visible to the user throughout. "
    "Empty or invalid packages are rejected at pre-processing, before "
    "anything is submitted for processing."
)


# Every block of running copy in the document.
PROSE = {
    "lede": (
        "This describes a standard {product} deployment. {product} is "
        "delivered as a dedicated, single-tenant installation: each customer "
        "has their own instance and their own storage, with nothing shared "
        "between customers."
    ),
    "security_note": (
        "<strong>No inbound connections other than those listed.</strong> "
        "The instance security group admits only HTTPS on 443, HTTP on 80 "
        "(which redirects to HTTPS), and SSH for named Penwern engineers. "
        "No other inbound port is open, so the application services behind "
        "the reverse proxy cannot be reached directly from outside the "
        "instance. Object storage is reached outbound using an AWS instance "
        "role, so no long-lived storage credentials are held on the server."
    ),
    "footer": (
        "{entity} · {product} architecture overview · Prepared for customer "
        "review. This document describes the standard deployment; the final "
        "configuration is confirmed during onboarding."
    ),
    "arch_intro": (
        "The diagram below shows the components of a deployment, the "
        "boundaries between them, and every point at which the system "
        "connects to something outside itself. Solid outlines are always "
        "present; dashed outlines are optional and are enabled only where a "
        "customer needs them."
    ),
    "arch_caption": (
        "{product} deployment architecture. Optional modules and connections "
        "are shown with dashed outlines."
    ),
    "components_intro": (
        "Every deployment includes the following. All of them run on a single "
        "dedicated EC2 instance, with content held in dedicated S3 buckets."
    ),
    "connectors_intro": (
        "{product} can connect to systems you already run. Connectors work in "
        "both directions: Pure, CALM and SharePoint bring records and files "
        "into {product} so they do not have to be uploaded by hand, while "
        "ArchivesSpace works the other way, publishing catalogue entries out "
        "once content has been preserved. Each connector signs in using an "
        "account you provide, runs as its own service, and is installed only "
        "if you use that system, so a deployment carries nothing it does not "
        "need."
    ),
    "integrations_intro": (
        "Every connection that crosses the boundary of the deployment, in "
        "either direction."
    ),
    "workflow_intro": (
        "What happens when a user preserves content. Your files are prepared "
        "and validated before processing begins, and the resulting package is "
        "assembled and checked afterwards, so preservation is a managed "
        "pipeline rather than a hand-off. Steps 1 to 6 are always performed; "
        "step 7 applies only where an access catalogue is connected."
    ),
    "workflow_caption": (
        "The preservation pipeline. Packages are processed one at a time per "
        "instance, so throughput is predictable and the archive is never left "
        "in a partial state."
    ),
}
