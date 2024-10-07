import os
from student import StudentInfo
from adds_student import AddStudent
from open_studAcc import openACc
from student_search import SearchStud

stu = StudentInfo()
stu1 = StudentInfo()
studAcc = openACc(stu)
addstud = AddStudent(stu)
search = SearchStud(stu)

#stu.setName('Admin Camacho'), stu.setAge('20'), stu.setIdnum('2023-2-02449'), stu.setEmail('nat@gmail.com'), stu.setPhone('09560252200')
#addstud.add_student(stu.getName(), stu.getAge(), stu.getIdnum(), stu.getEmail(), stu.getPhone())
addstud.add_student("Admin Camacho", "20", "2023-2-02449", "nat@gmail.com", "09560252200")
addstud.add_student("Cruz", "19", "2023-2-02000", "jed@gmail.com", "09560252200")
addstud.add_student('Catli', '20', '2023-2-12345', 'don@gmail.com', '09560252200')
addstud.add_student('Aidan', '19', '2023-2-09876', 'jc@gmail.com', '09560252200')

def main():
    student = None
    for a in range(4):
        os.system("cls")
        idnum = input("\n\nWelcome to student portal!\nEnter student ID number: ")
        student = studAcc.open_studentAcc(idnum)
        if student:
            studportal(student)
        
def studportal(student):
    os.system("cls")
    while True:
        print(f"Welcome, {student.getName()}!\n")
        choice = input("Please choose from the following options\n1. View your Information\n2. View other student's information\n3. Register new student\'s info\n4. View all students in the list\n5. Exit\nEnter choice: ")

        if choice == '1': #your info
            search.searchstud(student.getIdnum())
            again = input("\nContinue? [y/n]\nChoice: ").lower()
            studportal(student.getIdnum()) if again == 'y' else quit()
        
        elif choice == '2': #ibang info
            otherid = input("\nEnter the student\'s id number: ")
            search.searchstud(otherid)
            again = input("\nContinue? [y/n]\nChoice: ").lower()
            studportal(student) if again == 'y' else quit()

        elif choice == '3': #registration
            addstud.new_student()
            again = input("\nContinue? [y/n]\nChoice: ").lower()
            studportal(student) if again == 'y' else quit()

        elif choice == "4": #view all
            search.printAllStudentInfo()
            again = input("\nContinue? [y/n]\nChoice: ").lower()
            studportal(student) if again == 'y' else quit()

        elif choice == '5': #exit na
            print("\nThank you for using.")
            quit()

        else:
            print("Invalid input, please try again."); studportal(stu.getIdnum())

main()