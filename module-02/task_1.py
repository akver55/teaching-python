# User inputs three numbers
# User chooses to perform sum of multiplication of those numbers
# Output the result

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))
operator = str(input("Enter '*' or '+' operator "))

if operator == "*":
    print(num_1 * num_2 * num_3)
elif operator == "+":
    print(num_1 + num_2 + num_3)
else:
    print("Sorry, you've entered not valid {operator} operator...")
