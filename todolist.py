def todo_list():
    tasks = []

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a new task: ")
            tasks.append(task)
            print(f"Task '{task}' added.")
        elif choice == '2':
            if tasks:
                print("Your tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks to show.")
        elif choice == '3':
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                task_num = int(input("Enter the number of the task to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Task '{removed_task}' removed.")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks to remove.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

todo_list()
