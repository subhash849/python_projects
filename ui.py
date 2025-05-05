import tkinter as tk
from code import TaskManager  # Import the TaskManager class

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.task_manager = TaskManager()

        # Create UI components
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.task_entry = tk.Entry(root, width=52)
        self.task_entry.pack(pady=5)

        tk.Button(root, text="Add Task", command=self.add_task).pack(pady=5)
        tk.Button(root, text="Delete Task", command=self.delete_task).pack(pady=5)

        self.load_tasks()  # Load existing tasks

    def load_tasks(self):
        """Load tasks from TaskManager into the listbox."""
        self.task_listbox.delete(0, tk.END)  # Clear the listbox
        for task in self.task_manager.get_tasks():
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        """Add a new task."""
        task = self.task_entry.get()
        if task:
            self.task_manager.add_task(task)
            self.task_entry.delete(0, tk.END)  # Clear input
            self.load_tasks()  # Refresh listbox

    def delete_task(self):
        """Delete the selected task."""
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_manager.delete_task(selected_index[0])
            self.load_tasks()  # Refresh listbox

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()