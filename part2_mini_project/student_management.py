filename = "students.txt"

def load_students():
    s_list = []
    try:
        f = open(filename, "r")
        for line in f:
            line = line.strip()
            if line != "":
                data = line.split(",")
                name = data[0]
                roll = data[1]
                marks = []
                for x in data[2:]:
                    marks.append(float(x))
                student = {"name": name, "roll": roll, "marks": marks}
                s_list.append(student)
        f.close()
    except FileNotFoundError:
        pass
    return s_list


def save_students(s_list):
    f = open(filename, "w")
    for s in s_list:
        m_str = ""
        for m in s["marks"]:
            m_str = m_str + "," + str(m)
        f.write(s["name"] + "," + s["roll"] + m_str + "\n")
    f.close()


def add_student(s_list):
    print("\nADD STUDENT")
    name = input("Enter name: ")
    roll = input("Enter roll no: ")
    
    marks = []
    try:
        n = int(input("Enter number of subjects: "))
        for i in range(n):
            m = float(input("Enter marks for subject " + str(i + 1) + ": "))
            marks.append(m)
    except ValueError:
        print("Wrong input! Enter numbers only.")
        return

    s = {"name": name, "roll": roll, "marks": marks}
    s_list.append(s)
    save_students(s_list)
    print("Student added!")


def view_students(s_list):
    print("\n STUDENT LIST")
    if len(s_list) == 0:
        print("No records found.")
        return
    
    for s in s_list:
        print("Roll No:", s["roll"], "| Name:", s["name"], "| Marks:", s["marks"])


def search_student(s_list):
    print("\n SEARCH STUDENT")
    r = input("Enter roll no to search: ")
    found = False
    for s in s_list:
        if s["roll"] == r:
            print("Record found -> Name:", s["name"], ", Marks:", s["marks"])
            found = True
            break
    if not found:
        print("Student not found.")


def calc_average(s_list):
    print("\n CALCULATE AVERAGE")
    r = input("Enter roll no: ")
    for s in s_list:
        if s["roll"] == r:
            total = 0
            for m in s["marks"]:
                total = total + m
            avg = total / len(s["marks"])
            print("Average marks of", s["name"], "=", round(avg, 2))
            return
    print("Student not found.")



students = load_students()

while True:
    print("\n1. ADD STUDENT")
    print("2. VIEW ALL STUDENTS")
    print("3. SEARCH STUDENT BY ROLL NUMBER")
    print("4. CALCULATE AVERAGE MARKS")
    print("5. EXIT")
    
    ch = input("Enter choice (1-5): ")
    
    if ch == "1":
        add_student(students)
    elif ch == "2":
        view_students(students)
    elif ch == "3":
        search_student(students)
    elif ch == "4":
        calc_average(students)
    elif ch == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again.")
        