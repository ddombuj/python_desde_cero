"""CLI Calculator
Author: Diego Domínguez
date: 2025‑06‑17

A simple console‑based calculator.
"""
from __future__ import annotations

from typing import Callable, Tuple

# ----------------------------------------------------------------------------
# Core arithmetic operations (pure functions)
# ----------------------------------------------------------------------------

def add(a: float, b: float) -> float:
    """Return *a + b*."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return *a - b*."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return *a × b*."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return *a ÷ b*.
    Raises
    ------
    ZeroDivisionError
        If *b* is zero.
    """
    if b == 0:
        raise ZeroDivisionError("It's not possible to divide by 0")
    return a / b


# ----------------------------------------------------------------------------
# User‑interface helpers (I/O separated from logic)
# ----------------------------------------------------------------------------

def read_number(prompt: str) -> float | None:
    """Return a *float* read from *input()* or *None* if the value is not numeric."""
    value = input(prompt)
    try:
        return float(value)
    except ValueError:
        return None


def read_two_numbers() -> Tuple[float, float] | None:
    """Prompt the user for two numbers.  Return *None* to signal cancellation."""
    print("(Insert a letter to go back to menu)")

    first = read_number("Insert the first number: ")
    if first is None:
        return None

    second = read_number("Insert the second number: ")
    if second is None:
        return None

    return first, second


# ----------------------------------------------------------------------------
# Menu definition and rendering
# ----------------------------------------------------------------------------

MenuAction = Callable[[float, float], float]

OPERATIONS: dict[int, tuple[str, MenuAction, str]] = {
    1: ("Sumar", add, "+"),
    2: ("Restar", subtract, "-"),
    3: ("Multiplicar", multiply, "×"),
    4: ("Dividir", divide, "÷"),
}

def print_menu() -> int:
    """Display the menu and return the chosen option as an *int*."""
    while True:
        print("\n------- Menu -------")
        for key, (name, _, _) in OPERATIONS.items():
            print(f"{key}. {name}")
        print("0. Exit")
        print("--------------------")

        choice = input("Type the number of your option: ")
        if choice.isdigit():
            choice_int = int(choice)
            if 0 <= choice_int <= len(OPERATIONS):
                return choice_int
        print("Option is invalid, try again…\n")


# ----------------------------------------------------------------------------
# Main program loop
# ----------------------------------------------------------------------------

def main() -> None:
    """Run the interactive calculator until the user chooses to exit."""
    while True:
        option = print_menu()
        if option == 0:
            break

        numbers = read_two_numbers()
        if numbers is None:  # user cancelled number entry
            continue

        a, b = numbers
        name, func, symbol = OPERATIONS[option]
        print(f"\n---- {name} ----")
        try:
            result = func(a, b)
        except ZeroDivisionError as exc:
            print(exc)
        else:
            print(f"{a} {symbol} {b} = {result}")

    print("Saliendo…")


# ----------------------------------------------------------------------------
# Entry‑point guard
# ----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
