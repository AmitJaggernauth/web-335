#Author: Amit Jaggernauth
#Date: 2/14/2026
#Assignment:Hands on 3.1

#List of tasks for the lemonade stand

tasks = [
    "Buy lemons and sugar"
    "Prepare lemonade"
    "Set up the stand"
    "Serve customers"
    "Clean up the Stand"
]

#Print each task using a for loop

print("Lemonade Stand Tasks")
for task in tasks:
    print("-", task)

print("\nWeekly Schedule")

#Lists of days in the week

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#Loop through days and assign tasks

for i in range(len(days)):
    day = days[i]

    if day == "Saturday" or day == "Sunday":
        print(f"{day}: Day off! Time to rest.")
    else:
        print(f"{day}: Today's task is '{task[i % len(tasks)]}'.")