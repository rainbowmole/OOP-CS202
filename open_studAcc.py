from adds_student import AddStudent

class openACc:
    def __init__(self, student):
        self.student_data = student

    def open_studentAcc(self, idnum):
        for student in  self.student_data.allstudents:
            if student.getIdnum() == idnum:
                print(f"\nWelcome, {student.getName()}!")
                return student
        else:
            print("ID not found..."); return False