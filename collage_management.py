import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="your_database"
)
cursor = db.cursor()

# Create users table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users
             (id INT AUTO_INCREMENT PRIMARY KEY,
              username VARCHAR(255) NOT NULL,
              fullname VARCHAR(255) NOT NULL,
              email VARCHAR(255) NOT NULL,
              password VARCHAR(255) NOT NULL)''')
db.commit()

def signup():
    username = username_entry.get()
    fullname = fullname_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    query = "INSERT INTO users (username, fullname, email, password) VALUES (%s, %s, %s, %s)"
    values = (username, fullname, email, password)
    cursor.execute(query, values)
    db.commit()
    messagebox.showinfo("Success", "Signup successful")

def login():
    username = login_username_entry.get()
    password = login_password_entry.get()

    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    values = (username, password)
    cursor.execute(query, values)
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Success", "Login successful")
    else:
        messagebox.showerror("Error", "Invalid username or password")

root = tk.Tk()
root.title("Login / Signup")

# ... Widget definitions as before ...

def close_app():
    db.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", close_app)
root.mainloop()
