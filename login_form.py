import tkinter as tk
from tkinter import messagebox

def login_Form():
    user = entry_username.get()
    password = entry_password.get()

    if user == "student" and password == "1234":
        messagebox.showinfo("Log in successfully","Welcome to admin")
        getInfo()
        root.withdraw()
    else:
        messagebox.showerror("Login Failed","Invalid username or password")

def getInfo():
    info_root = tk.Toplevel(root)
    info_root.title("User Form")
    info_root.geometry("400x300")

    label_name = tk.Label(info_root, text="Name:", font=("Arial", 10))  
    label_name.pack(pady=10)
    name_user = tk.Entry(info_root, width=30)  
    name_user.pack(pady=10)

    label_age = tk.Label(info_root, text="AGE:", font=("Arial", 10))  
    label_age.pack(pady=10)
    age_user = tk.Entry(info_root, width=30) 
    age_user.pack(pady=10)

    label_address = tk.Label(info_root, text="ADDRESS:", font=("Arial", 10))  
    label_address.pack(pady=10)
    address_user = tk.Entry(info_root, width=30)  
    address_user.pack(pady=10)

    def return_to_login():
        name = name_user.get()
        age = age_user.get()
        address = address_user.get()

        messagebox.showinfo("Form Submitted", f"Name: {name}\nAge: {age}\nAddress: {address}") 

        info_root.destroy()
        root.deiconify()

    return_button = tk.Button(info_root, text="submit", command=return_to_login)
    return_button.pack(pady=10)    

root = tk.Tk()
root.title("Login Form")
root.geometry("400x300")

label = tk.Label(root,text="Username", font=("Arial",10))
label.pack(pady=10)
entry_username = tk.Entry(root,width=30)
entry_username.pack(pady=10)

label = tk.Label(root,text="Password", font=("Arial",10))
label.pack(pady=10)
entry_password = tk.Entry(root,width=30,show="*")
entry_password.pack(pady=10)

submit_button = tk.Button(root,text="login" ,width=10, command=login_Form)
submit_button.pack(pady=10)




root.mainloop()