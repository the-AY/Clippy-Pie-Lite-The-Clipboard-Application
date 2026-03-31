# 🚀 Clippy Pie Lite

A lightweight, fast, and portable clipboard manager designed to speed up job applications.

Clippy Pie Lite helps you store frequently used data (name, email, cover letters, etc.) and paste them instantly while applying for jobs.

---

## ✨ Features

* 📂 **Category-based organization** (Frontend, Backend, Internships, etc.)
* 📋 **One-click copy** for instant pasting
* 📝 **Supports large text** (1000+ words for cover letters, SOPs)
* 🔍 **Search functionality** (filter entries instantly)
* 📁 **Folder integration**

  * Open resume folder
  * Copy folder path
* ⚡ **Global shortcut**

  * `Ctrl + Shift + Space` to show/hide app
* 🎨 **Modern UI**

  * Sidebar layout
  * Clean and minimal design
* 🗑 **Clear data option** with confirmation
* 📦 **Portable EXE**

  * No installation required
  * Works offline

---

## 🧰 Requirements

Install the following before running:

* Python 3.8+
* pip (Python package manager)

---

## 📦 Required Packages

Install dependencies using:

```bash
pip install customtkinter keyboard pyinstaller
```

### Package Details

* `customtkinter` → Modern UI framework
* `keyboard` → Global shortcut support
* `pyinstaller` → Convert app to executable

---

## ▶️ Run the App (Development Mode)

```bash
python app.py
```

---

## 📦 Build EXE (Portable Version)

### Step 1: Install PyInstaller

```bash
pip install pyinstaller
```

---

### Step 2: Build Executable

```bash
pyinstaller --onefile --noconsole app.py
```

---

### Step 3: Locate Output

After build completes, go to:

```
dist/app.exe
```
Also available in this repo pre built .EXE file download and Use it .
---

## ⚠️ Notes

* 🔑 Global shortcut may require **Run as Administrator** (Windows)
* 🛡 Some antivirus tools may flag `.exe` (false positive due to PyInstaller)
* 📁 Data is stored locally in `data.json`

---

## 📁 Project Structure

```
Clippy-Pie-Lite/
│
├── app.py
├── data.json (auto-generated)
├── dist/
│   └── app.exe
└── README.md
```

---

## 💡 Use Case

Perfect for:

* Job applications
* Freelancing platforms
* Repetitive form filling
* Storing reusable text snippets

---

## 👨‍💻 Credits

Developed by **Bot** 🚀

---

## 📌 Future Improvements

* System tray support
* Auto paste feature
* Drag & reorder entries
* Export / import data
* Custom app icon

---

## ⭐ Support

If you like this project:

* Star ⭐ the repo
* Share with others
* Improve & contribute 🚀
