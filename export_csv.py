import csv
from tkinter import messagebox, filedialog
from database import students

def export_to_csv():
    data = list(students.find())

    if not data:
        messagebox.showwarning("No Data", "No records available to export")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        title="Save CSV File"
    )

    if not file_path:
        return  # user cancelled

    try:
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "Name", "Email", "Course", "Mobile"])

            for s in data:
                writer.writerow([
                    s.get("student_id", ""),
                    s.get("name", ""),
                    s.get("email", ""),
                    s.get("course", ""),
                    s.get("mobile", "")
                ])

        messagebox.showinfo("Success", "Data exported successfully")

    except Exception as e:
        messagebox.showerror("Error", str(e))
