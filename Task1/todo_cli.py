from pathlib import Path


DATA_FILE = Path(__file__).with_name("tasks.txt")


def load_tasks() -> list[str]:
    if not DATA_FILE.exists():
        return []
    return [line.strip() for line in DATA_FILE.read_text(encoding="utf-8").splitlines() if line.strip()]


def save_tasks(tasks: list[str]) -> None:
    DATA_FILE.write_text("\n".join(tasks), encoding="utf-8")


def show_menu() -> None:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")


def view_tasks(tasks: list[str]) -> None:
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task(tasks: list[str]) -> None:
    task = input("Enter new task: ").strip()
    if not task:
        print("Task cannot be empty.")
        return

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def update_task(tasks: list[str]) -> None:
    if not tasks:
        print("No tasks available to update.")
        return

    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to update: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if not 1 <= task_number <= len(tasks):
        print("Invalid task number.")
        return

    updated_task = input("Enter updated task: ").strip()
    if not updated_task:
        print("Task cannot be empty.")
        return

    tasks[task_number - 1] = updated_task
    save_tasks(tasks)
    print("Task updated successfully.")


def delete_task(tasks: list[str]) -> None:
    if not tasks:
        print("No tasks available to delete.")
        return

    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if not 1 <= task_number <= len(tasks):
        print("Invalid task number.")
        return

    removed_task = tasks.pop(task_number - 1)
    save_tasks(tasks)
    print(f"Removed task: {removed_task}")


def main() -> None:
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")


if __name__ == "__main__":
    main()
