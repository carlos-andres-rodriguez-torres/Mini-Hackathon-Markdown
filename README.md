# 📝 Mini-Hackathon-Markdown

This repository contains a mini project to extract information from a web page and convert it into **Markdown** format. The goal is to practice web scraping, data processing, and working with Markdown files.

---

## 📂 Project Structure

```
.
├── requirements.txt     # Project dependencies
├── code.py               # Main script to run the process
├── README.md             # This file
└── .gitignore            # Ignored files and folders
```

---

## 🏁 Setup Instructions

### 1️⃣ Create a Virtual Environment

```bash
python3 -m venv virtual_environment
```

### 2️⃣ Activate the Virtual Environment

On Linux / Mac:

```bash
source virtual_environment/bin/activate
```

On Windows:

```bash
virtual_environment\Scriptsctivate
```

---

### 3️⃣ Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

---

## 🚀 Execution

### 4️⃣ Run the Main Script

```bash
python3 markdown.py
```

---

## 📥 Notes

- The script allows the user to input a URL.
- It downloads the page's HTML content.
- Converts the HTML to **Markdown** format.
- Saves the result to a `.md` file.

---

## ✅ Requirements

- Python 3.8 or later.
- Required libraries (in `requirements.txt`):
  - `requests`
  - `markdownify`

---

---

## 📄 License

This project was developed for educational purposes.

---

## ✍️ Authors

- Carlos Rodríguez, Oliver Chan, Juan José Acevedo, Jofra Coll

---
