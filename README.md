# YouTube Transcription Utility

This application is a web-based utility built with Flask that processes YouTube video transcripts and generates a table that can be copied and pasted into a OneNote document.

## Features

- Accepts a YouTube URL as input.
- Fetches the transcript of the video using the `youtube-transcript-api`.
- Displays the transcript in a table format with two columns: **Start** and **Text**.
- Provides a "Copy Table to Clipboard" button for easy copying of the table into OneNote or other applications.

## How It Works

1. Enter a YouTube URL in the input field.
2. Click the **Fetch** button to retrieve the transcript.
3. If a transcript is available, it will be displayed in a table.
4. Use the **Copy Table to Clipboard** button to copy the table for pasting into OneNote.

## Technologies Used

- **Flask**: Backend framework for handling routes and rendering templates.
- **HTML/CSS**: For the frontend design and layout.
- **JavaScript**: For clipboard functionality.
- **youtube-transcript-api**: To fetch YouTube video transcripts.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git

## Remaining Tasks
- The table section should hide when there is no transcript
- The application doesn't run correctly from the root and can't find utilities
- Rename row to item

