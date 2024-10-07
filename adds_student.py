from student import StudentInfo

class AddStudent:
    def __init__(self, student):
        self.student_data = student
    
    def add_student(self, name, age, idnum, email, phone):
        student = StudentInfo()
        student.setName(name)
        student.setAge(age)
        student.setIdnum(idnum)
        student.setEmail(email)
        student.setPhone(phone)
        
        student.getName()
        student.getAge()
        student.getIdnum()
        student.getEmail()
        student.getPhone()

        self.student_data.allstudents.append(student)
        print(f'\nAdded student {name} to the list')
    
    def new_student(self):
        print("\n===ADD NEW STUDENT===")
        newstud = StudentInfo()
        name, age, idnum, email, phone = input("\nEnter Name: "), int(input("Enter Age: ")), input("Enter ID Number: "), input("Enter Email: "), input("Enter Phone Number: ")
        print("\n===NOTHING FOLLOWS===\n")
        newstud.setName(name)
        newstud.setAge(age)
        newstud.setIdnum(idnum)
        newstud.setEmail(email)
        newstud.setPhone(phone)

        newstud.getName()
        newstud.getAge()
        newstud.getIdnum()
        newstud.getEmail()
        newstud.getPhone()

        self.student_data.allstudents.append(newstud)
        print(f'\nAdded student {name} to the list')

    

