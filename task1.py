import tkinter as tk
from tkinter import messagebox

def add_task():
    t = task_entry.get()
    if t:
        tasks_listbox.insert(tk.END, t)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task must be entered.")

def update_task():
    try:
        i = tasks_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task:
            tasks_listbox.delete(i)
            tasks_listbox.insert(i, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task must be entered.")
    except IndexError:
        messagebox.showwarning("Warning", "A task must be selected to update.")

def delete_task():
    try:
        i = tasks_listbox.curselection()[0]
        tasks_listbox.delete(i)
    except IndexError:
        messagebox.showwarning("Warning", "A task must be selected for deletion.")

# Initialize the main window
root = tk.Tk()
root.title("To-Do List")

tasks_listbox = tk.Listbox(root, width=50, height=15)
tasks_listbox.pack(pady=20)

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

add_task_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_task_button.pack(side=tk.LEFT, padx=10)

update_task_button = tk.Button(button_frame, text="Update Task", command=update_task)
update_task_button.pack(side=tk.LEFT, padx=10)

delete_task_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_task_button.pack(side=tk.LEFT, padx=10)


root.mainloop()
