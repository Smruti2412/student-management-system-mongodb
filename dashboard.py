import tkinter as tk
from tkinter import ttk, messagebox
from database import students
from validation import validate_student
from export_csv import export_to_csv


def open_dashboard():
    root = tk.Tk()
    root.title("Student Management System")
    root.state("zoomed")
    root.configure(bg="#f1f5f9")

    # ================= COLORS =================
    BG = "#f1f5f9"
    HEADER = "#1e293b"
    CARD = "#ffffff"
    TEXT = "#0f172a"
    MUTED = "#64748b"
    PRIMARY = "#3b82f6"
    SUCCESS = "#10b981"
    DANGER = "#ef4444"
    INPUT_BG = "#f8fafc"
    INPUT_ACTIVE = "#dbeafe"

    # ================= HEADER =================
    header = tk.Frame(root, bg=HEADER, height=75)
    header.pack(fill="x")

    tk.Label(
        header,
        text="🎓 Student Management Dashboard",
        bg=HEADER,
        fg="white",
        font=("Segoe UI", 22, "bold")
    ).pack(pady=18)

    # ================= MAIN =================
    main = tk.Frame(root, bg=BG)
    main.pack(fill="both", expand=True, padx=30, pady=20)

    # ================= LEFT CARD =================
    left = tk.Frame(main, bg=CARD)
    left.pack(side="left", fill="y", padx=(0, 20))
    left.config(highlightbackground="#e2e8f0", highlightthickness=1)

    tk.Label(
        left,
        text="Student Details",
        bg=CARD,
        fg=TEXT,
        font=("Segoe UI", 14, "bold")
    ).pack(pady=(20, 10))

    form = tk.Frame(left, bg=CARD)
    form.pack(padx=25, pady=10)

    def field(label, row):
        tk.Label(
            form,
            text=label,
            bg=CARD,
            fg=MUTED,
            font=("Segoe UI", 10, "bold")
        ).grid(row=row, column=0, sticky="w", pady=8)

        entry = tk.Entry(
            form,
            width=28,
            font=("Segoe UI", 10),
            bg=INPUT_BG,
            relief="flat",
            highlightthickness=2,
            highlightbackground="#e2e8f0"
        )
        entry.grid(row=row, column=1, pady=8, padx=5)

        # Highlight effect on click
        entry.bind("<FocusIn>", lambda e: entry.config(bg=INPUT_ACTIVE))
        entry.bind("<FocusOut>", lambda e: entry.config(bg=INPUT_BG))

        return entry

    e_id = field("Student ID", 0)
    e_name = field("Name", 1)
    e_email = field("Email", 2)
    e_course = field("Course / Class", 3)
    e_mobile = field("Contact No", 4)

    # ================= FUNCTIONS =================
    def clear():
        for e in (e_id, e_name, e_email, e_course, e_mobile):
            e.delete(0, tk.END)

    def insert():
        err = validate_student(e_id.get(), e_name.get(), e_email.get(), e_mobile.get())
        if err:
            messagebox.showerror("Error", err)
            return

        students.insert_one({
            "student_id": e_id.get(),
            "name": e_name.get(),
            "email": e_email.get(),
            "course": e_course.get(),
            "mobile": e_mobile.get()
        })
        fetch()
        clear()

    def update():
        students.update_one(
            {"student_id": e_id.get()},
            {"$set": {
                "name": e_name.get(),
                "email": e_email.get(),
                "course": e_course.get(),
                "mobile": e_mobile.get()
            }}
        )
        fetch()

    def search():
        query = search_entry.get().strip()

        # Clear table first
        table.delete(*table.get_children())

        # If search box empty → show all records
        if not query:
            fetch()
            return

        # Case-insensitive partial match
        results = list(students.find({
            "$or": [
            {"student_id": {"$regex": query, "$options": "i"}},
            {"name": {"$regex": query, "$options": "i"}},
            {"email": {"$regex": query, "$options": "i"}},
            {"course": {"$regex": query, "$options": "i"}},
            {"mobile": {"$regex": query, "$options": "i"}}
        ]
        }))

        # If no results found → show message and reload all data
        if not results:
            messagebox.showinfo("Search Result", "No matching student found.")
            fetch()
            return

        # Insert filtered results
        for s in results:
            table.insert("", "end", values=(
                s["student_id"],
                s["name"],
                s["email"],
                s["course"],
                s["mobile"]
            ))

    def delete():
        if not messagebox.askyesno("Confirm", "Delete selected record?"):
            return
        students.delete_one({"student_id": e_id.get()})
        fetch()
        clear()

    # ================= BUTTON STYLE =================
    def styled_button(parent, text, cmd, color):
        btn = tk.Button(
            parent,
            text=text,
            command=cmd,
            bg=color,
            fg="white",
            activebackground="#1e40af",
            activeforeground="white",
            relief="flat",
            font=("Segoe UI", 10, "bold"),
            width=12,
            cursor="hand2"
        )

        # Hover effect
        btn.bind("<Enter>", lambda e: btn.config(bg="#1d4ed8"))
        btn.bind("<Leave>", lambda e: btn.config(bg=color))

        return btn

    btn_frame = tk.Frame(left, bg=CARD)
    btn_frame.pack(pady=20)

    styled_button(btn_frame, "Add", insert, SUCCESS).grid(row=0, column=0, padx=8, pady=8)
    styled_button(btn_frame, "Update", update, PRIMARY).grid(row=0, column=1, padx=8, pady=8)
    styled_button(btn_frame, "Delete", delete, DANGER).grid(row=1, column=0, padx=8, pady=8)
    styled_button(btn_frame, "Clear", clear, MUTED).grid(row=1, column=1, padx=8, pady=8)

    # ================= RIGHT PANEL =================
    right = tk.Frame(main, bg=CARD)
    right.pack(side="right", fill="both", expand=True)
    right.config(highlightbackground="#e2e8f0", highlightthickness=1)

    top_right = tk.Frame(right, bg=CARD)
    top_right.pack(fill="x", pady=15, padx=20)

    tk.Label(
        top_right,
        text="Search Student Records:",
        bg=CARD,
        fg=TEXT,
        font=("Segoe UI", 10, "bold")
    ).pack(side="left")

    # Search Entry
    search_entry = tk.Entry(
        top_right,
        font=("Segoe UI", 10),  # Slightly bigger
        width=20,
        bg=INPUT_BG,
        relief="flat",
        highlightthickness=2,
        highlightbackground="#cbd5e1",
        highlightcolor=PRIMARY
    )
    search_entry.pack(side="left", padx=12, ipady=6)

    # Focus Effect (same as left fields)
    search_entry.bind("<FocusIn>", lambda e: search_entry.config(bg=INPUT_ACTIVE))
    search_entry.bind("<FocusOut>", lambda e: search_entry.config(bg=INPUT_BG))

    tk.Button(
        top_right,
        text="Search",
        command=search,
        bg=PRIMARY,
        fg="white",
        relief="flat",
        padx=15,
        cursor="hand2"
    ).pack(side="left")

    tk.Button(
        top_right,
        text="Export CSV",
        command=export_to_csv,
        bg="#475569",
        fg="white",
        relief="flat",
        padx=15,
        cursor="hand2"
    ).pack(side="right")

    # ================= TABLE =================
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    background="#f8fafc",
                    foreground=TEXT,
                    rowheight=32,
                    fieldbackground="#f8fafc",
                    font=("Segoe UI", 10))
    style.configure("Treeview.Heading",
                    font=("Segoe UI", 10, "bold"),
                    background="#e2e8f0")

    columns = ("ID", "Name", "Email", "Course", "Contact")
    table = ttk.Treeview(right, columns=columns, show="headings")

    for col in columns:
        table.heading(col, text=col)
        table.column(col, anchor="center")

    table.pack(fill="both", expand=True, padx=20, pady=15)

    def fetch():
        table.delete(*table.get_children())
        for s in students.find():
            table.insert("", "end", values=(
                s["student_id"], s["name"], s["email"], s["course"], s["mobile"]
            ))

    def select_row(event):
        values = table.item(table.focus(), "values")
        if values:
            clear()
            e_id.insert(0, values[0])
            e_name.insert(0, values[1])
            e_email.insert(0, values[2])
            e_course.insert(0, values[3])
            e_mobile.insert(0, values[4])

    table.bind("<ButtonRelease-1>", select_row)

    fetch()
    root.mainloop()