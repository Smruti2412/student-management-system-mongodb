# 🎓 Student Management System  
A GUI-based Student Management System developed using Python and MongoDB.

---

## 📌 Project Description

The Student Management System is a desktop application developed to replace traditional manual record-keeping systems.  

It provides an easy-to-use graphical user interface (GUI) for managing student records efficiently. The system uses MongoDB as the backend database to store and manage student data securely.

This project demonstrates the integration of Python with MongoDB and implements full CRUD (Create, Read, Update, Delete) operations.

---

## 🏫 Real-World Scenario

A mid-sized educational organization wants to replace its manual student record system with a digital solution that:

- Stores data efficiently
- Allows quick search and updates
- Reduces paperwork
- Provides secure access through login authentication

This system fulfills those requirements using modern database and GUI technologies.

---

## 🛠 Technologies Used

- Python 3.x
- Tkinter (GUI Development)
- MongoDB (Database)
- PyMongo (MongoDB-Python Connector)
- CSV Module (Export functionality)

---

## ✨ Features

### 🔐 User Authentication
- Admin login system
- Password show/hide toggle
- Credential validation using MongoDB

### 📋 Student Record Management
- Add new student records
- View all stored records
- Search records (by ID, Name, Email, Course, Mobile)
- Update existing records
- Delete selected records with confirmation

### 📤 Additional Functionalities
- Export data to CSV file
- Input validation with error messages
- Case-insensitive multi-field search
- Modern and user-friendly interface

---

## 🗄 Database Structure

### Database Name:
```
student_management
```

### Collections:
- `users` → Stores login credentials
- `students` → Stores student records

### Sample Student Document:
```json
{
  "student_id": "101",
  "name": "Pranav Lohar",
  "email": "pranav@gmail.com",
  "course": "BSc IT",
  "mobile": "9876543210"
}
```

---

## 🔄 CRUD Operations Implemented

| Operation | Description |
|------------|-------------|
| Create | Add new student records |
| Read | View all stored records |
| Update | Modify student details |
| Delete | Remove records with confirmation |
| Search | Multi-field search functionality |

---

## 🚀 How to Run the Project

### 1️⃣ Install Required Libraries
```bash
pip install pymongo
```

### 2️⃣ Make Sure MongoDB is Running
Start MongoDB service on your system.

### 3️⃣ Clone the Repository
```bash
git clone <your-github-repository-link>
```

### 4️⃣ Run the Application
```bash
python login.py
```

---
<img width="1919" height="1026" alt="image" src="https://github.com/user-attachments/assets/b17bbddc-b3d1-4cf3-b6bc-85dce0b1376e" />


## 📂 Project Structure

```
Student-Management-System/
│
├── login.py
├── dashboard.py
├── database.py
├── validation.py
├── export_csv.py
├── README.md
```

---

## 🎯 Learning Outcomes

- Understanding MongoDB integration using PyMongo
- Designing GUI applications using Tkinter
- Implementing CRUD operations
- Applying input validation
- Managing real-world database systems

---

## 📌 Future Enhancements

- Role-based access control
- Pagination system
- Data visualization dashboard
- Password encryption
- Deployment using Flask (Web Version)

---

## 👨‍💻 Developed By

**Smruti Ganesh Lohar - 421**  
MSc IT Student  
Guru Nanak Khalsa College  

---

## 📜 License

This project is developed for educational purposes.
