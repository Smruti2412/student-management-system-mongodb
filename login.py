import tkinter as tk
from tkinter import messagebox
from database import users
import dashboard


def login():
    username = entry_user.get()
    password = entry_pass.get()

    if not username or not password:
        messagebox.showwarning("Warning", "Please enter username and password")
        return

    user = users.find_one({"username": username, "password": password})
    if user:
        root.destroy()
        dashboard.open_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid Credentials")


def toggle_password():
    if entry_pass.cget("show") == "*":
        entry_pass.config(show="")
        show_btn.config(text="Hide")
    else:
        entry_pass.config(show="*")
        show_btn.config(text="Show")


# ================= WINDOW =================
root = tk.Tk()
root.title("Login - Student Management System")
root.geometry("950x550")
root.resizable(True, True)
root.configure(bg="#0f172a")

# ================= HEADER =================
header = tk.Frame(root, bg="#1e293b", height=90)
header.pack(fill="x")

tk.Label(
    header,
    text="🎓 Student Management System",
    bg="#1e293b",
    fg="white",
    font=("Segoe UI", 24, "bold")   # Increased
).pack(pady=25)

# ================= CENTER FRAME =================
center = tk.Frame(root, bg="#0f172a")
center.pack(expand=True)

# ================= LOGIN CARD =================
card = tk.Frame(center, bg="white", padx=60, pady=50)
card.pack()

card.config(highlightbackground="#94a3b8", highlightthickness=1)

tk.Label(
    card,
    text="Admin Login",
    bg="white",
    fg="#0f172a",
    font=("Segoe UI", 22, "bold")   # Increased
).grid(row=0, column=0, columnspan=4, pady=(0, 35))


# ================= FIELD STYLE =================
def styled_entry(parent, row, label_text, show=None):
    tk.Label(
        parent,
        text=label_text,
        bg="white",
        fg="#475569",
        font=("Segoe UI", 13, "bold")   # Increased
    ).grid(row=row, column=0, sticky="w", pady=12)

    entry = tk.Entry(
        parent,
        width=32,
        font=("Segoe UI", 14),   # Increased
        bg="#f1f5f9",
        relief="flat",
        show=show
    )
    entry.grid(row=row, column=1, columnspan=2, pady=12, ipady=8)

    # Focus Highlight Effect
    entry.bind("<FocusIn>", lambda e: entry.config(bg="#dbeafe"))
    entry.bind("<FocusOut>", lambda e: entry.config(bg="#f1f5f9"))

    return entry


# Username
entry_user = styled_entry(card, 1, "Username")

# Password
entry_pass = styled_entry(card, 2, "Password", show="*")

# Show Button
show_btn = tk.Button(
    card,
    text="Show",
    command=toggle_password,
    bg="#e2e8f0",
    fg="#0f172a",
    relief="flat",
    font=("Segoe UI", 11),   # Increased
    cursor="hand2",
    padx=10,
    pady=5
)
show_btn.grid(row=2, column=3, padx=10)


# ================= BUTTON STYLE =================
def modern_button(parent, text, command):
    shadow = tk.Frame(parent, bg="#94a3b8")
    shadow.grid(row=3, column=0, columnspan=4, pady=40)

    btn = tk.Button(
        shadow,
        text=text,
        command=command,
        bg="#3b82f6",
        fg="white",
        font=("Segoe UI", 15, "bold"),   # Increased
        relief="flat",
        width=25,
        pady=12,
        cursor="hand2"
    )
    btn.pack(padx=2, pady=2)

    # Hover Effect
    btn.bind("<Enter>", lambda e: btn.config(bg="#1d4ed8"))
    btn.bind("<Leave>", lambda e: btn.config(bg="#3b82f6"))

    return btn


modern_button(card, "Login", login)


# ================= FOOTER =================
tk.Label(
    root,
    text="© 2026 Student Management System | Developed by Smruti Lohar",
    bg="#0f172a",
    fg="#94a3b8",
    font=("Segoe UI", 11)   # Increased
).pack(side="bottom", pady=20)


root.mainloop()
