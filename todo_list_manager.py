#To-do List Manager CLI
import json

DATA_FILE = "tasks.json"

def load_tasks():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks():
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "Done" if task["done"] else "Pending"
            print(f"{i}. {task['name']} - {status}")

def main():
    while True:
        print("\n1. Add task")
        print("2. Mark task done")
        print("3. View tasks")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter task name: ").strip()
            if not name:
                print("Task name cannot be empty!")
                continue 
            if name.isdigit():
                print("Task name cannot be just numbers!")
                continue
            tasks.append({"name": name, "done": False})
            print(f"Task '{name}' added!")
            save_tasks()

        elif choice == "2":
            if not tasks:
                print("No tasks to mark as done!")
                continue

            show_tasks()
            try:
                num = int(input("Enter task number to mark done: "))
                if 1 <= num <= len(tasks):
                    tasks[num-1]["done"] = True
                    print(f"Task '{tasks[num-1]['name']}' marked as done!")
                    save_tasks()
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "3":
            show_tasks()

        elif choice == "4":
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
