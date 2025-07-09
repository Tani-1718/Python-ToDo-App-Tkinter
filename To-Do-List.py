import tkinter as tk  # for designing GUI
from tkinter import messagebox
from tkinter import *
from tkinter import ttk  #this is used for dropdown menu

import time
from datetime import datetime

import os #this is used for file handling

from datetime import datetime









root = Tk()
root.geometry("1000x1000")
root.config(bg = "#1e1e1e")
root.title("To-Do-List")

############################ entry frame ###########################################

f1 = Frame(root)
Label1 = Label(f1 , text = "username")
Label2 = Label(f1 , text = "password")
entry1 = Entry(f1)
entry2 = Entry(f1 , show="*")
Label1.grid(row=1 , column=1 , padx=7 , pady=7)
entry1.grid(row=1 , column=2 , padx=7 , pady=7)
Label2.grid(row=2 , column=1 , padx=7 , pady=7)
entry2.grid(row=2 , column=2 , padx=7 , pady=7)
f1.place(relx= 0.5 , rely = 0.5 , anchor = CENTER)
button1 = Button(f1 , text = "LOGIN" , command= lambda:getValue())
button1.grid(row = 3 ,columnspan=3 , padx=7 , pady=7)

############### to do frame ##################################

f2 = Frame(root , bg = '#1e1e1e')
clock_label = Label(f2 , bg="#1e1e1e", fg="#00ffcc", font=("Segoe UI", 10, "bold"))
clock_label.grid(row = 0 , column=0 , sticky="w" , padx = 10 , pady=5)

def update_clock():
    time_string = time.strftime("%a %d %b %Y | %I:%M:%S:%p")
    clock_label.config(text = time_string)
    root.after(1000 , update_clock)


theme_var = StringVar(value="dark")

def toggle_theme():
    if theme_var.get() == "dark":
        root.config(bg= "white")
        f2.config(bg= "white")
        task_listbox.config(bg = "white", fg="black", selectbackground="#ccc")
        add_button.config(bg="#2196F3", fg="white")
        delete_button.config(bg="#f44336", fg="white")
        clear_button.config(bg="gray", fg="white")
        theme_button.config(bg="white", fg="black")
        clock_label.config(bg="white", fg="#004d99")

    else:
        root.config(bg="#1e1e1e")
        task_listbox.config(bg="#2e2e2e", fg="white", selectbackground="#444")
        add_button.config(bg="#4CAF50", fg="white")
        delete_button.config(bg="#F44336", fg="white")
        clear_button.config(bg="#666", fg="white")
        theme_button.config(bg="#1e1e1e", fg="white")
        clock_label.config(bg="#1e1e1e", fg="#00ffcc")

theme_button = Checkbutton(f2 , text = " 🌙 Dark Mode" , variable=theme_var , onvalue="light" , offvalue="dark",
                           command= toggle_theme , bg="#1e1e1e", fg="white", font=("Segoe UI", 10))
theme_button.grid(row=0 , column= 1 , sticky= "e" , padx=10 )








task_entry = tk.Entry(f2 , width = 50 , font= ("Segoe UI" , 12))
task_entry.grid(row = 1 , column=0 , columnspan=2 , padx=  10 , pady=10)




tasks = []

def add_tasks():
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END , task)
        task_entry.delete(0 , tk.END)
        save_tasks()
    else:
        messagebox.showerror("error" , "task can not be empty")

def delete_tasks():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        task_listbox.delete(index)
        tasks.pop(index)
        save_tasks()
    else:
        messagebox.showerror("error" , "plz select a task to ve deleted")

def clear_tasks():
    if messagebox.askyesno("CLEAR ALL!! , are you sure you want to delete all tasks?"):
        task_listbox.delete(0,tk.END)
        tasks.clear()
        save_tasks()

def toggle_complete(event):
    index = task_listbox.curselection()
    if index:
        i = index[0]
        current = tasks[i]
        if "[✔]" in current:
            updated = current.replace("[✔] ", "")
        else:
            updated = "[✔] " + current
        tasks[i] = updated
        task_listbox.delete(i)
        task_listbox.insert(i, updated)
        task_listbox.select_set(i)
        save_tasks()

task_listbox = tk.Listbox(f2, width=60, height=15, font=("Segoe UI", 11),
                          bg="#2e2e2e", fg="white", selectbackground="#444")
task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
task_listbox.bind("<Double-Button-1>", toggle_complete)

############################################### BUTTONS ########################################
add_button = tk.Button(f2, text="➕ Add Task", command=add_tasks, bg="#4CAF50", fg="white", font=("Segoe UI", 11), width=20)
add_button.grid(row=3, column=0, pady=5)

delete_button = tk.Button(f2, text="❌ Delete Task", command=delete_tasks, bg="#F44336", fg="white", font=("Segoe UI", 11), width=20)
delete_button.grid(row=3, column=1, pady=5)

clear_button = tk.Button(f2, text="🧼 Clear All", command=clear_tasks, bg="#666", fg="white", font=("Segoe UI", 11), width=42)
clear_button.grid(row=4, column=0, columnspan=2, pady=10)

##################################### HELPER FUNCTION ######################################################
def save_tasks():
    with open("tasks.txt" , "w") as f:
        for task in tasks:
            f.write(task +"\n")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt" , "r+") as f:
            for line in f:
                task = line.strip()
                if task:
                    tasks.append(task)
                    task_listbox.insert(tk.END , task)

def getValue():
    user = entry1.get()
    pwd = entry2.get()
    print("your username : ", user, " and password : ", pwd , " is now saved.")
    if not user or not pwd:
        messagebox.showwarning(title="error found" , message= "nothing can be empty")
    else:
        print(f"Username : {user} , Password : {pwd} - logged in")
        show_to_do()
    
def show_to_do():
    f1.place_forget()
    f2.place(relx=0.5  ,rely=0.5 , anchor= CENTER)


load_tasks()
root.mainloop()










