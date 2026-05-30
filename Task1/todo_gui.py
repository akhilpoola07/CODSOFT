import tkinter as tk
from pathlib import Path
from tkinter import messagebox


DATA_FILE = Path(__file__).with_name("tasks.txt")


class TodoApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("460x520")
        self.root.resizable(False, False)
        self.tasks: list[str] = []

        self.build_ui()
        self.load_tasks()

    def build_ui(self) -> None:
        title = tk.Label(
            self.root,
            text="To-Do List",
            font=("Arial", 20, "bold"),
            fg="#1f3c88",
        )
        title.pack(pady=15)

        subtitle = tk.Label(
            self.root,
            text="Add, update, and manage your daily tasks",
            font=("Arial", 10),
            fg="#555555",
        )
        subtitle.pack(pady=(0, 15))

        input_frame = tk.Frame(self.root)
        input_frame.pack(padx=20, fill="x")

        self.task_entry = tk.Entry(input_frame, font=("Arial", 12))
        self.task_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        add_button = tk.Button(
            input_frame,
            text="Add Task",
            width=12,
            bg="#1f7a8c",
            fg="white",
            command=self.add_task,
        )
        add_button.pack(side="right")

        list_frame = tk.Frame(self.root)
        list_frame.pack(padx=20, pady=20, fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(
            list_frame,
            height=14,
            font=("Arial", 12),
            selectbackground="#86bbd8",
            activestyle="none",
        )
        self.listbox.pack(side="left", fill="both", expand=True)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        button_frame = tk.Frame(self.root)
        button_frame.pack(padx=20, pady=(0, 20), fill="x")

        update_button = tk.Button(
            button_frame,
            text="Update Selected",
            bg="#f4a261",
            fg="white",
            command=self.update_task,
        )
        update_button.pack(side="left", expand=True, fill="x", padx=(0, 8))

        delete_button = tk.Button(
            button_frame,
            text="Delete Selected",
            bg="#d62828",
            fg="white",
            command=self.delete_task,
        )
        delete_button.pack(side="left", expand=True, fill="x", padx=8)

        clear_button = tk.Button(
            button_frame,
            text="Clear All",
            bg="#6c757d",
            fg="white",
            command=self.clear_tasks,
        )
        clear_button.pack(side="left", expand=True, fill="x", padx=(8, 0))

    def load_tasks(self) -> None:
        if not DATA_FILE.exists():
            return

        for line in DATA_FILE.read_text(encoding="utf-8").splitlines():
            task = line.strip()
            if task:
                self.tasks.append(task)
                self.listbox.insert(tk.END, task)

    def save_tasks(self) -> None:
        DATA_FILE.write_text("\n".join(self.tasks), encoding="utf-8")

    def add_task(self) -> None:
        task = self.task_entry.get().strip()
        if not task:
            messagebox.showwarning("Missing Task", "Please enter a task first.")
            return

        self.tasks.append(task)
        self.listbox.insert(tk.END, task)
        self.task_entry.delete(0, tk.END)
        self.save_tasks()

    def update_task(self) -> None:
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a task to update.")
            return

        updated_task = self.task_entry.get().strip()
        if not updated_task:
            messagebox.showwarning("Missing Task", "Please enter the updated task.")
            return

        index = selection[0]
        self.tasks[index] = updated_task
        self.listbox.delete(index)
        self.listbox.insert(index, updated_task)
        self.listbox.selection_set(index)
        self.task_entry.delete(0, tk.END)
        self.save_tasks()

    def delete_task(self) -> None:
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a task to delete.")
            return

        index = selection[0]
        self.listbox.delete(index)
        self.tasks.pop(index)
        self.save_tasks()

    def clear_tasks(self) -> None:
        if not self.tasks:
            messagebox.showinfo("Nothing to Clear", "Your task list is already empty.")
            return

        confirmed = messagebox.askyesno(
            "Clear All Tasks",
            "Are you sure you want to remove all tasks?",
        )
        if not confirmed:
            return

        self.tasks.clear()
        self.listbox.delete(0, tk.END)
        self.save_tasks()


def main() -> None:
    root = tk.Tk()
    TodoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
