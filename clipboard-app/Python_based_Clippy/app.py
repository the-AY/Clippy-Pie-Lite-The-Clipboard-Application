# =============================
# 🚀 CLIPPY PIE LITE - VERSION 4
# =============================

import customtkinter as ctk
import json
import os
import subprocess
from tkinter import messagebox
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

DATA_FILE = "data.json"

# -----------------------------
# DATA HANDLING
# -----------------------------

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"categories": []}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


data = load_data()

# -----------------------------
# MAIN APP
# -----------------------------

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Clippy Pie Lite")
        self.geometry("700x500")
        self.attributes("-topmost", True)

        self.search_var = ctk.StringVar()

        self.create_ui()
        self.refresh_categories()

        threading.Thread(target=self.global_shortcut_listener, daemon=True).start()

    # -------------------------
    # UI
    # -------------------------
    def create_ui(self):

        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True)

        # SIDEBAR
        sidebar = ctk.CTkFrame(main_frame, width=200)
        sidebar.pack(side="left", fill="y")

        ctk.CTkLabel(sidebar, text="Categories", font=("Arial", 16, "bold")).pack(pady=10)

        self.cat_list = ctk.CTkScrollableFrame(sidebar)
        self.cat_list.pack(fill="both", expand=True, padx=5)

        ctk.CTkButton(sidebar, text="+ Add", command=self.add_category).pack(pady=5)

        # RIGHT PANEL
        right = ctk.CTkFrame(main_frame)
        right.pack(side="right", fill="both", expand=True)

        # SEARCH WITH ICON
        search_frame = ctk.CTkFrame(right)
        search_frame.pack(pady=5, padx=10, fill="x")

        ctk.CTkLabel(search_frame, text="🔍").pack(side="left", padx=5)

        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search...", textvariable=self.search_var)
        self.search_entry.pack(side="left", fill="x", expand=True)
        self.search_var.trace_add("write", lambda *args: self.refresh_entries())

        # INPUT
        self.title_entry = ctk.CTkEntry(right, placeholder_text="Title")
        self.title_entry.pack(pady=5, padx=10, fill="x")

        self.value_entry = ctk.CTkTextbox(right, height=80)
        self.value_entry.pack(pady=5, padx=10, fill="x")

        # soft grey placeholder
        self.value_entry.insert("0.0", "Enter description or data...")
        self.value_entry.configure(text_color="#888888")

        self.value_entry.bind("<FocusIn>", self.clear_placeholder)
        self.value_entry.bind("<FocusOut>", self.add_placeholder)

        ctk.CTkButton(right, text="➕ Add Entry", command=self.add_entry).pack(pady=5)

        # ENTRIES
        self.entries_frame = ctk.CTkScrollableFrame(right)
        self.entries_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # FOOTER
        footer = ctk.CTkFrame(right)
        footer.pack(fill="x", padx=10, pady=5)

        ctk.CTkButton(footer, text="📂 Folder", command=self.open_folder).pack(side="left", padx=5)
        ctk.CTkButton(footer, text="🔗 Copy Path", command=self.copy_folder_path).pack(side="left", padx=5)
        ctk.CTkButton(footer, text="🗑 Clear", fg_color="#a83232", command=self.clear_data).pack(side="right", padx=5)

    # -------------------------
    # PLACEHOLDER HANDLING
    # -------------------------

    def clear_placeholder(self, event):
        if self.value_entry.get("0.0", "end").strip() == "Enter description or data...":
            self.value_entry.delete("0.0", "end")
            self.value_entry.configure(text_color="#ffffff")

    def add_placeholder(self, event):
        if not self.value_entry.get("0.0", "end").strip():
            self.value_entry.insert("0.0", "Enter description or data...")
            self.value_entry.configure(text_color="#888888")

    # -------------------------
    # CATEGORY
    # -------------------------

    def refresh_categories(self):
        for w in self.cat_list.winfo_children():
            w.destroy()

        for cat in data["categories"]:
            btn = ctk.CTkButton(self.cat_list, text=cat["name"],
                                command=lambda c=cat: self.select_category(c))
            btn.pack(fill="x", pady=2)

        if data["categories"]:
            self.select_category(data["categories"][0])

    def select_category(self, cat):
        self.current_category = cat
        self.refresh_entries()

    def add_category(self):
        dialog = ctk.CTkInputDialog(text="Enter category name:", title="New Category")
        name = dialog.get_input()
        if not name:
            return

        data["categories"].append({"name": name, "entries": [], "folder": ""})
        save_data(data)
        self.refresh_categories()

    # -------------------------
    # ENTRIES
    # -------------------------

    def add_entry(self):
        if not hasattr(self, "current_category"):
            return

        title = self.title_entry.get()
        value = self.value_entry.get("0.0", "end").strip()

        if not title or not value or value == "Enter description or data...":
            return

        self.current_category["entries"].append({"title": title, "value": value})
        save_data(data)

        self.title_entry.delete(0, "end")
        self.value_entry.delete("0.0", "end")
        self.add_placeholder(None)

        self.refresh_entries()

    def refresh_entries(self):
        for w in self.entries_frame.winfo_children():
            w.destroy()

        if not hasattr(self, "current_category"):
            return

        search = self.search_var.get().lower()

        for entry in self.current_category["entries"]:
            if search and search not in entry["title"].lower() and search not in entry["value"].lower():
                continue

            frame = ctk.CTkFrame(self.entries_frame)
            frame.pack(fill="x", pady=3)

            ctk.CTkLabel(frame, text=entry["title"], font=("Arial", 12, "bold")).pack(side="left", padx=5)

            ctk.CTkButton(frame, text="📋", width=40,
                          command=lambda v=entry["value"]: self.copy_text(v)).pack(side="right")

    def copy_text(self, text):
        self.clipboard_clear()
        self.clipboard_append(text)

    # -------------------------
    # FOLDER
    # -------------------------

    def open_folder(self):
        cat = self.current_category

        if not cat["folder"]:
            dialog = ctk.CTkInputDialog(text="Enter folder path:", title="Folder Path")
            path = dialog.get_input()
            if not path:
                return
            cat["folder"] = path
            save_data(data)

        if os.path.exists(cat["folder"]):
            subprocess.Popen(["explorer", cat["folder"]])

    def copy_folder_path(self):
        if self.current_category["folder"]:
            self.copy_text(self.current_category["folder"])

    # -------------------------
    # CLEAR
    # -------------------------

    def clear_data(self):
        if messagebox.askyesno("Confirm", "Delete ALL data?"):
            global data
            data = {"categories": []}
            save_data(data)
            self.refresh_categories()
            self.refresh_entries()

    # -------------------------
    # SHORTCUT
    # -------------------------

    def global_shortcut_listener(self):
        try:
            import keyboard
            keyboard.add_hotkey("ctrl+shift+space", self.toggle_window)
            keyboard.wait()
        except:
            pass

    def toggle_window(self):
        if self.state() == "withdrawn":
            self.deiconify()
        else:
            self.withdraw()

# -----------------------------
# RUN
# -----------------------------

if __name__ == "__main__":
    app = App()
    app.mainloop()
