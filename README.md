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

## 🏗️ Building the Application Locally

This section provides step-by-step instructions to build and run Clippy Pie Lite on your local machine.

### Prerequisites

Before you start, ensure you have the following installed:

* **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
* **pip** - Python package manager (comes with Python)
* **Git** (optional, for cloning the repository)
* **Administrator access** (required for global keyboard shortcuts on Windows)

### Step 1: Clone or Download the Repository

**Option A: Using Git**
```bash
git clone https://github.com/the-AY/Clippy-Pie-Lite-The-Clipboard-Application.git
cd Clippy-Pie-Lite-The-Clipboard-Application
```

**Option B: Manual Download**
- Download the repository as a ZIP file
- Extract it to your desired location
- Open terminal/PowerShell in the `clipboard-app/Python_based_Clippy/` directory

### Step 2: Install Dependencies

Navigate to the application directory:

```bash
cd clipboard-app/Python_based_Clippy
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Or manually install the packages:

```bash
pip install customtkinter keyboard pyinstaller
```

### Step 3: Run in Development Mode

To test the application before building:

```bash
python app.py
```

The application window should appear. Test the features:
- Add categories and clipboard entries
- Use the search functionality
- Test copy-to-clipboard functionality
- Create or modify profiles in the sidebar

### Step 4: Build Executable (Optional)

To create a portable `.exe` file:

```bash
pyinstaller --onefile --noconsole --name "Clippy" app.py
```

**Parameters explained:**
- `--onefile` → Creates a single executable file
- `--noconsole` → Hides the console window
- `--name "Clippy"` → Names the output executable

After the build completes, the executable will be located at:

```
dist/Clippy.exe
```

### Step 5: Run the Executable

Double-click `dist/Clippy.exe` to launch the application, or run:

```bash
.\dist\Clippy.exe
```

### Data Storage

- Application data is stored in `data.json` in the same directory as the application
- This file contains all your clipboard categories and entries
- Back up this file if you want to preserve your data

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
