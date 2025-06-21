"""
Password Generator CLI
Author: Diego Domínguez
Date: 2025‑06‑21
"""

from secrets import choice
import string
from typing import Dict

# ---------------------------------------------------------------------------
# Initial configuration
# ---------------------------------------------------------------------------

DEFAULT_LENGTH = 20  # Default password length

# Each category contains a character set and an enabled flag
Category = Dict[str, bool | str]
CATEGORIES: dict[int, Category] = {
    1: {"name": "Lowercase",  "chars": string.ascii_lowercase, "enabled": True},
    2: {"name": "Uppercase",  "chars": string.ascii_uppercase, "enabled": True},
    3: {"name": "Digits",     "chars": string.digits,          "enabled": True},
    4: {"name": "Symbols",    "chars": string.punctuation,     "enabled": True},
}

# ---------------------------------------------------------------------------
# Business logic (pure functions, no prints)
# ---------------------------------------------------------------------------

def build_pool(categories: dict[int, Category]) -> str:
    """Concatenates and returns all characters from enabled categories."""
    pool = "".join(cat["chars"] for cat in categories.values() if cat["enabled"])
    if not pool:
        raise ValueError("At least one category must be enabled.")
    return pool


def generate_password(length: int, pool: str) -> str:
    """Generates and returns a random password of the given length."""
    return "".join(choice(pool) for _ in range(length))

# ---------------------------------------------------------------------------
# User interface
# ---------------------------------------------------------------------------

def show_menu() -> int | None:
    """Displays the menu and returns the user's selection."""
    print("\n------- Password Generator -------")
    for key, cat in CATEGORIES.items():
        status = "Yes" if cat["enabled"] else "No"
        print(f"{key}. {cat['name']:10s} [{status}]")
    print("0. Exit / Press ENTER to generate password")
    print("----------------------------------")

    user_input = input(">> ").strip()
    if user_input == "":
        return None  # Generate password
    if user_input.isdigit():
        return int(user_input)
    print("Invalid input. Please enter a number.")
    return show_menu()  # Tail recursion (safe for simple CLI use)

def toggle_category(option: int) -> None:
    """Toggles the enabled state of the selected category."""
    if option in CATEGORIES:
        CATEGORIES[option]["enabled"] = not CATEGORIES[option]["enabled"]

def main() -> None:
    while True:
        selection = show_menu()
        if selection == 0:
            print("👋 See you next time!")
            break
        if selection is None:
            try:
                pool = build_pool(CATEGORIES)
                pwd  = generate_password(DEFAULT_LENGTH, pool)
                print(f"\nYour new password ({DEFAULT_LENGTH}):  {pwd}\n")
            except ValueError as exc:
                print(f"⚠️  {exc}")
        else:
            toggle_category(selection)

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()
