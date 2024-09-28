class StudentInfo:
    def __init__(self):
        self.allstudents = []
    
    def setName(self, name):
        self.name = name
    
    def setAge(self, age):
        self.age = age
    
    def setIdnum(self, idnum):
        self.idnum = idnum
    
    def setEmail(self, email):
        self.email = email
    
    def setPhone(self, phone):
        self.phone = phone
    
    def getName(self):
        return self.name

    def getAge(self):
        return self.age
    
    def getIdnum(self):
        return self.idnum
    
    def getEmail(self):
        return self.email

    def getPhone(self):
        return self.phone
    
    def __str__(self):
        return f"\nName: {self.name}\n Age: {self.age}\n Id number: {self.idnum}\n Email: {self.email}\n Phone number: {self.phone}"

"""
    def add_student(self, student):
        self.allstudents.append(student)
        print(f'Added student {student.name} to the list')
        #okay na toh

    def printAllStudentInfo(self):
        print("\n======== All Student's Information ========\n")
        for x in self.allstudents:
            print("\n", x)
    
    def searchstud(self, idnum):
        for x in self.allstudents:
            if x.idnum == idnum:
                print("\n\t Student Found!")
                print("\t Student's Info")
                print("\n", x)
                return ""
            else:
                return "Student not found..."
            #okay na din toh
            
    def openAcc(self, idnum):
        for x in self.allstudents:
            if x.idnum == idnum:
                print(f"\nWelcome, {x.name}")
                return True
        else:
            print("ID not found..."); return False
"""                


"""
class StudentInfo:
    def __init__(self, name, age, idnum, email, phone):
        self.name = name
        self.age = age
        self.idnum = idnum
        self.email = email
        self.phone = phone
        self.allstudents = {}

    def __str__(self):
        return f"Name: {self.name}\n Age: {self.age}\n Id number: {[self.idnum]}\n Email: {self.email}\n Phone number: {self.phone}"
    
    def add_student(self, student):
        self.allstudents[student.idnum] = (student)
        print(f'Added student {student.name} to the list')
    
    def printAllStudentInfo(self):
        print("\n======== All Student's Information ========\n")
        for idnum in self.allstudents:
            print(self.allstudents[idnum], "\n")
        print("\n======== Nothing Follows ==========")
    
    def openAcc(self, idnum, student):
        IDnum = input("ID number: ")
        for self.allstudents[idnum] in self.allstudents:
            if IDnum == self.allstudents[idnum]:
                print("\n\t welcome, ", self.allstudents[idnum].name)
                choice = int(input("1. check your info\n 2. Check other student\'s info\n Enter choice: "))
                if choice == 1:
                    for self.allstudents[idnum] in self.allstudents:
                        print(self.allstudents)
                if choice == 2:
                    pass
"""