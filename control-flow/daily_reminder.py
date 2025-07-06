# daily_reminder.py (updated for older Python versions)

# Prompt user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Replace match-case with if-elif-else
if priority == "high":
    reminder = f"Reminder: '{task}' is a high priority task"
elif priority == "medium":
    reminder = f"Reminder: '{task}' is a medium priority task"
elif priority == "low":
    reminder = f"Note: '{task}' is a low priority task"
else:
    reminder = f"Note: '{task}' has an unknown priority level"

# Conditional adjustment based on time sensitivity
if time_bound == "yes":
    if priority in ("high", "medium"):
        reminder += " that requires immediate attention today!"
    else:
        reminder += " that should be completed today."
else:
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += "."

# Print the final reminder
print(reminder)