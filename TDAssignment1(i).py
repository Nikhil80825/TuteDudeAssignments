num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

Addition = float(num1 + num2)
Subtraction = float(num1 - num2)
Multiplication = float(num1 * num2)
Division = float(num1 / num2) if num2 != 0 else "Undefined (cannot divide by zero)"

print("Addition:", Addition)
print("Subtraction:", Subtraction)
print("Multiplication:", Multiplication)
print("Division:", Division)
