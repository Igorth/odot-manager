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

        self.add_button = tk.Button(root, text="Add Task")
        self.add_button.grid(row=2, column=1)

        self.listbox = tk.Listbox(root)
        self.listbox.grid(row=3, column=0, columnspan=2)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
