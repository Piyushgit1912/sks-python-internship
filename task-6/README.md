

# ==============================================================================
# 2. DOCUMENTATION & TEST REPORT: Task_6_Word_Count_Tool/README.md
# ==============================================================================

# Task 6: Word Count Tool

**Intern Name:** Piyush Upadhyay  
**Reference ID:** SKS/A2/C149158  
**Domain:** Python Development  
**Organization:** Saiket Systems  



"""
Task 6: Word Count and Frequency Analysis Tool
Features:
- Reads and parses text files to calculate line count, word count, and character count.
- Performs word frequency distribution analysis ignoring case and punctuation.
- Displays structured analysis summaries directly in the terminal[cite: 1].
- Generates and exports detailed analysis reports to a text file.
- Robust exception handling for missing files and encoding issues[cite: 1].
"""
---

## Overview

Task 6 requires developing a Python text analysis utility that reads an input text file, calculates key structural metrics (number of lines, words, and characters), and determines the frequency distribution of words to identify the most recurring terms[cite: 1].

---

## Technical Features

* **Text Parsing & Tokenization:** Uses regular expressions (`\b[a-zA-Z0-9_']+\b`) to extract clean words while stripping out punctuation and whitespace.
* **Frequency Mapping:** Utilizes Python's standard `collections.Counter` data structure to perform word frequency distributions and rank occurrences[cite: 1].
* **Report Generation:** Generates a structured analysis output presented in formatted tables both in the terminal and as an exportable `.txt` file[cite: 1].
* **Defensive File I/O:** Handles missing files (`FileNotFoundError`), permission restrictions, and fallback encodings (`utf-8` and `latin-1`)[cite: 1].

---

## Example Test Run & Validation

### Sample Input Corpus (`sample_corpus.txt`)
```text
Python is an interpreted, high-level programming language.
Python is designed for readability and simplicity.
With Python, developers can write clear and logical code.
Python makes data analysis simple and fast.