#!/usr/bin/env python3
"""
CLI Measures Converter
Author: Diego Domínguez
Updated: 2025‑06‑21

A simple currency and temperature converter with menu navigation.
"""

from typing import Callable


# ----------------------------------------------------------------------------
# Conversion Logic (pure functions, no I/O)
# ----------------------------------------------------------------------------

def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9

def convert_currency(amount: float, rate: float) -> float:
    return amount * rate

# ----------------------------------------------------------------------------
# Data Configuration
# ----------------------------------------------------------------------------

TEMPERATURE_CONVERSIONS: dict[int, tuple[str, Callable[[float], float]]] = {
    1: ("Celsius to Fahrenheit", celsius_to_fahrenheit),
    2: ("Fahrenheit to Celsius", fahrenheit_to_celsius),
}

CURRENCIES: dict[int, str] = {1: "EUR", 2: "USD", 3: "CNY"}
RATES: dict[str, dict[str, float]] = {
    "EUR": {"USD": 1.148, "CNY": 8.259},
    "USD": {"EUR": 0.871, "CNY": 7.189},
    "CNY": {"EUR": 0.121, "USD": 0.139},
}

# ----------------------------------------------------------------------------
# Reusable User Input Helpers
# ----------------------------------------------------------------------------

def input_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid number. Try again.")

def input_option(prompt: str, valid: list[int]) -> int:
    while True:
        value = input(prompt)
        if value.isdigit():
            num = int(value)
            if num in valid:
                return num
        print("❌ Invalid option. Try again.")

# ----------------------------------------------------------------------------
# Menus
# ----------------------------------------------------------------------------

def temperature_menu() -> None:
    print("\n--- Temperature Conversion ---")
    for key, (label, _) in TEMPERATURE_CONVERSIONS.items():
        print(f"{key}. {label}")
    print("0. Back")

    choice = input_option("Select an option: ", [0, *TEMPERATURE_CONVERSIONS.keys()])
    if choice == 0:
        return

    label, func = TEMPERATURE_CONVERSIONS[choice]
    value = input_number("Enter the temperature to convert: ")
    result = func(value)

    unit = "F°" if "Fahrenheit" in label else "C°"
    print(f"\n✅ Result: {result:.2f} {unit}")

def currency_menu() -> None:
    print("\n--- Currency Conversion ---")
    for key, code in CURRENCIES.items():
        print(f"{key}. {code}")
    print("0. Back")

    from_option = input_option("Select source currency: ", [0, *CURRENCIES.keys()])
    if from_option == 0:
        return
    from_currency = CURRENCIES[from_option]

    available_targets = RATES[from_currency].keys()
    targets_map = {i + 1: code for i, code in enumerate(available_targets)}

    print("\n--- Convert to ---")
    for i, code in targets_map.items():
        print(f"{i}. {code}")
    print("0. Back")

    to_option = input_option("Select target currency: ", [0, *targets_map.keys()])
    if to_option == 0:
        return
    to_currency = targets_map[to_option]

    amount = input_number(f"Enter amount in {from_currency}: ")
    rate = RATES[from_currency][to_currency]
    result = convert_currency(amount, rate)

    print(f"\n✅ Result: {result:.2f} {to_currency}")

# ----------------------------------------------------------------------------
# Main Menu and Loop
# ----------------------------------------------------------------------------

MAIN_ACTIONS: dict[int, tuple[str, Callable[[], None]]] = {
    1: ("Convert Temperatures", temperature_menu),
    2: ("Convert Currencies", currency_menu),
}

def main_menu() -> int:
    print("\n=== Main Menu ===")
    for key, (label, _) in MAIN_ACTIONS.items():
        print(f"{key}. {label}")
    print("0. Exit")
    return input_option("Choose an option: ", [0, *MAIN_ACTIONS.keys()])

def main() -> None:
    print("Welcome to the Measures Converter CLI!")
    while True:
        option = main_menu()
        if option == 0:
            print("👋 Goodbye!")
            break
        _, action = MAIN_ACTIONS[option]
        action()

# ----------------------------------------------------------------------------
# Entry Point
# ----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
