# FileShelf

A lightweight Python command-line utility that automatically sorts cluttered directories (such as a `Downloads` folder) by moving files into categorized subfolders based on their file extensions.

## Features

* **Automatic Categorization:** Sorts files into `Documents`, `Images`, `Spreadsheets`, `Text Files`, `Programs`, and `Others`.

* **Case-Insensitive Matching:** Handles both lowercase and uppercase file extensions (e.g., `.pdf` and `.PDF`).

* **Safe Duplicate Handling:** Prevents accidental overwrites by automatically renaming duplicate files (e.g., `report.pdf` becomes `report_1.pdf`).

* **Folder Reuse:** Reuses existing category folders without throwing errors.

* **Graceful Error Handling:** Skips locked, open, or permission-restricted files without crashing and reports them at the end.

* **Execution Summary:** Displays a clear breakdown of how many files were moved into each category.

## Supported File Categories

| Category | Supported Extensions | 
| ----- | ----- | 
| **Documents** | `.pdf`, `.doc`, `.docx`, `.ppt`, `.pptx`, `.odt`, `.rtf` | 
| **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp` | 
| **Spreadsheets** | `.xls`, `.xlsx`, `.csv`, `.ods` | 
| **Text Files** | `.txt`, `.md`, `.log` | 
| **Programs** | `.py`, `.js`, `.ts`, `.html`, `.css`, `.java`, `.c`, `.cpp`, `.sh` | 
| **Others** | Any file extension not listed above (e.g., `.zip`, `.exe`, `.mp4`) | 



## Usage

1. Save the Python script as `fileshelf.py`.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the program:

   ```
   python fileshelf.py
   
   ```

4. Enter the path to the folder you want to organise when prompted:

   ```
   Enter the folder path to organise: ~/Downloads
   
   ```

## Example Output

### Terminal Summary

```
Enter the folder path to organise: /Users/alex/Downloads

--- Organisation Summary ---
Documents      : 2
Images         : 2
Spreadsheets   : 1
Text Files     : 0
Programs       : 1
Others         : 1
----------------------------
Total files moved: 7

```

### Resulting Directory Structure

```
Downloads/
├── Documents/
│   ├── report.pdf
│   └── notes.docx
├── Images/
│   ├── photo.jpg
│   └── logo.png
├── Spreadsheets/
│   └── sales.xlsx
├── Programs/
│   └── script.py
└── Others/
    └── archive.zip

```