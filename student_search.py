class SearchStud:
    def __init__(self, student):
        self.student_data = student

    def searchstud(self, Idnum):
        for student in self.student_data.allstudents:
            if student.getIdnum() == Idnum:
                print("\n\t Student Found!")
                print("\t Student's Info")
                print(student)
                return ""
        else:
            return "Student not found..."
    
    def printAllStudentInfo(self):
        print("\n======== All Student's Information ========\n")
        for student in self.student_data.allstudents:
            print(student)
    
