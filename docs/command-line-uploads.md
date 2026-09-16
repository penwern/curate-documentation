# Uploading with the Curate command-line client

The Curate command-line client (`cec`) is intended for large uploads or
workflows where the web uploader is not suitable. Use it only with the Curate
server, account and destination provided by Curate support.

This guide describes setup on Windows. If you use macOS or Linux, contact
Curate support for the correct client and installation instructions.

## Before you begin

You will need:

- the Windows command-line client supplied by Curate support;
- the URL of your Curate server;
- a Curate API key supplied by Curate support; and
- the exact destination workspace and folder for the upload.

The API key used by the command-line client is a Personal Access Token (PAT).
Treat it like a password: do not put it in documentation, email, screenshots,
support tickets or shell commands.

## Download the command-line client

Contact Curate support to request the command-line client. Support will provide
the appropriate version for your Curate system and, where applicable, a
checksum that you can use to verify the downloaded file.

Do not download a different version from an unofficial source or use the
client's update command. If Windows or your organisation's endpoint protection
blocks the client, contact your IT team and Curate support. Do not disable or
bypass organisational security controls.

Create a permanent folder for the client and place `cec.exe` inside it. For
example:

```text
C:\Users\<your-Windows-username>\CurateTools\CEC\cec.exe
```

Do not move `cec.exe` after adding its folder to `PATH`.

## Add CEC to your PATH

Adding the client folder to your user `PATH` lets you run `cec` from any
PowerShell window without typing its full location.

1. Open the Windows Start menu and search for **Environment Variables**.
2. Select **Edit environment variables for your account**.
3. Under **User variables**, select **Path**, then select **Edit**.
4. Select **New** and enter the folder containing `cec.exe`, for example:

   ```text
   C:\Users\<your-Windows-username>\CurateTools\CEC
   ```

5. Select **OK** to close each window.
6. Close any open PowerShell windows, then open a new PowerShell window.

Confirm that Windows can find the client:

```powershell
cec version
```

If PowerShell reports that `cec` is not recognised, confirm that the `PATH`
entry is the folder containing `cec.exe`, not the path to `cec.exe` itself.

## Request an API key

Contact Curate support to request an API key for command-line uploads. Tell
support:

- which Curate user or service account will perform the upload;
- which workspace and folder the account must access;
- whether access is required for a single upload or ongoing work; and
- the expected upload size and approximate number of files.

Support will provide the server URL, API key, permitted destination and any
expiry information. The key will only provide the permissions assigned to its
account and scope.

## Add the API key to CEC

First check that CEC can use the Windows credential store:

```powershell
cec config check-keyring
```

If this command fails, or CEC warns that credentials will be stored in clear
text, stop and contact your IT team or Curate support. Do not use
`--skip-keyring`.

Add the connection interactively:

```powershell
cec config add token
```

When prompted, enter:

1. the full Curate server URL supplied by support, including `https://`;
2. the API key; and
3. a memorable connection name, such as `Organisation-Production`.

Using the interactive command prevents the API key from being saved in your
PowerShell command history.

List the configured connections:

```powershell
cec config ls
```

If more than one connection is configured, select the required connection:

```powershell
cec config use "Organisation-Production"
```

Run `cec config ls` again and confirm that the correct connection is active.

## Test the connection

List the workspaces that the API key can access:

```powershell
cec ls
```

List the destination supplied by support:

```powershell
cec ls "workspace-name/path/to/destination"
```

Check that a destination exists:

```powershell
cec ls "workspace-name/path/to/destination" --exists
```

For `ls`, use a path such as `workspace-name/folder`. For uploads, add the
`cells://` prefix, for example `cells://workspace-name/folder/`.

Before starting a large upload, upload a small, non-sensitive test file to a
support-approved test destination:

```powershell
cec scp "C:\Uploads\cec-test.txt" "cells://workspace-name/test-destination/"
```

Confirm that the file arrived:

```powershell
cec ls "workspace-name/test-destination/cec-test.txt" --details
```

## Upload files and folders

Always quote local and remote paths, particularly when they contain spaces.
Use only the destination supplied by Curate support.

### Upload one file

```powershell
cec scp "C:\Uploads\delivery-001.zip" "cells://workspace-name/path/to/destination/"
```

### Upload a folder

CEC uploads folders recursively. The following command uploads the
`Delivery-001` folder and its contents into the destination:

```powershell
cec scp "C:\Uploads\Delivery-001" "cells://workspace-name/path/to/destination/"
```

The expected remote path is:

```text
workspace-name/path/to/destination/Delivery-001
```

Use a small test folder to confirm the resulting layout before starting a
large upload.

### Upload a large file or folder tree

For large uploads, use `--no-progress`. This avoids the continuously refreshed
terminal progress display while retaining CEC's multipart upload and retry
behaviour:

```powershell
cec scp --no-progress "C:\Uploads\Delivery-001" "cells://workspace-name/path/to/destination/"
```

The command may produce little output while it is working. Keep PowerShell
open, prevent the computer from sleeping and wait for the command to finish.

When the PowerShell prompt returns, display CEC's exit code:

```powershell
$LASTEXITCODE
```

An exit code of `0` indicates that CEC completed successfully. Any other value
indicates a failure.

## Verify an upload

List the uploaded folder:

```powershell
cec ls "workspace-name/path/to/destination/Delivery-001"
```

You can also verify that selected files exist:

```powershell
cec ls "workspace-name/path/to/destination/Delivery-001/subfolder/example.dat" --exists
```

For important or regulated transfers, follow your organisation's agreed
checksum or integrity-verification procedure after the upload.

## Important safety guidance

- Confirm the active connection and exact destination before every upload.
- Do not use `--force` unless Curate support explicitly instructs you to do so.
  Force mode can merge folders and replace existing files.
- Do not use `--skip-verify` to bypass a TLS or certificate error.
- Do not change multipart, concurrency or retry settings unless instructed by
  Curate support.
- A failed or interrupted upload can leave partial content at the destination.
  Do not assume that rerunning the command will resume from the point of
  interruption.
- Before retrying a failed upload, inspect the destination and contact support
  if you are unsure whether partial content should be removed or replaced.
- Never share the API key in a command, screenshot, log or support ticket.

## Troubleshooting

**`cec` is not recognised**

Close and reopen PowerShell. Confirm that the folder containing `cec.exe` is in
your user `PATH`.

**Authentication fails**

Run `cec config ls` and confirm that the intended connection is active. The API
key may have expired or been revoked; contact Curate support for assistance.

**The destination cannot be listed or written to**

Check the spelling of the workspace and folder. If the path is correct, contact
Curate support to confirm the API key's permissions.

**CEC reports that the destination already exists**

Do not add `--force` automatically. Confirm the existing content and the
required overwrite behaviour with Curate support.

**The upload was interrupted or returned a non-zero exit code**

Record the time, source, destination, exit code and displayed error message,
but do not include the API key. Check the remote destination before retrying
and contact Curate support if partial content is present.
