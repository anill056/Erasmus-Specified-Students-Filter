# Erasmus Specified Students Filter 🧮

A Python script that pulls Erasmus application data from a public Google Sheet, filters specific students based on TCKN and name rules, sorts them by score, calculates the engineering average, and exports the result as an Excel file.  
It also **automatically uploads the final Excel file to your Google Drive** and generates a public shareable link.

---

## 🚀 Features

- 📥 Pulls real-time data from Google Sheets
- 🔍 Filters students based on custom rules (TCKN & name patterns)
- 📊 Sorts by score and adds engineering average row
- 📤 Exports to Excel (`.xlsx`)
- ☁️ Uploads result to Google Drive
- 🔗 Returns a public shareable link

---

## ⚙️ Requirements

- Python 3.7+
- [`pandas`](https://pandas.pydata.org/)
- [`openpyxl`](https://openpyxl.readthedocs.io/)
- [`PyDrive`](https://pypi.org/project/PyDrive/)

Install dependencies:

```bash
pip install pandas openpyxl pydrive
```

---

## 🧭 How to Use

### 1. Clone or download this repository

```bash
git clone git@github.com:yourusername/erasmus-filter.git
cd erasmus-filter
```

### 2. Set up Google Drive API

To enable automatic upload to Google Drive, you must generate a `client_secrets.json` file:

#### 🔒 Why?
This file contains your personal credentials to connect your Google account securely.

#### 📌 Steps:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable **Google Drive API**
4. Go to **APIs & Services > Credentials**
5. Create **OAuth client ID** → Choose **Desktop app**
6. Download the file → rename to `client_secrets.json`
7. Place the file next to your Python script (locally, **do not upload** this to GitHub)

**✅ Warning:**  
This file is already listed in `.gitignore` and will NOT be committed.

---

### 3. Run the script

```bash
python erasmus_filter.py
```

You will be prompted to sign into your Google Account in the browser.

---

## 🧾 Output

The final file will be saved as:

```
Erasmus Specified Students.xlsx
```

And will be automatically uploaded to your Google Drive with public access enabled.

---

## 🧪 Example Output Format

```
| TCKN     | Ad Soyad         | Öğrenci No | Puan  |
|----------|------------------|------------|--------|
| 21345678 | Ahmet Yılmaz     | 20201234   | 92.5   |
| 10675412 | Alper Koç        | 20184567   | 88.0   |
|          | Engineering Average         |        | 84.3   |
```

---

## 📁 .gitignore

This project includes a `.gitignore` to prevent pushing sensitive or unnecessary files:

```
client_secrets.json
__pycache__/
*.pyc
*.log
.env
.DS_Store
```

---

## 📜 License

MIT License  
© 2025 Anıl Aksu

---

## 🤝 Contributions

Pull requests are welcome. For major changes, please open an issue first.

---

## 🌍 Example Use Cases

- Automating Erasmus selection & sorting
- Generating reports from Sheets
- One-click public Drive uploads
