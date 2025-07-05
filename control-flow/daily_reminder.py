# daily_reminder.py (compatible with older Python versions)

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if priority == "high":
    reminder = f"Reminder: '{task}' is a high priority task"
elif priority == "medium":
    reminder = f"Reminder: '{task}' is a medium priority task"
elif priority == "low":
    reminder = f"Note: '{task}' is a low priority task"
else:
    reminder = f"Task priority '{priority}' is not recognized."

if time_bound == "yes" and priority in ["high", "medium", "low"]:
    reminder += " that requires immediate attention today!"
elif priority in ["high", "medium", "low"]:
    reminder += ". Consider completing it when you have free time."

print()
print(reminder)
print()
print("Well done on completing this project! Let the world hear about this milestone achieved.")
print("\n🚀 Click here to tweet! 🚀")
