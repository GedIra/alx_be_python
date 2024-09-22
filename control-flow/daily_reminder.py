task = input("Input task description: ")
task_priority = input("task priority(high, medium, low): ").lower()
time_bound = input("Is the task time bound ? (yes/no): ").lower()

while True:

    match task_priority:

        case 'high':
            message = "is a high priority task that requires immediate attention today!"
            break

        case 'medium':
            message = "is a medium priority task, do it not lather than tomorrow"
            break

        case 'low':
            message = "is a low priority task. Consider completing it when you have free time."
            break

        case _:
            print("Invalid priority")
            break

    if time_bound == 'yes':
        print("Reminder:", task, message)
        break


    elif time_bound == 'no':
        print("Note:", task, message)
        break

    else:
        print("Invalid time_bound")
        break
