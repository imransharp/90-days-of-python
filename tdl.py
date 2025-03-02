tasks = []  # List to store tasks

while True:
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})  # Store task with completion status

    print(f"\nYour tasks are:")
    for i, t in enumerate(tasks, start=1):
        status = "✅ Completed" if t["completed"] else "❌ Not Completed"
        print(f"{i}. {t['task']} - {status}")

    add_more = input("\nDo you want to enter another task? (yes/no): ").strip().lower()
    if add_more == "no":
        break

while True:
    mark_complete = input("\nDo you want to mark a task as completed? (yes/no): ").strip().lower()
    if mark_complete == "no":
        break
    elif mark_complete == "yes":
        task_number = int(input("Enter task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True  # Mark selected task as completed
        else:
            print("Invalid task number.")

    print("\nUpdated Task List:")
    for i, t in enumerate(tasks, start=1):
        status = "✅ Completed" if t["completed"] else "❌ Not Completed"
        print(f"{i}. {t['task']} - {status}")

print("\nFinal Task List:")
for i, t in enumerate(tasks, start=1):
    status = "✅ Completed" if t["completed"] else "❌ Not Completed"
    print(f"{i}. {t['task']} - {status}")
