age = 20
height = 175.2
branch = "AI-DS"
is_learning = True

print(type(age) , age)
print(type(height) , height)
print(type(branch) , branch)
print(type(is_learning) , is_learning)

celsius = float(input("\nEnter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C is equal to {fahrenheit:.4f}°F")


length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area: {area}, Perimeter: {perimeter}")


a, b = 15, 20
print("\nComparison & Logical Examples")
print(f"a == b: {a == b}")
print(f"a < b: {a < b}")
print(f"(a < b) and (b == 20): {(a < b) and (b == 20)}")
print(f"(a > b) or (b == 20): {(a > b) or (b == 20)}")
print(f"not (a == b): {not (a == b)}")



