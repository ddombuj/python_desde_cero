# 🕸️ CLI Web Scraper

A simple and effective command-line tool written in Python to scrape and display the **latest news titles** from BBC Mundo.

🎯 Designed for learning, practice, and real-world utility.

---

## 🚀 Features

- 🌐 Connects to the BBC Mundo homepage.
- 🧠 Extracts the top news headlines from the site.
- 📄 Clean text output of each title.
- 🧼 Modular structure with clear separation of concerns.
- ⚠️ Basic error handling and logging for failed requests or empty results.

---

## 📂 Structure

cli-web-scraper/  
│  
├── web_scraper.py # Main script with logic and command-line execution  
└── README.md # This file  

---

## 🛠️ Technologies

- Python 3.10+
- Required libraries:
  - `requests`
  - `beautifulsoup4`

You can install dependencies with: 
   ```bash
   pip install -r requirements.txt
   ```

--- 

## ▶️ Usage

1. Clone the repo or download the script:
  ```bash
  git clone https://github.com/ddombuj/cli-web-scraper
  cd cli-web-scraper
  ```
2. Run the program:
  ```bash
  python web_scraper.py
  ```
3. View the top headlines printed to your console.

---

## 📈 Future Ideas
- Extract article URLs along with the titles
- Export results to a CSV or JSON file
- Handle dynamic content using Selenium or Playwright
- Make the scraper class-agnostic using configuration or heuristics
- Add CLI arguments for flexibility (e.g. --limit 10 or --site <url>)

---

## 👨‍💻 Author
Created by Diego Domínguez  
🎓 Made as a personal project to improve Python skills and build a clean CLI tool.
