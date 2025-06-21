"""
CLI Hangman
Author : Diego Domínguez
Updated : 2025-06-21
"""

from __future__ import annotations
from pathlib import Path
import random
from typing import Set

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

WORD_SOURCE = Path(__file__).with_name("English-1000-common.txt")
MAX_TRIES   = 11

# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------

def load_words(filepath: Path) -> list[str]:
    """Read the word list file and return a list with one word per line."""
    if not filepath.exists():
        raise FileNotFoundError(f"Word list not found: {filepath}")
    with filepath.open() as fh:
        return [line.strip().lower() for line in fh if line.strip()]

def mask_word(secret: str, guesses: Set[str]) -> str:
    """Return the secret word with un-guessed letters replaced by underscores."""
    return " ".join(letter if letter in guesses else "_" for letter in secret)

def play_round(secret: str) -> bool:
    """Run a single hangman round. Return True if the player wins."""
    guessed: Set[str] = set()
    wrong:   Set[str] = set()
    remaining = MAX_TRIES
    unique_letters = set(secret)

    while remaining > 0:
        print("\n" + "-" * 40)
        print(f"Word: {mask_word(secret, guessed)}")
        print(f"Wrong letters: {' '.join(sorted(wrong)) or 'None'}")
        print(f"Tries left: {remaining}")
        choice = input("▶ Enter a letter: ").lower().strip()

        # Validate input
        if len(choice) != 1 or not choice.isalpha():
            print("❌ Please type **a single alphabetic character**.")
            continue
        if choice in guessed or choice in wrong:
            print("⚠️  Letter already used. Try another.")
            continue

        # Process guess
        if choice in unique_letters:
            guessed.add(choice)
            print("✅ Good guess!")
            if guessed == unique_letters:
                return True
        else:
            wrong.add(choice)
            remaining -= 1
            print("❌ Wrong guess.")
    return False

# ---------------------------------------------------------------------------
# Menu & main loop
# ---------------------------------------------------------------------------

def main() -> None:
    try:
        words = load_words(WORD_SOURCE)
    except Exception as exc:
        print(f"Error loading word list: {exc}")
        return

    print("🎉 Welcome to CLI Hangman!")
    while True:
        option = input("\nPress ENTER to play or type 0 to exit: ").strip()
        if option == "0":
            print("👋 Goodbye!")
            break

        secret = random.choice(words)
        win = play_round(secret)
        print("\n" + "=" * 40)
        if win:
            print(f"🏆 You WIN! The word was: {secret}")
        else:
            print(f"💀 You LOSE. The word was: {secret}")
        print("=" * 40)

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
