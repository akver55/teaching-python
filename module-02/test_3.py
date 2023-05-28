# User inputs length in meters
# User selects to convert meters into one of the following:
# - miles
# - inches
# - yards
# Print the output

from time import sleep


meters = int(input("Enter length in meters: "))
convert_to = input("To convert to miles enter - 1\nTo convert to inches enter - 2\nTo convert to yards enter - 3\n")

if convert_to != "1" and convert_to != "2" and convert_to != "3":
    print("Sorry, you didn't correct selection from provided...")
    sleep(1)
    exit()

if convert_to == "1":
    miles = meters / 1.609344
    print(f"{meters} meters = {round(miles, 4)} miles")
elif convert_to == "2":
    inches = meters * 39.3701
    print(f"{meters} meters = {round(inches, 2)} inches")
else:
    yards = meters * 1.094
    print(f"{meters} meters = {round(yards, 4)} yards")