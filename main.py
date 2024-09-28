import os
from student import StudentInfo
from adds_student import AddStudent
from open_studAcc import openACc
from student_search import SearchStud
from all_studentprint import allprint

stu = StudentInfo()
studAcc = openACc(stu)
addstud = AddStudent(stu)
search = SearchStud(stu)
printallstud = allprint(stu)

stu.setName('Camacho'), stu.setAge('20'), stu.setIdnum('2023-2-02449'), stu.setEmail('nat@gmail.com'), stu.setPhone('09560252200')
addstud.add_student(stu.getName(), stu.getAge(), stu.getIdnum(), stu.getEmail(), stu.getPhone())

def main():
    os.system("cls")
    idnum = input("\n\nWelcome to Admin portal!\nEnter admin ID number: ")
    if studAcc.open_studentAcc(idnum):
        studportal(idnum)
    else:
        main()

def studportal(idnum):
    os.system("cls")
    print(f"Welcome, Admin {stu.getName()}!\n")
    choice = input("Please choose from the following options\n1. View your Information\n2. View other student's information\n3. Register new student\'s info\n4. View all students in the list\n5. Exit\nEnter choice: ")

    if choice == '1': #your info
        search.searchstud(stu.getIdnum())
        again = input("\nContinue? [y/n]\nChoice: ").lower()
        studportal(stu.getIdnum()) if again == 'y' else print("\nThank you for using.")
    
    elif choice == '2': #ibang info
        otherid = input("\nEnter the student\'s id number: ")
        search.searchstud(otherid)
        again = input("\nContinue? [y/n]\nChoice: ").lower()
        studportal(stu.getIdnum()) if again == 'y' else print("\nThank you for using.")

    elif choice == '3': #registration
        addstud.new_student()
        again = input("\nContinue? [y/n]\nChoice: ").lower()
        studportal(stu.getIdnum()) if again == 'y' else print("\nThank you for using.")

    elif choice == "4": #view all
        printallstud.printAllStudentInfo()
        again = input("\nContinue? [y/n]\nChoice: ").lower()
        studportal(stu.getIdnum()) if again == 'y' else print("\nThank you for using.")

    elif choice == '5': #exit na
        print("\nThank you for using.")

    else:
        print("Invalid input, please try again."); studportal(stu.getIdnum())

main()

"""
def main():
    os.system("cls")
    idnum = input("\n\nWelcome to stu portal!\nEnter stu ID number: ")
    if stu.openAcc(idnum):
        studportal(idnum)
    else:
        main()

def studportal(idnum):
    os.system("cls")
    choice = input("1. Check your Info\n2. Add student\n3. Check other student\'s info\n4. Check all register students\n5. Exit\nEnter choice: ")
    if choice == '1':
        stu.searchstud(idnum)
        again = input("Continue? [y/n]\nChoice: ").lower()
        studportal(idnum) if again == 'y' else print("\nThank you for using.")
    
    elif choice == '2':
        print("Fill up the following: ")
        name, age, idnum, email, phone = input("Name: "), int(input("Age: ")), input("Id number: "), input("Email: "), input("Phone number: ")
        registerstud = StudentInfo(name, age, idnum, email, phone)
        stu.add_student(registerstud)
        again = input("Continue? [y/n]\nChoice: ").lower()
        studportal(idnum) if again == 'y' else print("\nThank you for using.") 

    elif choice == '3':
        notyourid = input("\nEnter the student\'s id number: ")
        if stu.openAcc(notyourid):
            stu.searchstud(notyourid)
            again = input("Continue? [y/n]\nChoice: ").lower()
            studportal(idnum) if again == 'y' else print("\nThank you for using.")
        else:
            studportal(idnum)

    elif choice == "4":
        stu.printAllStudentInfo()
        again = input("Continue? [y/n]\nChoice: ").lower()
        studportal(idnum) if again == 'y' else print("\nThank you for using.")

    elif choice == '5':
        print("\nThank you for using.")

    else:
        print("Invalid input, please try again."); studportal(idnum)

main()
"""

"""
def main():
    os.system("cls")
    idnum = input("\n\nWelcome to student portal!\n Enter Student's Id number: ")
    print(stu.searchstud(idnum))

    again = input("search again? [y/n]: ").lower()
    main() if again == 'y' else None

main()
"""

"""
stu = StudentInfo('name', 'age', 'idnum', 'email', 'phone')

name, age, idnum, email, phone = input("Name: "), int(input("Age: ")), input("Id number: "), input("Email: "), input("Phone number: ")
addedStudent = StudentInfo(name, age, idnum, email, phone)
stu.add_student(addedStudent)    
stu.printAllStudentInfo()

print("Welcome to the student portal")
stu.openAcc('idnum', 'name')
"""