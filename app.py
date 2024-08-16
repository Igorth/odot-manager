import tkinter as tk
from tkinter import messagebox
from task_manager import TaskManager
from task import Task


class TaskManagerApp:
    def __init__(self, root):
        self.manager = TaskManager()
        # self.manager.load_from_json()
        self.root = root
        self.root.title("Odot Manager")

        # Interface layout
        self.title_label = tk.Label(root, text="Title:")
        self.title_label.grid(row=0, column=0)
        self.title_entry = tk.Entry(root)
        self.title_entry.grid(row=0, column=1)

        self.description_label = tk.Label(root, text="Description:")
        self.description_label.grid(row=1, column=0)
        self.description_entry = tk.Entry(root)
        self.description_entry.grid(row=1, column=1)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=2, column=1)

        self.listbox = tk.Listbox(root)
        self.listbox.grid(row=3, column=0, columnspan=2)
        self.listbox.bind("<Double-Button-1>", self.mark_as_completed)

        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        self.edit_button.grid(row=4, column=0)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=4, column=1)

        self.update_list()

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()

        if title:
            try:
                new_task = Task(title, description)
                self.manager.add_task(new_task)
                self.manager.save_to_json()
                self.update_list()
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter a title.")

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for task_dict in self.manager.list_tasks():
            status = "Completed" if task_dict["completed"] else "Incomplete"
            self.listbox.insert(tk.END, f"{task_dict['title']} - {status}: {task_dict['description']}")

    def edit_task(self):
        selected_task = self.listbox.get(tk.ACTIVE)
        if selected_task:
            title = selected_task.split(" - ")[0]
            new_title = self.title_entry.get()
            new_description = self.description_entry.get()

            if title in self.manager.tasks:
                task = self.manager.tasks[title]
                task.edit(new_title, new_description)
                self.manager.save_to_json()
                self.update_list()
            else:
                messagebox.showerror("Error", "Task not found.")

    def delete_task(self):
        selected_task = self.listbox.get(tk.ACTIVE)
        if selected_task:
            title = selected_task.split(" - ")[0]
            try:
                self.manager.delete_task(title)
                self.manager.save_to_json()
                self.update_list()
            except KeyError as e:
                messagebox.showerror("Error", str(e))

    def mark_as_completed(self, event):
        selected_task = self.listbox.get(tk.ACTIVE)
        if selected_task:
            title = selected_task.split(" - ")[0]
            if title in self.manager.tasks:
                task = self.manager.tasks[title]
                task.mark_as_completed()
                self.manager.save_to_json()
                self.update_list()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
