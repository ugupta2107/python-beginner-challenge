f = open("sample.txt", "w")
f.write("GDG TASK 2.\n")
f.close()

f = open("sample.txt", "r")
text = f.read()
print("File content:")
print(text)
f.close()


name = input("\nEnter student name: ")
marks = input("Enter student marks: ")

f = open("student_data.txt", "w")
f.write("Name: " + name + "\n")
f.write("Marks: " + marks + "\n")
f.close()

f = open("student_data.txt", "r")
print("\nSaved student data:")
print(f.read())
f.close()


try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Error: That is not a valid number!")


filename = "missing_file.txt"
try:
    f = open(filename, "r")
    content = f.read()
    f.close()
    
    if content.strip() == "":
        print("\nThe file is empty.")
    else:
        print("\nFile data:", content)
except FileNotFoundError:
    print("\nError: The file does not exist.")