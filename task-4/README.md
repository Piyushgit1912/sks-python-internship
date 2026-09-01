
# ==============================================================================
# 2. DOCUMENTATION & TEST REPORT: Task_4_Web_Scraper/README.md
# ==============================================================================

# Task 4: Basic Web Scraper

**Intern Name:** Piyush Upadhyay  
**Reference ID:** SKS/A2/C149158  
**Domain:** Python Development  
**Organization:** Saiket Systems  

---

## Overview

Task 4 involves designing a web scraper that extracts live web data (such as articles, quotes, or news headlines) using Python's `requests` and `BeautifulSoup` libraries[cite: 1]. The extracted content is structured and formatted for terminal display, as well as saved to external JSON and CSV files[cite: 1].

---

## Technical Features

* **HTTP Client:** Uses `requests` configured with custom User-Agent headers to ensure reliable page retrieval.
* **HTML Parsing & Traversal:** Uses `BeautifulSoup` (`html.parser`) to parse DOM nodes, extract text, and clean whitespace.
* **Dual Exporters:** Includes built-in methods to save structured results into standard `.json` and `.csv` files.
* **Network & HTTP Error Handling:** Safely manages bad URLs, network timeouts, unreachable domains, and standard HTTP error codes (`404`, `500`).

---

## Example Test Run & Validation

### Target URL
`https://quotes.toscrape.com`

### Sample Output in Terminal
```text
Fetching and parsing: [https://quotes.toscrape.com](https://quotes.toscrape.com)...

--- Extracted 10 Items ---
[1] “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
     Source/Author: Albert Einstein

[2] “It is our choices, Harry, that show what we truly are, far more than our abilities.”
     Source/Author: J.K. Rowling

Data successfully exported to JSON: scraped_data.json
Data successfully exported to CSV: scraped_data.csv