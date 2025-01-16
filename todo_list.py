import os

def display_menu():
    print("\n--- To-Do List Application ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Save and Exit")

def load_tasks(file_name="tasks.txt"):
    if not os.path.exists(file_name):
        return []
    with open(file_name, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks, file_name="tasks.txt"):
    with open(file_name, "w") as file:
        file.writelines(f"{task}\n" for task in tasks)

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            if not tasks:
                print("\nNo tasks available.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
        elif choice == "2":
            new_task = input("\nEnter the new task: ").strip()
            if new_task:
                tasks.append(new_task)
                print("Task added successfully!")
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            if not tasks:
                print("\nNo tasks to delete.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                try:
                    task_num = int(input("Enter the task number to delete: ").strip())
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        print(f"Task '{removed_task}' deleted successfully!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
