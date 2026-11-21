subjects = ["PPS","TCE", "CODE", "BE", "CLP"]
for sub in subjects:
    print(sub)



marks_list = []
print("\nEnter 5 marks:")
for i in range(5):
    m = float(input(f"Mark {i + 1}: "))
    marks_list.append(m)

print(f"Total: {sum(marks_list)}")
print(f"Average: {sum(marks_list) / len(marks_list):.2f}")
print(f"Highest: {max(marks_list)}")
print(f"Lowest: {min(marks_list)}")


student = {
    "name" : "Utkarsh",
    "roll_number": "26UAD100",
    "marks" : marks_list  
}
print("\n Student Dictionary: " ,student)


names = ["Kritish", "Dhruv", "Aditya", "Aryan", "Utkarsh"]
find_name = input("\n Enter a name to search: ")
if find_name in names:
    print(f"{find_name} exist in the list.")
else:
    print(f"{find_name} not found.")



word = input("\nEnter a word: ")
freq = {}
for ch in word:
    if ch in freq:
        freq[ch] += 1 
    else:
        freq[ch] = 1
print("Character frequencies: ", freq)