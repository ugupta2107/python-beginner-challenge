for i in range(1, 101):
    print(i)

print("\nPrime numbers between 1 and 100:")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
print()


n = int(input("\nEnter a number for multiplication table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
    

n = int(input("\nEnter N to find sum from 1 to N: "))
s = 0
for i in range(1, n + 1):
    s += i
print(f"Sum from 1 to {n} is: {s}")


word = input("\nEnter a word: ")
vowels = "aeiouAEIOU"
count = 0

for char in word:
    if char in vowels:
        count += 1

print("Number of vowels:", count)





