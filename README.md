# FileCleanerPro

**FileCleanerPro** is a Python and PyQt6-based **file cleaner and archiver GUI application**.  
It allows users to easily delete or archive unnecessary or old files in selected folders.

---

## Features

- Scan folders for files
- Filter by file extensions (e.g., .txt, .log, .tmp)
- Delete selected files
- Archive selected files (in zip format)
- User-friendly GUI
- Display the number of selected files in the list

---

## Requirements

- Python 3.13 or higher
- PyQt6 library

To install PyQt6:
```bash
pip install PyQt6
Usage
Clone or download the project to your computer.

Open the terminal or use GitHub Desktop to navigate to the project folder.

Run the main.py file with Python:

bash
Kodu kopyala
python main.py
GUI will open:

Click Scan Files to select and scan a folder.

Select files from the list.

Use Delete Selected or Archive Selected buttons to perform actions.

Folder Structure
css
Kodu kopyala
FileCleanerPro/
│
├─ main.py
├─ cleaner/
│   ├─ file_scanner.py
│   └─ file_manager.py
└─ README.md
Future Improvements
Filter by file size or modification date

Scheduled automatic cleaning

Advanced log and reporting

Support for RAR archiving
