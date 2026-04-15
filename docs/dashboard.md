## The Dashboard

The dashboard is a dedicated reporting area that gives administrators a real-time view of their Curate <span style="font-size: 8pt;vertical-align: super;">TM</span> instance. From here you can see how many files are stored, how storage is distributed across workspaces, what has been uploaded or deleted, and a full log of user activity.

Access is restricted to users with administrator or SuperUser privileges. Other users will see an access-restricted message if they navigate to the dashboard.

<!-- SCREENSHOT: Full-page view of the Overview tab, showing all stat cards and charts -->


The dashboard is divided into six tabs, each covering a different reporting area:

- **Overview** — a summary of total files, storage and file type distribution across all workspaces
- **Ingestion** — upload activity over time and a log of individual upload events
- **Storage** — current storage usage broken down by workspace
- **Deletions** — items currently in recycle bins and a history of permanent deletions
- **Activity** — a full log of all user activity across workspaces
- **Formats** — a breakdown of detected file formats and MIME types

Three controls sit in the top-right corner of the tab bar: a **Workspace** filter, an **Export** button, and a **Refresh** button. These are described at the end of this page.

## Overview

The Overview tab provides a high-level snapshot of the current state of your Curate instance.

<!-- SCREENSHOT: The three stat cards at the top of the Overview tab — Total Files, Total Storage, Workspaces -->


Three stat cards show:

- **Total Files** — the number of files currently held across all workspaces
- **Total Storage** — the cumulative size of all stored files
- **Workspaces** — the number of active workspaces

Two charts are displayed side by side below the stat cards:

- **Files by Type** — a doughnut chart breaking down all files into broad categories (Documents, Spreadsheets, Presentations, Images, Audio, Video, Archives and PDF)
- **Storage by Workspace** — a horizontal bar chart showing how storage is distributed across each workspace

<!-- SCREENSHOT: The Files by Type doughnut chart and Storage by Workspace bar chart side by side -->


A third chart, **Files by Workspace**, shows the file count for each workspace as a horizontal bar chart.

<!-- SCREENSHOT: The Files by Workspace horizontal bar chart -->


## Ingestion

The Ingestion tab shows upload activity across your Curate instance.

<!-- SCREENSHOT: Top of the Ingestion tab showing the Total Uploads and This Month stat cards -->


Two stat cards show:

- **Total Uploads** — the number of upload events recorded over the last 12 months
- **This Month** — the number of uploads so far this month

Note that the stat cards and the chart include uploads of AIPs into the Archive workspace. Counts reflect individual file events, so uploading a folder of 50 files produces 50 upload events.

### Uploads Over Time

The **Uploads Over Time** line chart shows upload volume across a rolling period. Use the **Daily**, **Weekly** or **Monthly** buttons above the chart to adjust the time granularity.

<!-- SCREENSHOT: The Uploads Over Time line chart with the Daily/Weekly/Monthly granularity toggle buttons visible above it -->


### Recent Uploads

The **Recent Uploads** table lists individual upload events. For each upload you can see the file name, workspace, the user who uploaded it, the file size, and the date and time.

<!-- SCREENSHOT: The Recent Uploads table showing file name, workspace, user, size and date columns, with the date range filter and Hide AIP uploads toggle above it -->


The table is paginated at 25 records per page. Two optional filters sit above it:

- **Date range** — set a From and/or To date to narrow results to a specific period. Click **Clear dates** to remove the filter.
- **Hide AIP uploads** — this toggle is on by default. When active it excludes uploads into the Archive workspace from the table. AIP uploads still appear in the stat cards and chart regardless of this setting.

The workspace filter in the top bar also applies to this table when a workspace is selected.

## Storage

The Storage tab shows how storage is currently distributed across your workspaces.

<!-- SCREENSHOT: Top of the Storage tab showing the Total Storage, Workspaces, and Largest Workspace stat cards -->


Three stat cards show:

- **Total Storage** — cumulative storage across all workspaces
- **Workspaces** — the number of workspaces that contain at least one file
- **Largest Workspace** — the name of the largest workspace and its current size

Two charts are displayed side by side:

- **Storage by Workspace** — a horizontal bar chart showing each workspace's storage size
- **Storage Distribution** — a doughnut chart showing each workspace's share of total storage, with a percentage shown in the tooltip

<!-- SCREENSHOT: The Storage by Workspace bar chart and Storage Distribution doughnut chart side by side -->


### Workspace Breakdown

Below the charts, the **Workspace Breakdown** list shows each workspace with a proportional progress bar alongside its storage figure. Workspaces are ordered from largest to smallest.

<!-- SCREENSHOT: The Workspace Breakdown list showing each workspace with its proportional progress bar and storage figure -->


### Storage Over Time

If the optional storage reporting service is configured for your deployment, a **Storage Over Time** line chart will appear below the workspace breakdown. This chart tracks the growth of total storage over a historical period.

<!-- SCREENSHOT: The Storage Over Time line chart with the Bucket, Range and Total/Per datasource controls visible in the chart header -->


Three controls appear in the chart header:

- **Bucket** — group data points by Day, Week or Month
- **Range** — select the last 30 days, last 6 months, or last year
- **Total / Per datasource** — toggle between a single total storage line, or separate lines for each datasource

## Deletions

The Deletions tab covers items that have been soft-deleted (moved to a workspace recycle bin) and gives you the ability to act on them.

<!-- SCREENSHOT: Top of the Deletions tab showing the Soft-Deleted Items and Deleted Size stat cards -->


Two stat cards show:

- **Soft-Deleted Items** — the total number of items currently sitting in recycle bins across all workspaces
- **Deleted Size** — the combined size of those items; this represents storage that could be recovered

Two charts are displayed side by side:

- **Deleted Items by Workspace** — a horizontal bar chart showing how many soft-deleted items are in each workspace's recycle bin
- **Time in Recycle Bin** — a horizontal bar chart grouping items by how long they have been in the bin: less than 7 days, 7 to 30 days, 1 to 3 months, and more than 3 months

<!-- SCREENSHOT: The Deleted Items by Workspace bar chart and Time in Recycle Bin bar chart side by side -->


### Review Queue

The **Review Queue** lists every item currently in a recycle bin. If the workspace filter is applied, only items from that workspace are shown. The item count is displayed in a badge next to the section heading.

Each row in the queue shows:

- **Name** — the file or folder name, with its full path shown beneath
- **Type** — whether the item is a **File** or **Folder**
- **Workspace** — which workspace the item came from
- **Size**
- **In bin since** — when the item was moved to the recycle bin
- **Requested by** — the user who moved the item

<!-- SCREENSHOT: The Review Queue table showing rows with checkboxes, file name and path, type badge, workspace, size, date in bin and requested-by columns -->


Select one or more items using the checkboxes (or the header checkbox to select all), and an action bar will appear with two options:

- **Restore** — returns the selected items to their original workspace
- **Permanently Delete** — removes the items from storage entirely

Permanently deleting items is irreversible. When you click **Permanently Delete**, a confirmation bar replaces the action bar and asks you to confirm before proceeding.

<!-- SCREENSHOT: The action bar that appears when queue items are selected, showing the Restore and Permanently Delete buttons (ideally with the confirmation bar visible, triggered after clicking Permanently Delete) -->


If all recycle bins are empty, the queue shows an empty state message in place of the table.

### Deletion History

Below the review queue, the **Deletion History** table shows a log of permanent deletion events pulled from the audit log. Each entry shows the user who performed the deletion, the item affected, the workspace, and the date and time.

<!-- SCREENSHOT: The Deletion History table showing user, item, workspace, and date/time columns -->


## Activity

The Activity tab provides a log of all user activity across your Curate instance.

<!-- SCREENSHOT: Top of the Activity tab showing the Total Activities and This Month stat cards -->


Two stat cards show:

- **Total Activities** — the total number of activity events on record
- **This Month** — the number of events recorded so far this month

The activity types tracked are: **Upload**, **Create**, **Access**, **Delete**, **Move**, **Share** and **Share Modified**.

### Activity Charts

A granularity toggle lets you switch the time range of the charts between **Daily**, **Weekly** and **Monthly**.

Two charts are displayed side by side:

- **Activity Over Time** — a line chart showing the overall volume of all activity events
- **Activity by Type** — a doughnut chart showing the proportion of each activity type over the selected period

<!-- SCREENSHOT: The Activity Over Time line chart and Activity by Type doughnut chart side by side, with the Daily/Weekly/Monthly toggle above them -->


### Activity Log

Below the charts, the **Activity Log** table lists individual events. Each row shows the activity type, the user who performed it, the item affected, the workspace, and the date and time.

<!-- SCREENSHOT: The Activity Log table showing activity type, user, item, workspace and date/time columns, with the type filter dropdown visible above -->


The table is paginated at 25 records per page. Use the **type filter** dropdown above the table to narrow results to a specific activity type: All Types, Access, Create, Delete, Move, Upload, Share or Share Modified. The workspace filter in the top bar also applies here.

## Formats

The Formats tab provides a detailed breakdown of the file formats held in your Curate instance. It requires the optional format reporting service to be configured; if it has not been set up, a message will be shown explaining this.

A badge near the top of the tab shows the date and time of the most recent data snapshot that the format reporting service has processed.

<!-- SCREENSHOT: Top of the Formats tab showing the snapshot date badge and the four stat cards — Total Files, Total Size, Unique Formats, No-MIME Count -->


Four stat cards show:

- **Total Files** — total number of files counted across all formats
- **Total Size** — total storage across all detected formats
- **Unique Formats** — the number of distinct MIME types and file extensions detected in your content
- **No-MIME Count** — the number of files where format detection fell back to a file extension rather than a full MIME type identification

### Format Charts

Two panels are shown side by side:

- **Top Formats by File Count** — a doughnut chart showing the ten most common formats; all remaining formats are grouped under "Other"
- **All Formats** — a scrollable table listing every detected format with its MIME type or extension, category, file count, total size, and a proportional bar

<!-- SCREENSHOT: The Top Formats by File Count doughnut chart alongside the All Formats scrollable table, showing MIME type, category, file count, size and proportion bar columns -->


The category shown for each format is a broad grouping (Images, Documents, Video, etc.) derived from the MIME type or extension.

### Format Trends Over Time

The **Format Trends Over Time** line chart tracks how format usage has changed over time.

<!-- SCREENSHOT: The Format Trends Over Time line chart with the Metric, Range, By format/Per datasource, filter input and Top N controls visible in the chart header -->


Several controls appear in the chart header:

- **Metric** — switch between **File Count** and **Total Bytes**
- **Range** — view the last 30 days, last 6 months or last year
- **By format / Per datasource** — toggle whether each series represents a format or a datasource
- **Filter formats** — when in "By format" mode, type part of a MIME type or extension to filter the series shown in the chart
- **Top N** — when no filter is active, choose to show the Top 5, Top 10, Top 20 or all formats

## Workspace Filter

The workspace filter dropdown at the top right of the dashboard lets you narrow reporting on certain tabs to a single workspace. It applies to the **Ingestion**, **Deletions** and **Activity** tabs. On other tabs the dropdown is greyed out.

Select **All Workspaces** to remove the filter and show data across all workspaces.

## Exporting Data

Each tab has an **Export** button in the top-right corner. Clicking it opens a small dropdown showing the available export formats for that tab.

Most tabs offer:

- **CSV** — exports the primary log or table for that tab
- **Excel (.xlsx)** — exports all data for that tab across multiple sheets
- **JSON** — exports all data as a structured JSON file

On the Overview tab the button is labelled **Export Report** and produces a single file covering all tabs at once. The Excel export creates a multi-sheet workbook with one sheet per data set.

<!-- SCREENSHOT: The Export button dropdown open, showing the CSV, Excel (.xlsx) and JSON format options -->


Exported files are downloaded directly to your browser's default download location. Log exports are capped at 10,000 records. Filenames follow the pattern `curate-[tab]-[date].[extension]`.

## Refreshing the Data

The circular refresh button at the top right of the tab bar clears all cached dashboard data and reloads everything from scratch.

Dashboard data is cached in your browser session to reduce API load. The cache duration varies by data type: activity and deletion data is held for around 5 minutes, while workspace and storage statistics are cached for up to 30 minutes. Use the refresh button if you need to see the most current figures.
