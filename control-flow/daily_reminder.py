task = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match task_priority:

        case 'high':
            message = "is a high priority task that requires immediate attention today!"

        case 'medium':
            message = "is a medium priority task, do it not lather than tomorrow"

        case 'low':
            message = "is a low priority task. Consider completing it when you have free time."

        case _:
            print("Invalid priority")
            

if time_bound == 'yes':
        print(f"Reminder: '{task}' {message}")


elif time_bound == 'no':
        print(f"Note: '{task}' {message}")

else:
        print("Invalid time_bound")
