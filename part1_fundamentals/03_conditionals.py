num = int(input("Enter an integer: "))
if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")


marks = float(input("\nEnter marks (0-100): "))
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"
print(f"Grade: {grade}")


year = int(input("\nEnter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is NOT a Leap Year.")
    

x = float(input("\nEnter first number: "))
y = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    print(f"Result: {x + y}")
elif operator == "-":
    print(f"Result: {x - y}")
elif operator == "*":
    print(f"Result: {x * y}")
elif operator == "/":
    print(f"Result: {x / y}" if y != 0 else "Error")
else:
    print("Invalid operator")    