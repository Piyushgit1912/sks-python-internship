# ==============================================================================
# 1. SOURCE CODE: Task_3_File_Handling/file_handler.py
# ==============================================================================

"""
Task 3: Basic File Handling Utility
Features:
- File reading, string find-and-replace, and writing back to file.
- Custom output file specification or in-place file replacement.
- Comprehensive exception handling (FileNotFoundError, PermissionError, UnicodeDecodeError, etc.).
"""

2. DOCUMENTATION & TEST REPORT: Task_3_File_Handling/README.md
# ==============================================================================

# Task 3: Basic File Handling

**Intern Name:** Piyush Upadhyay  
**Reference ID:** SKS/A2/C149158  
**Domain:** Python Development  
**Organization:** Saiket Systems  

---

## Overview

Task 3 requires building a Python program capable of reading content from a text file, executing text transformations (finding and replacing specific words), and saving the modified content back to storage while handling standard file I/O exceptions gracefully.

---

## Technical Features

* **Safe Context Management:** Implements `with open(...)` to ensure file streams close reliably after operations.
* **OOP Modularity:** Uses `TextFileProcessor` class for read and find-and-replace methods.
* **Exception Handling:** Catches `FileNotFoundError`, `PermissionError`, and invalid UTF-8 encoding exceptions.
* **Flexible Destination:** Supports both in-place replacement and exporting to a newly designated output file.

---

## Example Test Run & Validation

### Sample Input File (`sample_input.txt`)
```text
Python is a great programming language.
Python is simple, readable, and widely used for data analysis.
Learning Python is both fun and rewarding.