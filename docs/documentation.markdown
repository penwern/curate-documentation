<link rel="stylesheet" href="/curate-documentation/style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@mdi/font@7.4.47/css/materialdesignicons.min.css">
<script>
document.addEventListener('DOMContentLoaded', function() {
    
  // Find all nav links with submenus
  document.querySelectorAll('.md-nav--secondary .md-nav__link').forEach(function(link) {
    const parentLi = link.closest('.md-nav__item');
    const submenu = parentLi.querySelector('.md-nav');
    if (submenu) {
      // Initially collapse all submenus
      submenu.style.display = 'none';

      // Add expand/collapse button
      let chevron = document.createElement('span');
      chevron.classList.add('mdi', 'mdi-chevron-down');
      chevron.style.cursor = 'pointer';
      link.appendChild(chevron);

      // Attach click event to toggle submenu
      chevron.addEventListener('click', function(e) {
        e.preventDefault();

        // Toggle the mdi-chevron icon
        chevron.classList.toggle('mdi-chevron-down');
        chevron.classList.toggle('mdi-chevron-up');

        // Toggle only the direct submenu visibility
        if (submenu) {
          submenu.style.display = submenu.style.display === 'none' ? '' : 'none';
        }

        // Collapse nested submenus when parent is expanded to ensure only the first layer is visible
        if (!chevron.classList.contains('mdi-chevron-down')) {
          const nestedSubMenus = submenu.querySelectorAll('.md-nav');
          nestedSubMenus.forEach(nestedSubMenu => {
            nestedSubMenu.style.display = 'none';
            // Find and reset chevrons in nested menus
            const nestedChevrons = nestedSubMenu.closest('.md-nav__item').querySelectorAll('.mdi-chevron-up');
            nestedChevrons.forEach(nestedChevron => {
              nestedChevron.classList.remove('mdi-chevron-up');
              nestedChevron.classList.add('mdi-chevron-down');
            });
          });
        }
      });
    }
  });
});

</script>

<img src="/curate-documentation/assets/Penwern Logo Large.png" style="width: 10em;"></img>

# Penwern Curate <span style="font-size: 8pt;vertical-align: super;">TM</span>

Penwern Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> is a comprehensive software platform that addresses
the fundamental issues with existing Digital Archiving solutions,
allowing organisations of any size to build, preserve and manage
best-practice Digital Archives with ground-breaking speed and
simplicity.

## Why is eArchiving important for any organization?

Valuable digital content can be become inaccessible, unusable, or
untrustworthy due to a number of factors, such as:

-   Files have been damaged or made inaccessible by viruses or malware.

-   Files are corrupted.

-   File types have become obsolete or software to read them is not
    available.

-   The authenticity of the data is in question as you cannot prove that
    a file hasn't changed.

-   You cannot find specific files due to a lack of understandable
    organisation or description.

Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> helps to fix these problems by:

-   Removing threats due to viruses and malware through a system or
    virus checks and quarantine.

-   Checksumming all files and regularly checking the integrity of files
    in its store.

-   Characterising file types by MIME type and Pronom ID so that you can
    monitor your holdings and take decisions on strategies to manage
    file type and software obsolescence.

-   Automatically extracting technical metadata.

-   Allowing you to organize your file-store any way you wish, but also
    to add descriptive metadata to files and folders so that you can
    search on multiple attributes.

-   Allowing you to retain all meta-information, and uniquely associate
    it with each object.

-   Allowing you to perform format migration on your objects to
    normalise their types to archival standards.

-   Preparing your content into standards-conformant information
    packages.

## Is Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> Useful for Archivists and Digital Curators?

Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> is a platform that can be used to provide a number of
critical functions within an electronic archiving system discretely or
can form a complete and effective system itself. Individually,
Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> can perform the following roles:

 - Ingest, Upload and Accession

 - Smart Deposit System

 - Metadata Extraction

 - Transcriber

 - Fixity Agent

 - Appraisal System

 - Selection and Arrangement Workspace

 - Reporting System

 - Unified Description Tool

 - Digital Preservation System

 - OAIS Information Packaging

 - Document Editing

 - Advanced Access System

 - Public Access Portal

In combination, these services mean that Curate comprises a
comprehensive and highly capable electronic archiving system all on its
own.

## Is Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> Useful for Business?

Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> is a file sharing platform that integrates the features
required for the preservation of data that go beyond basic data
protection (back-up, integrity checking, disaster recovery).

The standards-based principles of digital preservation and eArchiving
that Curate is built upon are rapidly becoming critical functions for
all businesses to practice. Curate removes many of the significant
barriers to entry that prevent businesses from effectively implementing
digital preservation and eArchiving.

It is cost effective, allowing you to create an archive for inactive
data that doesn't take up valuable storage on your primary storage
systems and allows you to consolidate data into a single platform.
Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> works in a way your users understand, with a best-in-class
user experience. You don't have to train all your users on new, complex
digital preservation applications.


## General

### Devices

Curate is supported on any device: computers, phones, and tablets.
Simple navigate to your Curate instance via your device's web-browser.
You may find compatibility issues with older or unsupported operating
systems.

### Log In

After navigating to your Curate instance, you will be asked to log in.
Curate can be configured to use external SSO providers, if desired by
your organisation. It can also integrate with LDAP/Active directory. If
multi-factor authentication is enabled (hardware and software
supported), you will be prompted to provide it. Your SSO and log-in
security requirements will have been discussed and integrated during
your signup.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image2.png" style=""></img>
</div>

## Application Areas

### Home Screen

When you log in to Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> you will see the home screen as shown
below and you will be guided through a short welcome tour. The home
screen provides you with links to recent content, and ways to navigate
through the rest of the application.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image3.png" style=""></img>
</div>

In the centre-top of the home screen, you will find the search bar. At
the far left, you can see the navigation panel.

You can find your account settings and preferences, as well as the
option to log out, by clicking on the profile icon in the navigation
panel.

Beneath that is the home button, which will return you to this screen.

At the bottom of the navigation panel, you can find your notifications
centre by hovering over the bell icon.

You can also switch between light and dark colour modes with the toggle
at the very bottom of the navigation panel.

### Bookmarks


The bookmarks tab can be accessed from the icon in the navigation panel. 
The bookmarks tab keeps references to all the files and folders you have 
saved using the "bookmark" feature [(*see bookmarking a file or folder*)](#bookmarking-a-file-or-folder). 
Clicking one of the items will navigate you to its location in Curate. 
If you want to remove an item from your bookmarks, click the <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image4.png" class="text-icon"style=""></img> icon 
next to the item you wish to remove.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image5.png" style=""></img>
</div>

### Workspaces

To open your workspaces panel, hover over the "All Files" button in the
navigation panel.

You will see the following spaces:

-   Personal files

-   Quarantine Space

-   Appraisal Space

-   Archive Space

-   Common Files

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image6.png" style=""></img>
</div>

Workspaces are where you perform your eArchiving workflow within Curate,
and where you'll be able to describe, arrange and eventually preserve
your objects.

Each workspace can be individually encrypted at the data source and
given its own independent fixity checking schedule.

Each workspace has a defined function, here is a quick explanation of
what each workspace is for:

#### Personal Files

This is a workspace that is only visible to you and not to other members
of your workgroup. You can upload files or folders to this space for
your own personal content, which would not normally be part of a group
archive.

Files uploaded into Personal are virus checked once and should not be moved
out into any other area of Curate <span style="font-size: 8pt;vertical-align: super;">TM</span>. 
If you have files in Personal that you do want to add to the archive, you should move them
into Quarantine so they can be submitted for a full quarantine period.

Files in Personal are not characterised, but you do have basic file
information available and you can add descriptive metadata. Note that
file downloads do not include descriptive metadata so the Personal
workspace should not be used for appraisal or arrangement of archival
content.

#### Quarantine Space

Content that is to be appraised and arranged in Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> should be
uploaded into the Quarantine workspace [(*see upload and ingest for more information*)](#upload-and-ingest). This is a shared workspace and so is visible to all
members of a workgroup. Uploaded files are virus checked and quarantined
for 30 days. It is recommended that files should not be moved from the
Quarantine workspace until the quarantine period is up, however
Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> is not prescriptive and you can choose to move files out early if you wish.

If the virus scanner detects a virus or malware then the affected file
will be moved to a folder called Infected within the Quarantine
workspace.

After the 30-day quarantine period and a second successful virus scan,
files are moved automatically into the Appraisal space and labelled "Released".

#### Appraisal Space

Files moved to the Appraisal space are characterised by the open-source
file characterisation tool Siegfried, which generates a file type unique
identifier from the PRONOM registry of filetypes maintained by the
National Archive (see <https://www.nationalarchives.gov.uk/PRONOM/>).

Once Siegfried has completed its analysis, the identified PRONOM ID is added to the file information area. 
Clicking on the PRONOM ID will open a new tab in your browser linked to the PRONOM registry page with more detailed information on the file format.

Within the Appraisal workspace you can move, copy and delete files, create folders and add
descriptive metadata. Using detailed file information you can make
appraisal decisions. From the appraisal space, you can also preserve and
package your objects in any configuration you wish. [*See appraisal*](#appraisal-selection-and-arrangement) [*preservation*](#preservation) and [*packaging*](#packaging) for more information.

#### Archive Space

Files and folders can be moved to the Archive workspace for long-term
retention. The organisation of the workspace is up to you, but the
search function can help any system you have by allowing simple searches
on filenames or advanced searches on descriptive metadata. AIPs generated
by the preservation process are also uploaded to the Archive workspace by default.

#### Common Files Space

The Common Files space is a shared area within a workgroup that can be
used to store shared reference documents and files, for example: user
guides, references, submission agreements, metadata schemas etc.

### Object information area

The object information area provides you with all the critical details
about a file or object inside Curate. The object information area will
appear on the right-hand side of the screen when you select a single
file or folder.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image7.png" style=""></img>
</div>

#### Object information area panels

##### File actions panel

The first panel in the object information area is file actions, which
shows a preview of the object you have selected and presents options to
share, download, or open the file in one of Curates rendering tools.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image8.png" style=""></img>
</div>

##### File information panel

The file information panel lists all the basic characteristics of the
selected object, along with the quarantine status, scan results and
detailed characterization information when the file has been appraised.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image9.png" style=""></img>
</div>

##### Extracted metadata panels; EXIF etc

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image10.png" style=""></img>
</div>

When you select a file that includes some
additional technical metadata, like a photograph with EXIF, Curate will
automatically extract it and display it in a new card in the object
information area. Click on "more" to view the full extracted EXIF data.

##### Metadata panel

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image11.png" style=""></img>
</div>

Clicking on any file or folder in Curate
will open the metadata panel in the object information area. The
Curate metadata panel comes with simple 15 field Dublin Core and 26
field ISAD(G) schemas built in. Any additional standardised or
customized schemas can be supported upon request. There is also a field
for custom tags, which are displayed as colourful tags in the file list.

The metadata panel also contains the "import" and "export" sections. The
import section allows you to import external DC, ISAD or any other
associated meta file to an object. It also provides fields for entering
the details of an external OAI-PMH record, from which you can harvest
and import its metadata. See [*importing metadata*](#) for more. The export
section allows you to make an object harvestable via your Curate systems
OAI-PMH server. See [*exporting records*](#) for more detail.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image12.png" style=""></img>
</div>

##### Comments

Each object in Curate has its own comments section that lets you leave
notes or comments for yourself or your colleagues.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image13.png" style=""></img>
</div>

##### File activity

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image14.png" style=""></img>
</div>

The final panel in the object information area, when a file or folder is selected in the file list, 
is the file activity panel. The file activity panel records and displays a log of
all the actions and modifications taken that relate to the selected
object. Please note that the activity stream does not record PREMIS
preservation events. Those are recorded internally. See [*PREMIS in Curate*](#premis-in-curate) for more information.

## Upload and Ingest

### Uploading Files and Folders into Quarantine

Files and Directories can be simple and quickly uploaded into
Curate <span style="font-size: 8pt;vertical-align: super;">TM</span>, but only into the Personal and Quarantine workspaces. If
files are uploaded into the Personal workspace they cannot be moved out
into any other workspace. Any file which is uploaded or moved into the
Quarantine workspace will be virus checked and a visual indication given
if the virus check was successful and the file virus free. Any file that
is found with a virus is immediately moved to a folder within the
Quarantine workspace called Infected. Files will be automatically
re-scanned for viruses after 30 days if they are left in the Quarantine
workspace, after which time they are then labeled Virus Free and
available for Release. Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> does not stop you from moving files
out of Quarantine at any time you wish.

### Advanced Web-uploader

The advanced web-uploader is the main ingest tool in Curate. It's fast,
efficient and offers several useability benefits over other, lower level
upload methods. The advanced web-uploader can handle ingests of
thousands of files and tens of gigabytes, making it capable of
processing most common ingest workloads.

<div class="tip"><span class="mdi mdi-information-outline"></span><span>If you have thousands of files to upload, you can compress your
objects into an archive package locally and then upload that instead.
This will greatly improve your upload performance.</span></div>

We would strongly recommend using the advanced web-uploader for the
majority of your ingests, where the size and volume is appropriate.

Try uploading files and folders (you can upload any complex folder
structure) using the advanced web-uploader. You can do this by selecting
'New' at the top of the screen, and then Upload.

You can drag and drop into the pop-up box or select to upload files or
folders. If you are uploading a large file or folder you can minimize
the upload window by clicking the X in the top right. You can then carry
on working and see the progress of the upload at any time by clicking
the 'Jobs Running' area at the bottom left of the window. New upload
jobs can be added at any time and will just be added to the upload
queue.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image15.png" style=""></img>
</div>

You can also simply drag your objects into the Curate window with the
appropriate location open and the content will be uploaded directly.

#### Web-uploader Options

When using the Curate web-uploader, you can also set configuration
options that dictate how Curate handles certain situations that can be
dangerous to an archiving workflow.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image16.png" style=""></img>
</div>

**Start uploading automatically**

Selecting this option means that each file you add to the uploader will
begin to upload immediately. If you disable this option, you can begin
to load all of the parts of an upload before beginning pieces of it at a
time. This can help you manage complex or large uploads on a sub-optimal
connection.

**Close panel after upload is finished**

Enabling this option will close the upload panel as soon as the final
file has finished uploading to Curate. Leaving this option disabled will
allow you to browse your completed uploads in the panel and at-a-glance
verify that they have valid integrity checks [*see pre-upload integrity verification*](#pre-upload-integrity-verification).

**If a file with the same name exists**

These exclusive options allow you to dictate how Curate handles uploads
of files with duplicate names. Note that this does not check for
duplicates based on their content, only their name. You should generally
avoid uploading multiple files with the same name to a single folder or
area intentionally. If you select "rename files", each file with a
duplicated name will have a numbered suffix. "merge folders" means that
files inside a folder with a duplicated name will instead be uploaded to
the original folder. Any duplicated files within the merged folder will
be treated with the "rename files" process.

#### Pre-upload Integrity Verification

When uploading objects using the Curate web-uploader, it automatically
generates and compares pre and post-upload checksums. A label indicating
the result of each files integrity check will appear underneath each
item in the uploader window.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image17.png" style=""></img>
</div>

Each of your files will also have a label attached which permanently
records the result of the integrity check.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image18.png" style=""></img>
</div>

### SFTP

Curate offers a connection to your workspaces over SFTP, allowing you to
ingest more massive uploads of content into your quarantine space than
the advanced web-uploader can handle. The SFTP protocol is more capable
for massive uploads than HTTPS used in the advanced web-uploader, but
uploading through SFTP in Curate necessitates a system reindex.

As a result, you will either need to schedule your planned SFTP upload
with us ahead of time or, if the workload is not time critical, feel
free to contact us once the upload has completed.

If you require SFTP upload in your Curate instance, please let us know
when you procure Curate for your organisation, or send us a support
ticket.

*Remember, we'd strongly advise you to use the advanced web-uploader for
most ingest usecases. It's best to only use sftp if your institution
explicitly requires it.*

#### Connecting to and Uploading Through SFTP

You can connect to your Curate workspaces over SFTP using any common FTP
client. If SFTP is enabled for your Curate instance, you will be
supplied the relevant connection details by email when they are
provisioned.

#### SFTP Integrity Verification

Warning: it is difficult to maintain integrity verification for all your
ingested files when uploading through SFTP. Many FTP clients offer often
poor support for checksum features integrated with the protocol, as a
result Curate is unable to automatically verify your SFTP uploads
integrity.

To resolve this, you will need to generate a JSON manifest of checksums
for your ingest content before you perform your SFTP upload, and then
perform manual ingest integrity verification once it is complete. [*See Manual Ingest Integrity Verification for more information.*](#manual-ingest-integrity-verification)

Once you have generated your checksum manifest, you may proceed to
upload your content via SFTP. Once your content is uploaded, and we have
completed the necessary reindex, you can upload your checksum manifest.
[*See Manual Integrity Verification for more information*](#manual-ingest-integrity-verification)

### Ingest Integrity Verification

Curate offers powerful methods for ingesting content into the system
which come with automated facilities for verifying that your files were
not compromised as they were uploaded to the system.

Uploads using the Advanced Web-uploader will
have their integrity verified completely automatically. Curate will
notify you with status tags attached to the respective object if any
items in your ingest workload are found to have been compromised during
the upload process.

Uploads using SFTP require manual checksum verification, which you can
read more about below.

####  Manual Ingest Integrity Verification

If you spot an inconsistency in the checksums or verification results
generated by Curate during your ingest upload, if you'd like to manually
verify that the automatic validation was completed successfully, or if
you have chosen to upload your content using a method that does not support automatic validation, you might need to
perform manual ingest integrity verification.

To perform manual ingest integrity verification, follow these steps:

##### Generating a checksum manifest

There are free several tools available to do this, but your chosen tool must be able to generate MD5 checksums, and it must be
able to provide a manifest file in this format:

**Comments and Metadata:** Lines starting with a semicolon (;) should include metadata about the checksum generation, such as the software used, URL for more information, and the timestamp of generation.

**Checksum Entries:** Each line contains an MD5 checksum followed by the filename, separated by an asterisk (*)

<div class="code-block">
        <div class="code-header">
            <span class="code-title">Example Function</span>
            <span class="code-language">JavaScript</span>
        </div>
        <pre>
            <code>
                [md5_checksum] *[filename]
            </code>
        </pre>
</div>

**Footer:** Optionally, a footer can summarize the process, e.g., total number of files hashed.

**Example of a Properly Formatted Checksum Manifest**

<div class="code-block">
        <div class="code-header">
            <span class="code-title">Example Function</span>
            <span class="code-language">JavaScript</span>
        </div>
        <pre>
            <code>
                ; Checksums generated by ExampleSoftware 1.0.0
                ; http://www.example.com
                ; 4/16/2023 9:25:42 PM
                \n
                f5c5777e2e66258b2b4e1a5820fb3eff *CNA_HIST_ADAQuestionsAndAnswersDocument.mp3
                ae7f5ebd507470dc7944cb64909ec665 *CNA_HIST_AdvisoryMeeting_2007_12_12.mp3
                ; 2 files hashed.
            </code>
        </pre>
</div>


<div class="tip"><span class="mdi mdi-information-outline"></span><span>
For best practice, we recommend uploading your checksum manifest
separately through the advanced web-uploader. This ensures the manifest
itself was uploaded without issue.
</span></div>


### Quarantine

#### Results

Once a file has been uploaded, the initial quarantine virus scan will
run and you will see a tag appear on the file listing. You can find
detailed results for each scan in the quarantine process in the file
information panel, see *file information panel* for more detail.

##### Quarantined

"Quarantined" indicates that the file has been successfully scanned and
no immediate threats were detected. The file has now begin it's 30 day
quarantine period.

##### Risk

Files that are found to be compromised or infected are labeled "Risk"
and are immediately relocated to the infected directory.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image19.png" style=""></img>
</div>

##### Released

After 30 days has passed, the second virus scan will be performed. If no
further threats are found, the quarantined files status label will
change to "Released".

### Uploading File and Folders into Personal

The upload process into the Personal Workspace is functionally
identical, but note two major differences:

-   Files will be virus scanned once only.

    -   If safe, the file is tagged "Passed".

    -   If compromised, the file is moved to an infected directory.

-   You cannot move files out of the personal workspace.

### Other Upload Methods

You can also get content into Curate using SFTP, webdav and with
physical data transport devices when on-cloud.

### Creating and Using a Deposit Space

Curate allows you to share any file, folder or other area (see *Sharing
files or folders* for more detail). By allowing users of a shared area
upload permissions, you can easily create a secure space for your
submitters to deposit their content.

Be sure to create your deposit space in the Quarantine workspace, so
that your deposited files are automatically quarantined. You are also
unable to upload files in to workspaces other than Quarantine and
Personal.

#### Setup

First create and share a folder for your deposit space. This folder is
where your depositors will upload their content. [(*see sharing a file or folder*)](#sharing-a-file-or-folder)

Once shared, you can enable "Upload files" under the permissions tab.
You should typically disable download permissions unless you want your
depositors to be able to download content from other depositors.

Under the "Access restrictions" tab, you can choose to set a password
for the space, and even specify an expiry period for the sharing link.
NB: once your sharing link has expired, nothing will happen to your
shared files or folders, the public URL will simply become inaccessible.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image20.png" style=""></img>
</div>

#### Usage

You may then share your deposit URL with your collaborators. They will
be presented with a simple interface into which they can upload their
deposit.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image21.png" style=""></img>
</div>

#### Simple upload interface

You can also choose to give your depositors an ultra-simple "drop files
here" style interface instead. Not only does this simplify the process
of uploading files for your submitters even further, but it also ensures
that they are unable to see any other content that has been uploaded
into the space. To change the deposit space interface, open the "link
label" section in the sharing configuration. Select "Drop Files Here"
for the simple upload interface. *Hint: make sure to save your changes.*

### Creating and Using a Smart Deposit Space

Smart Deposit Spaces allow you to require specific files, formats,
contents, documentation and even metadata from your depositors. You can
even leave them personalized messages upon submission, or chain
additional actions in your workflow.

Just like other Deposit spaces, make sure to create it in your
Quarantine workspace. You are unable to upload files into other
workspaces, and it will ensure that all your deposits are automatically
quarantined.

To create a Smart Deposit Space, first create a deposit space (see
creating and using a deposit space). Then, open your new deposit space
and right click in the empty space. You should then select the "Smart
Form" option.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image22.png" style=""></img>
</div>

The Smart Form builder will allow you to select what file formats you
require in your deposits in the "Expected Files" section. This will also
allow you to describe the required files, add authorized extensions and
size limitations.

You can then define what other information or metadata you require in
the "Submission Form" section.

Follow on actions and submission messages can be configured in the
"Legends and Completion" section.

In the "Creating and Using a Deposit Space" section, you can find more
information about the configuration options for your shared space,
including password protection, file visibility, access restrictions and
more.

Once you have created your Smart Deposit Space, you can save it and
disseminate the URL. Users accessing the link will be presented with a
form requesting the information you have described. Their uploads will
be rejected without any processing if the requirements are not met. The
users are unable to submit their deposit until they have completed all
your mandatory requirements.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image23.png" style=""></img>
</div>

## Appraisal, selection and arrangement

### Move Content into Appraisal

Files will be moved into the Appraisal workspace when they have
completed quarantine and two successful virus scans. Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> is not
prescriptive however and you can move data early. The Appraisal
workspace is used to create arrangements (folder structures containing
your files), conduct content appraisal helped by the file information
available and to create descriptions.

Try moving files and folders from the Quarantine workspace into
Appraisal. You can do this by selecting, right clicking and selecting
Move or by dragging and dropping to a different workspace in the listing
in the lefthand column. Multiple files or folders can be selected for
each move using the usual Control or Shift operations.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image24.png" style=""></img>
</div>

Note that if files are moved into Appraisal early (i.e. before the
quarantine period is up) then the Quarantine Status tag changes to Risk
to indicate that full quarantine conditions were not met.

Once you have files in the Appraisal workspace, Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> runs
comprehensive file characterisation programmes. To access the generated
characterization information, select a file and check the file
information panel in the object information area. [(*see File Information Panel*)](#file-information-panel). Characterised objects will include these fields in their
information area:

-   File MIME type

-   PRONOM ID

In Appraisal you can try creating folders ('New/New Folder') and moving
files between folders to create an arrangement.

You can also move, copy, rename, delete, lock and bookmark files with
right mouse click functions. Certain media and text files can be
viewed/rendered by double clicking the file.

The Compress option allows you to create a compressed package of a
folder in .zip, .tar or .tar.gz format. The original folder is retained
when you do this. You can use this to compress your archive packages, or
for any other general utility purpose.

Note that you can also move files from Quarantine into Personal, but you
will not be able to move them back out!

### Creating Descriptive Records

While you can begin to describe your files and folders from the moment
they are uploaded to Curate, many users choose to wait until the objects
have completed their Quarantine period successfully and have been
characterized in the appraisal space. This approach gives you the most
complete understanding of the object before describing it, it also
ensures you do not spend time describing files that have been deemed
unsafe.

Note that any description you apply to files in their quarantine period
will be retained, all metadata is retained with a file no matter where
it goes in the system.

#### Describing a Single File or Folder

Descriptive metadata is used to annotate a file, folder or group of
files in a folder structure. All descriptive metadata in Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> is
indexed and searchable [(*see search*)](#search-and-access). Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> provides both the
Dublin Core simple 15 element schema which you can read about in detail
(if you want to) <a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-3">here</a>
and the full General International Standard Archival Description ISAD(G)
descriptive metadata schema which you can read more about <a href="https://www.ica.org/en/isadg-general-international-standard-archival-description-second-edition">here</a> 

You can be as precise as you wish with the use of metadata elements by
following the specifications and controlled vocabularies. Alternatively,
you can just use those elements you wish, in the way that suits you,
(for example by putting a title in for each file). Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> does not
impose rules.

To begin to describe any file or folder in Curate, select the object you
would like to describe. On the right hand side of your screen, in the
object information area, you will see the file metadata panel. ([*see object information area*](#object-information-area) , and [*metadata panel*](#metadata-panel)).

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image25.png" style=""></img>
</div>

Next, click the dropdown for your chosen
record schema. Curate features simple DC and ISAD(G) out of the box, but
can easily support most any other standardized schema.

Enter the metadata for each field you would like to modify, and you will
then see the "save" button appear at the bottom of the panel.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image26.png" style=""></img>
</div>

Note that the save button will appear as
soon as any changes are made to the selected files descriptive metadata.
If you select another file before saving or without reverting your
changes, the changes will move to the next selected file and await you
to "save" again.

#### Batch Describing Files and Folders

To describe multiple files and or folders at once, first select all the
objects you would like to create or modify descriptive records for.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image27.png" style=""></img>
</div>

In the object information area, you will see only the file actions panel
[(*see file actions panel*)](#file-actions-panel) which will contain options to download the
multiple selection of objects, or "meta data" to modify the descriptive
records of all the files.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image28.png" style=""></img>
</div>

You can also right click any of the
objects in your selection, and you will see the "meta data" option in
the context menu.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image29.png" style=""></img>
</div>

You will then be prompted to select the
fields that you would like to modify.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image30.png" style=""></img>
</div>

As you tick each field you would like to
modify, a text area will appear in which to enter your new data.

Once you've modified all your chosen fields, click "ok" and all the
files in your selection will be updated.

### Creating a Report on File Types

Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> identifies file types via a MIME type and a PRONOM ID. You
can generate detailed reports of the MIME types, for example to create a
digital asset register, for any aggregation of files or folders. Try
going to a high-level folder that contains other folders and files,
click New and select 'Generate MIME type Report'. A popup will appear
with a pie chart showing the filetypes in your selection. You can float
over the chart to see the numbers. You can also download the MIME type
report as a CSV file.

<div class="main-content-img-container">
    <img src="/curate-documentation/vertopal_205d29a8e99241c0a1d0e3064ad58f44/media/image31.png" style=""></img>
</div>

### Creating a Transfer Package or SIP

Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> can create packages or SIPs for submission to repositories or
digital preservation platforms such as: Archivematica, Preservica and
EARK compliant systems using the templates in the Package Templates
workspace. We can give you a demonstration of package creation if you
are interested, just send us a message via the support channel.

## Preservation

Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> features a highly automated digital preservation service that
wraps the open source tool A3M into a dynamic workflow. Curate preservation workflows are highly configurable, simple to action, 
and automate the process of performing best-practice preservation and packaging actions on your files and folders. 

Here's the enriched version with proper markdown formatting and escaping:

### About A3M

A3M is an open-source tool, developed by the sensational Artefactual Systems <span style="font-size: 8pt;vertical-align: super;">TM</span>, that distills the essential preservation and packaging functionality of their widely-used platform Archivematica <span style="font-size: 8pt;vertical-align: super;">TM</span> into a specialised module. By removing unneeded components like the backend storage management and frontend-application while maintaining the same core code that has powered digital archiving programs across the globe, A3M is able to provide reliable, comprehensive preservation and packaging functionalities in entirely new contexts.

<a href="https://a3m.readthedocs.io/en/latest/">Read the A3M documentation</a>

<a href="https://github.com/artefactual-labs/a3m">Explore the A3M GitHub repository</a>

<span style="font-size: 8pt;">A3M and Archivematica are trademarks of <a href="https://www.artefactual.com/">Artefactual Systems Inc.</a></span>

#### A3M Benefits

Some key benefits of using A3M for digital preservation include:

 - Standards compliance: A3M fully supports the OAIS reference model, creates valid and well formed METS documents, and produces AIPs that conform to the BagIt specification.
 - Comprehensive format support: A3M's default Format Policy Registry (FPR) covers a wide range of file formats, from common office documents to complex multimedia files.
 - Extensibility: A3M's modular design makes it easy to add support for new formats, tools, and workflows as needs evolve.
 - Community-driven development: As an open-source project, A3M benefits from the contributions and expertise of a diverse community of users and developers.

<span style="font-size: 8pt;">A3M and Archivematica are trademarks of <a href="https://www.artefactual.com/">Artefactual Systems Inc.</a></span>

#### The Format Policy Registry (FPR)

At the heart of A3M's preservation workflow is the Format Policy Registry (FPR). The FPR is a centralised knowledge base that contains information about file formats and the optimal tools and strategies used to perform preservation and access normalisation on them.

The FPR consists of three main components:

 - Format database: A comprehensive registry of file formats.
 - Tool database: A curated collection of open tools used for normalisation.
 - Policy rules: A set of customisable rules that map specific file formats to their recommended normalisation actions.

 <span style="font-size: 8pt;">A3M and Archivematica are trademarks of <a href="https://www.artefactual.com/">Artefactual Systems Inc.</a></span>

<div class="tip"> <span class="mdi mdi-information-outline"></span> <span>The default FPR in Curate encapsulates a broad variety of migration pathways across several tools, offering wide coverage for file formats and applying extensively production-tested methodologies. It is the same as you would find in a standard installation of Archivematica.</span> </div>

By leveraging the collective knowledge and best practices encoded in the FPR, A3M is able to make informed, standards-based decisions about how to best preserve your digital content for the long term.

##### Customising the FPR
While the default FPR in Curate provides excellent coverage for a wide range of common file formats, we recognize that every institution has unique needs and priorities when it comes to digital preservation. That's why we've made it easy to customize the FPR to better align with your specific requirements.

Whether you need to add support for niche or proprietary formats, fine-tune the normalisation rules for certain content types, or integrate new preservation tools into your workflow, the FPR in Curate can be fully tailored. 

If you are an existing Archivematica user migrating to Curate, we can even use your existing customised FPR as a drop-in, ensuring a smooth transition and continuity of your preservation practices (provided your Archivematica installation is reasonably up-to-date).

To discuss customising the FPR for your Curate instance, please contact our support team. We'll work with you to understand your unique requirements and implement the necessary changes to your A3M FPR.

By combining the robustness and reliability of A3M with the flexibility and extensibility of the Curate platform, Curate enables you to implement a best-in-class digital preservation solution in an intuitive and reliable wrapper.

### Preservation Configs

The preservation workflow in Curate is highly customisable. You can choose to enable, disable or modify various parameters related to the handling of
your content:

* *Config Name:* The reference name given to your custom config, as it will appear in your list of available preservation configs when preserving an item. You should make your config names unique.

* *Config Description:* A brief description of your customised config to let you or your colleagues know what it's purpose is. 

* *Normalise Objects:*  Enable or disable the normalisation process for objects in your preservation selection

* *Image Normalisation Format:* Select your preferred format for image normalisation.

* *AIP Packaging Type:* Select the output packaging format of your workflow AIPs.
    * *standard:* Standard bagit AIP packaging 
    * *EARK:* Package AIPs in line with the EARK specifications. <a href="https://eark.online/">Read more about EARK here.</a>

* *Compress AIPs:* Whether to apply a compression algorithm to your output AIP object. 
    * *Compression Algorithm:* Compression algorithm to apply to AIPs.
    * *Compression Level:* Level of compression to apply to AIPs.

* *Generate Transfer Structure Report:* Generate a report about your incoming objects before preservation actions are applied to them

* *Document Empty Directories:* Create an entry in the AIP METS Structmap for empty directories within your preservation selection before they are deleted.

* *Extract Packages:* Any package objects (like .zip files) within your preservation selection will be extracted to a folder before your content is preserved.

    * *Delete Packages After Extraction:* The original package object referenced above will be deleted once its contents has been extracted, otherwise the original package object is preserved along with its extracted contents

<div class="warning"><span class="mdi mdi-alert"></span><span>Enabling compression for your AIPs will save a small amount of storage in your Archive workspace, depending on the selected algorithm and level, but it will also prevent Curate from being able to index their contents. This means you will not be able to search for files inside of your AIPs. As a result, we strongly recommend leaving AIP compression disabled.</span></div>

The system comes packaged with a default preservation config which is enacted when you choose the standard "Preserve" option in the UI [(*see preserving files and folders*)](#preserving-files-and-folders)
, and should be appropriate for most use-cases. If you would like to create a customised configuration that modifies any of the parameters described above, Curate provides an intuitive interface for customising, saving and editing your own preservation configs.

#### Creating a config

To create a new preservation config, first select the main user dropdown in the top left-hand corner of the Curate interface by clicking this icon: <div size="38" style="color: rgb(255, 255, 255); background-color: rgb(0, 102, 138); user-select: none; display: inline-flex; align-items: center; justify-content: center; font-size: 19px; border-radius: 50%; height: 38px; width: 38px;"><span class="mdi mdi-account" color="#ffffff" style="display: flex;align-content: center;color: rgb(255, 255, 255); position: relative; font-size: 22.8px; display: inline-block; user-select: none; transition: all 450ms cubic-bezier(0.23, 1, 0.32, 1) 0ms; width: 22.8px; height: 22.8px; margin: 7.6px;"></span></div>

From the dropdown, select "Preservation Configs" to open the configs menu.
<div class="main-content-image-container">
    <img src="/curate-documentation/assets/Preservation Configs Menu.png"></img>
</div>

On the left hand side of the menu, you will find all the controls for creating new configs or editing existing ones. On the right, you will find a list of all of your saved configs. [(*see modifying configs*)](#modifying-a-config)

To create a config, simply customise your desired parameters in the left hand area and then give your new config a name in the "details" box. Once you have entered a name, you will see the "Save config" button appear. Once you've hit "save", your configs will be reloaded and you will see your new config slide into the list of saved configs on the right.

#### Modifying a config

To modify your saved configs, navigate to the preservation configs menu, locate your saved config in the "Saved configs" area on the right of the menu, hover over and click your config to load it into the
working area on the left of the preservation configs menu.

Once the details of your saved config have loaded, you may begin to modify it's parameters and you will notice the "Save" button appear. Click the "save" button to write your new changes into the saved config.

<div class="tip"><span class="mdi mdi-information-outline"></span><span>You'll notice each of your saved configs has a star icon to the left of its information in the saved configs area. You can click on this icon to favourite any of your saved configs. When you go to launch a preservation workflow on some content, your favourite configs will be shown in the main context menu, rather than appearing in the custom configs drop-down. 
</span></div>


### Preserving Files and Folders

Initiating digital preservation on any of your content in Curate is incredibly straightforward. Whether you want to preserve a single file, a folder, or multiple files and folders, the process is the same. Simply navigate to the content you'd like to preserve in your Appraisal workspace [(see Appraisal Space)](#appraisal-space), select it, right-click, and choose "Preserve".

<div class="tip"> <span class="mdi mdi-information-outline"></span> <span>You can only launch preservation workflows from the Appraisal space. This ensures that your content has been properly characterised and evaluated before being preserved.</span> </div>

Choosing "Preserve" will launch the default preservation config on your selection. You will receive a confirmation message indicating that your request was received and that Curate will now handle the rest of the preservation process.

As Curate begins to execute the various steps in the preservation workflow, you will see status updates appear as tags on your selected content. These tags allow you to easily track the progress of the preservation process. Once Curate has finished processing your selection, a final "Preserved" tag will be applied to indicate the successful completion of the workflow.

### Using Custom Preservation Configs

In addition to the default preservation config, Curate allows you to create and use custom configs that define specific preservation parameters (see Creating Configs). To initiate a custom config on your selection:

 1. Right-click your selected content
 2. Choose "Preservation Configs" from the context menu
 3. Select your desired config from the list of custom configs to initiate the preservation workflow with the chosen config
 4. The rest of the process is identical to using the default config. Curate will execute the preservation workflow according to the parameters specified in your custom config.


### The Core Preservation Process
Under the hood, Curate leverages the power of A3M [(*see about A3M*)](#about-a3m)to perform the key preservation actions in its workflow. These actions ensure the long-term accessibility and integrity of your digital content.


#### Characterisation

A3M uses a set of specialised tools to analyze your files and extract detailed technical metadata about their format, structure, and properties. This metadata is crucial for informed preservation planning and decision-making. The extracted metadata is stored in the AIP's METS file, providing a complete technical description of the preserved content.

##### Characterisation Tools
A3M utilizes the following industry-standard tools for file characterization:

<a href="http://ffmpeg.org/">FFProbe</a>: A powerful multimedia stream analyzer that provides detailed information about audio and video files
<a href="http://mediaarea.net/en/MediaInfo">MediaInfo</a>: A versatile tool that extracts technical and tag data from video and audio files
<a href="https://exiftool.org/index.html">ExifTool</a>: A comprehensive metadata extraction tool that supports a wide range of file formats
<a href="https://forensicswiki.xyz/wiki/index.php?title=Fiwalk">Fiwalk</a>: A command-line tool for analyzing and extracting metadata from disk images and file systems

#### Normalisation

Normalisation is the process of converting files to standardized, preservation-friendly formats that are more likely to remain accessible over the long term.

A3M determines the appropriate target format for each file based on the Format Policy Registry (FPR) [(*see the FPR section for more*)](#the-format-policy-registry-fpr), a comprehensive knowledge base that maps file formats to recommended preservation actions. By consistently applying these normalisation rules, Curate helps ensure the future renderability and usability of your content.

##### Normalisation Tools

Depending on the type of content being preserved, A3M employs different tools for normalisation:

*Image Files*

 * <a href="https://imagemagick.org/script/convert.php">Imagemagick Convert</a>
 * <a href="https://inkscape.org/">Inkscape</a>

*Audio-Visual Files*

 * <a href="https://www.ffmpeg.org/">FFmpeg</a>

*Document Files*

 * <a href="https://www.ghostscript.com/">Ghostscript</a>
 * <a href="https://www.ps2pdf.com/">Ps2pdf</a>

#### Validation

The final step in the core preservation process is validation. A3M performs a series of checks to ensure the integrity and completeness of your preserved content. This includes verifying checksums to detect any data corruption, as well as validating file formats to ensure compliance with preservation standards.

Validation provides an added layer of assurance that your content has been accurately preserved and will remain accessible over time. Any issues detected during validation can be caught for review and remediation.

By combining robust characterisation, normalisation, and validation, Curate's A3M-powered workflow ensures the highest levels of digital preservation for your valuable content. The end result is a standards-based, fully-described Archival Information Package (AIP) that can be confidently stored and managed for the long term.

## Packaging
Curate integrates a powerful and flexible AIP (Archival Information Package) packaging system that allows it to output your archival objects in a variety of standardized structures. This ensures that your preserved content is stored in a well-documented, sustainable format that can be easily understood and accessed in the future.

### Supported Packaging Formats
By default, Curate uses the widely-adopted BagIt specification for packaging AIPs. BagIt is a hierarchical file packaging format designed to support disk-based storage and network transfer of arbitrary digital content. It provides a set of conventions for packaging content along with its metadata in a way that facilitates easy validation and long-term preservation.

In addition to BagIt, Curate also supports the E-ARK (European Archival Records and Knowledge Preservation) packaging format out of the box. E-ARK is a set of specifications that aim to provide a common European methodology for packaging digital archival records. It defines a set of information package formats (SIP, AIP, DIP) and guidelines for their creation, management and reuse.

<div class="tip"> <span class="mdi mdi-information-outline"></span> <span>Curate's packaging system is highly extensible. If your organization requires support for a specific packaging format not currently available, please get in touch with us. We can work with you to implement custom packaging formats to meet your specific needs.</span> </div>

### Configuring Packaging Options
Curate allows you to customize various aspects of the packaging process through preservation configs. You can specify parameters such as the packaging format (e.g., BagIt or E-ARK), compression options, and whether to include additional metadata or reports in the package. [See the preservation configs section](#preservation-configs) for more details on how to create and manage preservation configs.

### The Packaging Workflow
The packaging process in Curate is fully integrated with the preservation workflow. Once the core preservation actions (characterisation, normalisation, validation) have completed successfully [(see preservation)](#preservation), Curate automatically packages the resultant archival objects according to the specified packaging format and options.

The generated AIP packages are then stored in your Archival workspace [(see archive workspace)](#archive-space), where they can be easily located, searched and retrieved as needed. Each AIP includes the preserved content along with comprehensive metadata (descriptive, administrative, structural, preservation) to ensure its long-term understandability and usability.

<div class="tip"> <span class="mdi mdi-information-outline"></span> <span>The AIPs generated by Curate are fully self-describing and self-contained. This means they include all the information necessary to understand and render the content, without relying on any external systems or documentation.</span> </div>
To learn more about the BagIt and E-ARK specifications and how they support long-term digital preservation, check out these resources:

<a href="https://www.ietf.org/rfc/rfc8493.txt">Read more about the BagIt specification here</a>

<a href="https://eark.online">Read more about E-ARK here</a>

## Miscellaneous

### Bookmarking a File or Folder

Any file or folder can be bookmarked by selecting and choosing the
option in the right mouse click or More menus. Bookmarked files and
folders appear in the Bookmark listing which you can access via the Star
icon at the top of the left-hand column. The Bookmark listing gives you
quick access to files you may be working with.

The option to make a 'New Folder from Bookmarks' is a feature that
allows you to copy an existing folder which has been bookmarked. Using this you can
create templates for commonly used folder structures, including the files within them, and replicate them by creating a new folder from
the bookmark.

### File Locking

You can choose to lock any file or folder in Curate to prevent
modification by any other user.

For files, this will prevent direct modification of the files content.
For folders, it will prevent any modification to the contents of the
folder itself.

This option does not prevent modification to the metadata of the locked
object.

Locked files will have a icon in the file list to indicate that they are
locked.

### Compress

Any file or folder can be compressed from the right click or More menus.
Options are given for Zip, Tar or Tar.gz packages and the compressed
object is added as an additional item in the same folder.

## Search and Access

### Sharing a file or folder

You can create a public or secure, private link for any file or folder
in your account. When clocking the link, guest users can view, download,
view metadata and even upload content. Start by selecting your content, and then selecting "share" either from the right click context-menu, or from the top main options bar in the file-list.

### Searching for Files

You can do simple searches across all of Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> using the search box
at the top right of the screen. The simple search is conducted over file
names and folder names only (not metadata). Complete names or fragments
of filenames can be used, for example a file called myphotograph.jpg can
be found searching on: myphotograph.jpg, myphotograph, my, photograph or
even photo.

If you click in the simple search box you will see a filter icon to the
right, which opens the Advanced Search dialogue. Within this area you
can specifically search in filename, in any of the descriptive metadata
fields and basic file properties. Within the Advanced Search you can
also use the wildcard \* character to enter partial terms, such as
myphoto\*.

menu. You will get a new popup box and can select Enable Public Share
form here. You will now see a url that has been created and is unique
for your share. You can copy this using the Copy icon and you can send
it to anyone you wish. Other options in the Shares popup are:

-   You can send the link to another use in your group using the Send
    Invitation button

-   You can customise the last 12 digits of the link to be anything you
    want and so can make the link meaningful

-   Disable link

-   Change permissions:

    -   For files, by default invited users can download and preview
        content, but you can disable either of these options.

    -   For folders, an option is added to give permission to upload
        files into your folder

-   Access Restrictions: you can add a password and password expiry date
    to the link to make it private

-   Link Label: when the object is viewed from the link it will have a
    label on the top of the page, this is normally the file or folder
    name, but you can customise it here together with the link
    description which is normally the created date and the presentation
    of the link contents. By default the user is presented with a
    preview of the file (if enabled) or a big download button (if
    preview is disabled), but you can make the download button the
    default.

-   \[Advanced Visibility\]: by default the link can only be edited by
    you, but if you enable this option you can allow other users within
    your group to edit the link.

All of your shares can be viewed and edited by selecting the My Shares
option in the menu under your username.

# Support

If you need help, click the pull-down menu at the top left of the
window, which should be labelled with a truncated version of your user
ID and select Support. This will take you to a contact form which goes
directly to the Penwern support team.

## Integrations

### Microsoft Sharepoint

Curate's Sharepoint integration provides a robust and user-friendly solution for organisations to safeguard their valuable digital content stored in Microsoft 365 environments. This integration seamlessly connects Sharepoint with Curate, enabling efficient management and long-term protection of records directly from within Sharepoint. 

This documentation will guide you through setting up the integration between Curate and Sharepoint, and also using the feature.

NB: Curate Sharepoint is an additional feature available to Curate Enterprise customers. If you have not yet added Sharepoint integration to your Curate Enterprise contract and you would like to explore your options, please get in touch with us.

<div class="tip">
    <span class="mdi mdi-information-outline"></span>
    <span>
        <strong>Things you'll need:</strong>
        </br>
        <ul>
            <li>Administrative access to your organisations Sharepoint admin centre, or help from someone who does.</li>
            <li>Permission to create an API key for Curate in your Sharepoint admin centre that confers read access to Document Libraries in which you would like the Curate integration to be available.</li>
            <li>Permission to upload and deploy Sharepoint extensions to your organisations Sharepoint environment.</li>
            <li>An account on your organisations Curate Enterprise system with a user-admin tier role.</li>
            <li>15-20 minutes of time.</li>
        </ul>
    </span>
</div>

#### Security Setup

To connect your Sharepoint system to Curate, you will first need to give both Curate and Sharepoint sufficient permissions to interract with eachother securely. 

**Explanation**

Both Curate and Sharepoint are highly secure platforms protected by comprehensive access protocols that require explicit and controlled access in order to allow users, or in this case eachother, to perform useful actions amongst themselves. 

In order to facilitate a seamless user-experience, the Curate Sharepoint integration leverages the Microsoft Graph API, which enables your Curate system to programatically access data stored in Microsoft services like Sharepoint. When you preserve a file with Curate from Sharepoint, you actually just tell Curate which files you would like to preserve, rather than supplying it the files directly. Curate then uses it's access to your content via the Graph API to directly stream the specified files.

Not only does this make the Preserve action *instant*, no matter the size of your file selection, but it also means data movement is kept to a minimum, performance is improved, and the stability and robustness of your local connection is irrelevent. Uploads of any size are managed completely automatically with no requirement for your device to remain connected to a network, or for you to monitor its progress.

As a result, to access and retrieve your specified data, Curate requires specific permissions to use your Sharepoint data. Similarly, Sharepoint requires specific permissions from Curate in order for Curate to allow your requests to be authenticated and actioned securely.

All traffic between Curate and a properly configuree Sharepoint environment is implicitly encrypted in transit by the HTTPS protocol, and your data never leaves a secure stream set directly between your Curate and Sharepoint systems, which are both highly protected platforms with thorough authentication systems. 

Ultimately, this solution is much more secure, robust and frictionless than the alternative of downloading content to your, potentially risky, local client and sending the data to Curate thereafter. 

#### Generating a Curate API Key

First, lets generate a Curate API key which will be supplied to Sharepoint in order for your Curate system to authenticate requests coming in from your Sharepoint environment. 

<div class="warning"><span class="mdi mdi-alert"></span><span>You should only generate an API key for any system if you understand what you are doing and the potential risks. If you are unsure and would like some advice, please get in touch with us. You should follow common best-practice guidance for storing, securing and retaining your API keys.</span></div>

To generate a Curate API key:

- log in to a Curate account with at least a user-admin tier role for your organisation.
- Open the user account menu by clicking your account profile icon in the top left hand corner of the Curate interface (it's the same menu you log-out from).

<div class="main-content-img-container">
    <img src="/curate-documentation/assets/user-account-menu.png" style=""></img>
</div>

- Select the "API Keys <span class="mdi mdi-chip menu-icons" style="color: rgb(117, 117, 117);font-size: 16px;user-select: none;"></span>" button to open the API keys menu.

<div class="main-content-img-container">
    <img src="/curate-documentation/assets/api-keys-menu.png" style=""></img>
</div>

# Roadmap and Suggestions

Curate is an incredibly dynamic and flexible platform on which it is easy for us
to add exciting functionality over time. We have a lot of ideas already, and we will 
publish a public roadmap in the future, but we would also really like to know
your needs for new functions that we can prioritise. 

Please drop us a line if you have any suggestions for the future of the platform,
and also indicate if we can contact you in case we have questions.

Check out our website for exciting updates on the latest features coming to
Curate.
