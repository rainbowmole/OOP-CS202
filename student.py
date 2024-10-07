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