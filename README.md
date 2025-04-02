
# Erasmus Specified Students Filter 🧮

A Python script that pulls Erasmus application data from a public Google Sheet, filters specific students based on TCKN and name rules, sorts them by score, calculates the engineering average, and exports the result as an Excel file.  
It also **automatically uploads the final Excel file to Google Drive** and generates a public shareable link.

---

## 🚀 Features

- 📥 Pulls live data from Google Sheets (CSV format)
- 🔎 Filters students by partial TCKN and name patterns
- 📊 Sorts by score and calculates overall average
- 📤 Exports to Excel (`.xlsx`)
- ☁️ Uploads the file to Google Drive
- 🔗 Returns a public shareable link

---

## 📂 Output Example

```
| TCKN   | Ad Soyad     | Öğrenci No | Puan |
|--------|--------------|------------|------|
| 213456 | Ahmet Yılmaz | 20201234   | 92.5 |
| 104512 | Alper Koç    | 20205678   | 89.0 |
| ...    | ...          | ...        | ...  |
|        | Engineering Average       | 84.2 |
```

---

## ⚙️ Requirements

- Python 3.7+
- [`pandas`](https://pandas.pydata.org/)
- [`openpyxl`](https://openpyxl.readthedocs.io/)
- [`PyDrive`](https://pythonhosted.org/PyDrive/)

Install via pip:
```bash
pip install pandas openpyxl pydrive
```

---

## 🧭 How to Use

### 1. Clone this repo or copy the `erasmus_filter.py` file.

### 2. Set up Google Drive API credentials:
- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Create a project → Enable **Google Drive API**
- Go to **Credentials → Create OAuth client ID** (choose **Desktop app**)
- Download `client_secrets.json`
- Place it in the same folder as `erasmus_filter.py`

### 3. Run the script:
```bash
python erasmus_filter.py
```

### 4. Script will:
- Open browser to authenticate with Google
- Pull data → Filter → Export Excel
- Upload file to your Drive
- Give you a public shareable link

---

## 📜 License

MIT License  
© 2025 Anıl AKSU

---

## 🤝 Contributions

Pull requests are welcome. For major changes, please open an issue first.

---

## 🌍 Example Usage Scenarios

- Filtering Erasmus applicants
- Preparing automatic ranking sheets
- Sharing results with departments via Drive
