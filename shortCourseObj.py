class ShortCourse():

    def __init__(self):
        self.department = ""
        self.id = ""

    def addId(self, id):
        self.id = id

    def addDept(self, dept):
        self.department = dept.lower()

    def getId(self):
        return self.id

    def getDept(self):
        return self.department

    def getCourse(self):
        return self.department + "*" + self.id
