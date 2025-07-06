task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' has an unknown priority"

if priority in ["high", "medium"] and time_bound == "yes":
    message += " that requires immediate attention today!"
elif priority in ["high", "medium"]:
    message += ". Please plan accordingly."
elif priority == "low" and time_bound == "no":
    message += ". Consider completing it when you have free time."

print(message)
