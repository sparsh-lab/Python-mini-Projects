'''
what our app will do:
✅ Add tasks
✅ Remove tasks
✅ Save tasks
✅ Load tasks
'''

import tkinter as tk

# create main window
root = tk.Tk() 
root.title("TO DO LIST") # set title
root.geometry("400x500") # set size


# creat an entry box for user input
task_entry = tk.Entry(root, width=50) # width define how long will text field will
task_entry.pack(pady=20) # add padding for spacing

# create a listbox to add tasks
task_list = tk.Listbox(root, width=60, height=10)
task_list.pack(pady=20)

# create vertical scroll bar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_list.yview)

# function to add task
def add_task():
    task = task_entry.get() # get task from entry box
    if task !=" ": # only add if entry box is not empty
        task_list.insert(tk.END, task) # insert task at the end of listbox
        task_entry.delete(0, tk.END) # clear entry box after adding

# function to delete task
def delete_task():
    try:
        selected_task = task_list.curselection()[0] # get selected index
        task_list.delete(selected_task) # delete the task at the index
    except IndexError:
        pass # do nothing if no task is selected 

# function to mark tasks as completed
def mark_completed():
    try:
        selected_task = task_list.curselection()[0] # get selected index
        task = task_list.get(selected_task) #get task text
        if not task.startswith("✔ "): # prevent double marking
            task_list.delete(selected_task)
            task_list.insert(selected_task, "✔ " + task)  # Add checkmark
    except IndexError:
        pass  # Do nothing if no task is selected


# function to clear all task.
def clear_all():
    task_list.delete(0, tk.END)

# function to save all task to a file
def save_task():
    with open("tasks.txt", "w") as file: # open file in open mode
        task = task_list.get(0, tk.END) # get all task form task list
        for t in task:
            file.write(task + "\n") # write each task on new line

# funciton to load tasks from a file
def load_task():
    try:
        with open("tasks.txt", "r") as file: # open file in read mode
            tasks = file.readlines() # read all lines
            for task in task:
                task_list.insert(tk.END, task.strip()) # add each task to list box
    except FileNotFoundError:
        pass # if file does't exist do nothing


# call load task when app starts
load_task()


# create a "add task" button
add_button = tk.Button(root, text="add task", command=add_task)
add_button.pack(pady=10)

# create a delete task button
delete_button = tk.Button(root, text="Delete task", command=delete_task)
delete_button.pack(pady=10)

# Create "Mark as Completed" button
complete_button = tk.Button(root, text="Mark as Completed", command=mark_completed)
complete_button.pack(pady=5)

# create clear all task button
clear_button = tk.Button(root, text="clear all", command=clear_all)
clear_button.pack(pady=10)

#create a save button
save_button = tk.Button(root, text="save tasks", command=save_task)
save_button.pack(pady=10)


root.mainloop() # it will run the window until user want to close it.


