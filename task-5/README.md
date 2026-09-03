
#  DOCUMENTATION & TEST REPORT: Task_5_Currency_Converter/README.md
# ==============================================================================

# Task 5: Currency Converter

**Intern Name:** Piyush Upadhyay  
**Reference ID:** SKS/A2/C149158  
**Domain:** Python Development  
**Organization:** Saiket Systems  

---

## Overview

Task 5 entails building a real-time currency conversion tool in Python. The program integrates with a public REST API to retrieve live foreign exchange rates, accepts source and target currency inputs alongside amount values, and calculates the exact converted amounts while managing network and input exceptions gracefully.

---

## Technical Features

* **REST API Integration:** Connects to standard public exchange endpoints via the `requests` library to fetch current exchange rate maps in JSON format[cite: 1].
* **OOP Design:** Encapsulates rate storage, network fetching, and arithmetic conversion logic inside the `CurrencyConverter` class.
* **Input Validation:** Prevents application crashes from non-numeric amounts, negative figures, and unlisted currency symbols[cite: 1].
* **Continuous Conversion Loop:** Allows users to perform multiple conversions in a single session without repeated API handshakes.

---

## Example Test Run & Validation

### Sample Input
* **Base Currency:** `USD`
* **Target Currency:** `INR`
* **Amount:** `100`

### Console Output
```text
Fetching live exchange rates for base currency: USD...
Exchange rates successfully loaded!

------------------------------------------
Enter target currency code (e.g., INR, EUR, GBP) or 'exit' to quit: INR
Enter amount in USD: 100

>>> 100.00 USD = 8,350.50 INR (Exchange Rate: 1 USD = 83.5050 INR)
done ..