tasks tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task(num):
    if 0 < num <= len(tasks):
        removed = tasks.pop(num - 1)
        print(f"Task '{removed}' removed!")
    else:
        print("Invalid task number!")

while True:
    print("\n1. View tasks\n2. Add task\n3. Remove task\n4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "3":
        num = int(input("Task number to remove: "))
        remove_task(num)
    elif choice == "4":
        break
