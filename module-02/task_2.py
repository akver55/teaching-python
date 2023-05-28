# User inputs three numbers
# User chooses to make search either for:
# - biggest number
# - smallest number
# - average value of all numbers
# Output the result

from time import sleep

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))

action_with_numbers = (
    input(
        "For printing biggest number type: 1\nFor printing smallest number type: 2\nFor printing average value of numbers type: 3\n"
    )
)

if action_with_numbers != "1" and action_with_numbers != "2" and action_with_numbers != "3":
    print("Sorry, you didn't choose an action...")
    sleep(1)
    exit()


if action_with_numbers == "1":
    message = " is the biggest number"
    if num_1 > num_2 and num_1 > num_3:
        print(f"{num_1}{message}")
    elif num_2 > num_1 and num_2 > num_3:
        print(f"{num_2}{message}")
    elif num_3 > num_1 and num_3 > num_2:
        print(f"{num_3}{message}")
    else:
        print("There is now single biggest number from numbers provided...")


if action_with_numbers == "2":
    message = " is the smallest number"
    if num_1 < num_2 and num_1 < num_3:
        print(f"{num_1}{message}")
    elif num_2 > num_1 and num_2 > num_3:
        print(f"{num_2}{message}")
    elif num_3 < num_1 and num_3 < num_2:
        print(f"{num_3}{message}")
    else:
        print("There is now single smallest number from numbers provided...")

if action_with_numbers == "3":
    print(int((num_1 + num_2 + num_3) / 3), "is an average value of all three numbers")
