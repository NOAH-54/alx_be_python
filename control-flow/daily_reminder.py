task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case 'high':
        # you can have custom behavior here if you want
        pass
    case 'medium':
        pass
    case 'low':
        pass
    case _:
        print("Invalid priority entered.")
        exit()

if time_bound == 'yes':
    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
