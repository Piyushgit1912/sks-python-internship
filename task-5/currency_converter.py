# ==============================================================================
# 1. SOURCE CODE: Task_5_Currency_Converter/currency_converter.py
# ==============================================================================

"""
Task 5: Currency Converter
Features:
- Real-time exchange rate fetching using public REST APIs (open.er-api.com / ExchangeRate API).
- Dynamic multi-currency conversion with precision formatting.
- Robust input handling for invalid amounts, unknown currency codes, and network failures.
"""

import requests


class CurrencyConverter:
    def __init__(self, base_currency: str = "USD"):
        self.base_currency = base_currency.upper()
        self.api_url = f"https://open.er-api.com/v6/latest/{self.base_currency}"
        self.rates = {}

    def fetch_rates(self) -> bool:
        """Fetches live exchange rates for the base currency via API."""
        try:
            response = requests.get(self.api_url, timeout=10)
            response.raise_for_status()
            data = response.json()

            if data.get("result") == "success":
                self.rates = data.get("rates", {})
                return True
            else:
                print(f"[API Error]: Unable to fetch rates for '{self.base_currency}'.")
                return False
        except requests.exceptions.RequestException as e:
            print(f"[Network Error]: Could not connect to exchange rate service: {e}")
            return False

    def convert(self, amount: float, target_currency: str) -> float:
        """Converts an amount from base currency to target currency."""
        target_currency = target_currency.upper()
        if not self.rates:
            raise RuntimeError("Exchange rates have not been loaded. Please fetch rates first.")
        if target_currency not in self.rates:
            raise KeyError(f"Unsupported currency symbol: '{target_currency}'.")
        
        rate = self.rates[target_currency]
        return amount * rate


def main():
    print("\n==========================================")
    print("      REAL-TIME CURRENCY CONVERTER        ")
    print("==========================================")

    base = input("Enter base currency (e.g., USD, INR, EUR) [Default: USD]: ").strip().upper()
    if not base:
        base = "USD"

    converter = CurrencyConverter(base)
    print(f"\nFetching live exchange rates for base currency: {base}...")

    if not converter.fetch_rates():
        print("Exiting due to network/API error.")
        return

    print("Exchange rates successfully loaded!")

    while True:
        print("\n------------------------------------------")
        target = input("Enter target currency code (e.g., INR, EUR, GBP) or 'exit' to quit: ").strip().upper()
        if target in ("EXIT", "QUIT", "Q"):
            print("\nThank you for using the Currency Converter. Goodbye!")
            break

        amount_str = input(f"Enter amount in {base}: ").strip()
        try:
            amount = float(amount_str)
            if amount < 0:
                print("[Input Error]: Amount cannot be negative.")
                continue
        except ValueError:
            print("[Input Error]: Please enter a valid numerical amount.")
            continue

        try:
            converted = converter.convert(amount, target)
            rate = converter.rates[target]
            print(f"\n>>> {amount:,.2f} {base} = {converted:,.2f} {target} (Exchange Rate: 1 {base} = {rate} {target})")
        except KeyError as err:
            print(f"[Error]: {err}")
        except Exception as err:
            print(f"[Unexpected Error]: {err}")


if __name__ == "__main__":
    main()

