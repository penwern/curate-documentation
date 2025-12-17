## Email Processing

Curate provides powerful tools for processing and viewing email archives, allowing you to preserve email communications alongside your other digital content. The email processing feature extracts individual messages and attachments from PST and MBOX archive files, making them accessible, searchable, and preservable within your Curate workspaces.

### Why Process Email Archives?

Email archives often contain critical organisational records, but they present unique preservation challenges when stored in monolithic PST or MBOX formats. By processing these archives through Curate, you can:

- **Extract and preserve attachments as individual files**: Rather than keeping attachments encoded within email messages, Curate extracts them as separate files. This allows you to perform preservation actions on each attachment independently, ensuring formats like PDFs, images, and office documents can be normalised and preserved according to best practices.

- **Enable comprehensive virus scanning**: When processed in workspaces with virus scanning enabled (such as Quarantine or Personal spaces), every extracted file undergoes individual scanning. This provides thorough protection that wouldn't be possible with a single archive file.

- **Maintain email context and relationships**: Curate preserves the original folder structure from PST files and automatically reconstructs email threads, ensuring that conversations and organisational context are retained.

- **Search and access individual messages**: Once processed, emails become individually searchable and viewable within Curate's email renderer, making it easier to find and review specific communications.

### Supported Formats

Curate can process the following email archive formats:

- **PST files** (Microsoft Outlook Personal Storage Files)
- **MBOX files** (Standard Unix mailbox format)

### Processing an Email Archive

To process an email archive:

1. **Upload your PST or MBOX file** (_see Upload and Ingest_)(#upload-and-ingest).

2. **Locate your archive file** in the file list and select it.

3. **Select the file** and choose "Process Email Archive" from the "more" menu in the toolbar.

4. A **processing modal will appear** showing the status of your processing job. The modal displays:
   - The source file path
   - Current processing status (Queued, Processing, Completed, or Failed)
   - The job ID for reference
   - Output paths once processing completes

5. **Minimise the modal if desired**. Processing can take considerable time depending on the size of your archive, but you can minimise the status window and continue working. The modal can be restored from the "Jobs Running" indicator at the bottom of the screen, which will display a badge while processing is active. The job will proceed even if you close the modal, your browser window, or the Curate application. You can continue working while the job is processing. If you close Curate or refresh the page, the modal will dissappear but the job will continue.

#### Processing Time Expectations

<div class="warning"><span class="mdi mdi-alert"></span><span>Processing large email archives can take significant time, particularly in workspaces with virus scanning enabled. As an example, a 1GB PST file containing 10,000 emails may take several hours to process, as each extracted email produces a file plus one each for its attachments, which must be individually uploaded and scanned.</span></div>

Processing time scales with:
- The total size of the archive file
- The number of individual emails
- The number and size of attachments
- Whether virus scanning is enabled in the destination workspace

If you're processing very large archives, you may wish to schedule this work during off-peak hours or contact support for guidance on optimising large processing jobs.

### Viewing Processed Email Archives

Once processing is complete, your email archive will be stored as a `.mbox` folder containing individual email files (`.eml` format), extracted attachments, and a `manifest.json` file that maintains the structure and relationships between emails.

#### Opening the Email Viewer

To view your processed emails:

1. **Locate the processed archive folder** in your workspace. It will have a `.mbox` extension and contain the processed content.

2. **Double-click the `.mbox` folder**. A modal will appear asking whether you want to "Open" or "Render" the archive:
   - **Open**: Browse the internal file structure of the processed archive, viewing individual `.eml` files and extracted attachments as regular files.
   - **Render**: Launch the email viewer interface to read and navigate your emails as they would appear in an email client.

3. **Select "Render"** to launch the email viewer.

#### Using the Email Viewer

The email viewer provides a familiar, email-client-style interface for reviewing your processed archive:

**Email List Panel**

The left panel displays all emails in your archive with:
- Subject lines
- Sender information
- Date and time sent
- Preview snippets of email content
- Attachment indicators
- Thread grouping (emails in the same conversation are grouped together)

For PST archives, you can filter emails by their original Outlook folder structure using the folder browser at the top of the list panel.

**Email Detail Panel**

Selecting an email from the list displays its full content in the right panel, including:
- Complete email headers (From, To, CC, Date, Subject)
- Full message body (HTML or plain text)
- Inline images and embedded content
- Attached files with download options
- Thread view (if the email is part of a conversation, all related messages are displayed together)

**Search and Navigation**

Use the search box at the top of the email list to quickly find specific messages by subject, sender, recipient, or content. The viewer also supports keyboard navigation and responsive design for different screen sizes.

### Viewing Individual Email Files

In addition to viewing processed archives, Curate can also render individual `.eml` files directly. If you receive a standalone `.eml` file (for example, as an export from another email system), simply:

1. Upload the `.eml` file to any workspace
2. Double-click the file to open the email viewer

The file will be rendered immediately without requiring archive processing, allowing you to quickly review individual email messages.

### Processing Structure and Preservation

When Curate processes an email archive, it creates a structured output that preserves all the information needed for long-term access:

**Individual Email Files**

Each email is extracted as a separate `.eml` file, preserving the complete message including headers, body, and metadata. These files use the standard RFC 822 email message format, ensuring they remain readable by any standards-compliant email tool.

**Extracted Attachments**

All attachments are extracted as individual files and stored alongside their parent emails. By extracting attachments separately, Curate enables you to:
- Perform format-specific preservation actions (such as normalising PDFs or images)
- Apply individual virus scanning to each attachment
- Search and index attachment content
- Create separate preservation plans for different file types

**Folder Structure (PST files)**

For PST archives, Curate preserves the original Outlook folder hierarchy. The `manifest.json` file records which folder each email belonged to, allowing the email viewer to recreate the original structure and filter emails by folder.

**Email Threading**

Curate automatically reconstructs email conversations by analysing message headers (Message-ID, In-Reply-To, and References fields). Related emails are linked together in threads, preserving the context of conversations.

**Manifest File**

The `manifest.json` file serves as the central index for the processed archive, containing:
- Metadata for every email (sender, recipients, subject, date, snippet)
- Paths to individual `.eml` files and their attachments
- Folder structure information (for PST files)
- Thread relationships between emails
- Technical metadata needed for rendering

This manifest enables the email viewer to efficiently load and display archive contents without parsing every individual `.eml` file.

### Troubleshooting

**Processing Fails or Takes Excessive Time**

If your processing job fails or seems to stall:
- Check that your archive file passed virus scanning and is not corrupted
- For very large archives (multiple gigabytes or tens of thousands of emails), processing time can extend to several hours
- If a job appears stuck for an extended period, you can retry processing by selecting the archive file and choosing "Process Archive" again
- For persistent issues with large archives, contact support for assistance

**Email Viewer Shows "Unable to load archive"**

This typically indicates an issue with the processed archive structure:
- Ensure the `.mbox` folder contains a valid `manifest.json` file
- Verify that the processing job completed successfully (check for "Completed" status in the processing modal)
- Try closing and reopening the email viewer
- If problems persist, you may need to reprocess the original archive file

**Attachments Won't Display**

If attachments are not loading correctly:
- Check that the attachment files exist in the processed archive structure
- Verify you have appropriate permissions to access the files in the workspace
- For very large attachments, download times may be extended depending on your connection

For any issues not covered here, please contact support with your job ID and archive details for assistance.