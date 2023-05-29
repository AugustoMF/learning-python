print("Welcome to the Hours calculator, let's start!")

hours = 168

activities = {}

try:
     while True:
          atv = input("Insert an activity (Or type 'done' to finish): ")

          if atv.lower() == 'done':
           break

          hoursAtv = float(input("Insert the hours spent on {}: ".format(atv)))
          activities[atv] = hoursAtv

     totalHours = sum(activities.values())

except ValueError:
    print ("something went wrong, restart the program!")

if totalHours > hours:
    print("You reached the maximum of hours (168), please restart the program")
    quit()

for atv, hours in activities.items():
    percentage = (hours / totalHours) * 100
    print("{}: {:.2f}%".format(atv, percentage))
