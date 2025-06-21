# CLI Hangman

A simple and interactive command-line hangman game written in Python.

🎯 Designed for fun, learning, and practicing Python CLI programming.

---

## 🚀 Features

- 🎲 Randomly selects a secret word from a word list file.
- 🔤 Input validation allowing only single alphabetic letters.
- ❌ Tracks wrong guesses and limits attempts (default 11 tries).
- 👀 Displays the current progress of the word with masked letters.
- 🔄 Play multiple rounds until you decide to exit.
- 🧹 Clean and modular code structure for easy understanding and extension.

---

## 📂 Structure

cli-hangman/  
│  
├── hangman.py             # Main script with game logic and menu  
├── English-1000-common.txt # Word list file with common English words  
└── README.md              # This file  

---

## 🛠️ Technologies

- Python 3.8+
- No external dependencies

---

## ▶️ Usage

1. Clone the repo or download the script:

   ```bash
   git clone https://github.com/ddombuj/cli-hangman
   cd cli-hangman
   
2. Run the game:

   ```bash
   python hangman.py
3. Follow the on-screen prompts

---

## 📈 Future Ideas
- Add difficulty levels with varying max attempts or word length
- Include hints or categories for words
- Add support for multiplayer mode
- Implement a scoring system and leaderboard
- Create a GUI version with Tkinter or another toolkit

## 👨‍💻 Author
Created by Diego Domínguez  
🎓 Made as a personal project to improve Python skills and build a clean CLI tool.
