tasks = []

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
            name = input("Enter task name: ")
            tasks.append({"name": name, "done": False})
            print(f"Task '{name}' added!")

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
