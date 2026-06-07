class studentss:
    def __init__(self,id,name,rollno,course,sem,cgpa):
        self.id = id
        self.name = name
        self.rollno = rollno
        self.course = course
        self.sem = sem
        self.cgpa = cgpa

    def display(self):
        print(f"STUDENT ID: {self.id}")
        print(f"STUDENT NAME: {self.name}")
        print(f"STUDENT ROLL NUMBER: {self.rollno}")
        print(f"STUDENT COURSE: {self.course}")
        print(f"STUDENT SEMESTER: {self.sem}")
        print(f"STUDENT CGPA: {self.cgpa}")
        print("------------------------------")


class office:
    def __init__(self):
        self.studentss = []

    def add_info(self):
        id = int(input("ENTER STUDENT ID "))
        name = input("ENTER STUDENT NAME ")
        rollno = int(input("ENTER STUDENT ROLL NUMBER "))
        course = input("ENTER STUDENTS COURSE ")
        sem = input("ENTER SEMESTER ")
        cgpa = input("ENTER CGPA ")

        std = studentss(id,name,rollno,course,sem,cgpa)
        self.studentss.append(std)

        print("YOUR IFORMATION IS ADDED SUCCESFULLY")

    def display(self):
        if not self.studentss:
            print("NO RECORD IS FOUND")
            return

        for studentss in self.studentss:
            studentss.display()

    def search_students(self):
        sid = int(input("ENTER STUDENT ID "))

        for studentss in self.studentss:
            if studentss.id == sid:
                print(f"STUDENT IS FOUND WITH THIS STUDENT ID {sid}")
                studentss.display()
                return

        print("RECORD IS NOT FOUND")

    def update_student(self):
        sid = int(input("ENTER STUDENT ID "))

        for student in self.studentss:
            if student.id == sid:
                student.id = int(input("ENTER STUDENT ID "))
                student.name = input("ENTER STUDENT NAME ")
                student.rollno = int(input("ENTET STUDENT ROLL NUMBER "))
                student.course = input("ENTER STUDENT COURSE ")
                student.sem = input("ENTER SEMESTET ")
                student.cgpa = input("ENTER CGPA ")

                print(f"YOUR RECORD IS UPDATED ON THIS STUDENT ID {sid}")
                return

        print("RECORD IS NOT FOUND")

    def delete(self):
        sid = int(input("ENTER STUDENT ID "))

        for student in self.studentss:
            if student.id == sid:
                Warn = int(input(f"ARE YOU SURE TO DELETE THE RECORD OF {sid} THIS ID. PRESS 0 FOR YES "))

                if Warn == 0:
                    self.studentss.remove(student)
                    print(f"RECORD IS DELETED OF THIS ID {sid}")
                    return

        print("RECORD IS NOT FOUND")


me = office()

while True:
    print("\n======= STUDENT DATA =======")
    print("1. ADD STUDENT RECORD")
    print("2. DISPLAY STUDENT RECORD")
    print("3. SEARCH STUDENT RECORD")
    print("4. UPDATE STUDENT RECORD")
    print("5. DELETE STUDENT RECORD")
    print("6. EXIT")

    choice = input("ENTER YOUR CHOICE ")

    if choice == "1":
        me.add_info()

    elif choice == "2":
        me.display()

    elif choice == "3":
        me.search_students()

    elif choice == "4":
        me.update_student()

    elif choice == "5":
        me.delete()

    elif choice == "6":
        print("EXITINGGG...!!")
        break

    else:
        print("SORRY, INVALID CHOICE. TRY AGAIN")