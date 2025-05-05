import csv
import os

class TaskManager:
    def __init__(self, filename='tasks.csv'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the CSV file into the task list."""
        if os.path.exists(self.filename):
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.tasks.append(row[0])

    def add_task(self, task):
        """Add a new task to the list and save it to the CSV file."""
        self.tasks.append(task)
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([task])

    def delete_task(self, index):
        """Delete a task by its index."""
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def save_tasks(self):
        """Save all tasks back to the CSV file."""
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for task in self.tasks:
                writer.writerow([task])

    def get_tasks(self):
        """Return the current list of tasks."""
        return self.tasks

# Example usage:
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Buy groceries")
    manager.add_task("Read a book")
    print("Current tasks:", manager.get_tasks())
    manager.delete_task(0)
    print("Tasks after deletion:", manager.get_tasks())