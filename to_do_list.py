"""to_do_list
Original file is located at
    https://colab.research.google.com/drive/1bIn1f-J7ifdF2UNM88e7X8upR1n1UxFY
"""

tasks = []

def show_menu():
    print("\n=== TO-DO LIST APP ===")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1):
            status = "Done" if t["completed"] else "Pending"
            print(f"{i}. {t['task']} — {status}")

def mark_completed():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as completed: "))
        tasks[num - 1]["completed"] = True
        print(f"Task '{tasks[num - 1]['task']}' marked as completed!")
    except:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        print(f"Task '{removed['task']}' deleted!")
    except:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1–5): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye! Have a productive day!")
        break
    else:
        print("Invalid choice, try again.")

