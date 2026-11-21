def largest_number(a, b, c):
    return max(a, b, c)
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
print("Largest number is:", largest_number(n1, n2, n3))


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter an integer to check if it is prime: "))
if is_prime(num):
    print(f"{num} is a Prime number.")
else:
    print(f"{num} is NOT a Prime number.")


def average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)

print("Average marks:", average([45, 50, 98, 72, 68]))




def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Cannot divide by zero"

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
opeartor = input("Enter operator (+, -, *, /): ")
if opeartor  == "+":
    print("Result:", add(x, y))
elif opeartor  == "-":
    print("Result:", subtract(x, y))
elif opeartor == "*":
    print("Result:", multiply(x, y))
elif opeartor == "/":
    print("Result:", divide(x, y))
else:
    print("Invalid operator.")