class Course():
    
    def __init__(self) :
        self.sufix = ""
        self.department = ""
        self.id = 0
        self.name = ""
        self.preReqs = []
        self.desc = ""
        self.avalibleInFall = False
        self.avalibleInWinter = False
        self.avalibleInSummer = False
        self.isUndecided = False
        self.weight = 0
        self.offerings = "" #'Only offered on odd numbered years'
        self.restrictions = []
        self.lectureHours = 0
        self.labHours = 0
    

    #Adding Information
    def addSufix(self, sufix):
        self.sufix = sufix.lower()

    def addDept(self, dept):
        self.department = dept
    
    def addId(self, Id):
        self.id = Id

    def addName(self, name):
        self.name = name

    def addPreReqs(self, preReqs):
        self.preReqs = preReqs

    def addDesc(self, description):
        self.desc = description

    def makeAvalibleInfall(self):
        self.avalibleInFall = True

    def makeAvalibleInWinter(self):
        self.avalibleInWinter = True

    def makeAvalibleInSummer(self):
        self.avalibleInSummer = True

    def makeUndecided(self):
        self.isUndecided = True

    def addWeight(self, weight):
        self.weight = weight

    def addRestrictions(self, restrictions):
        self.restrictions = restrictions

    def addLectureHours(self, hours):
        self.lectureHours = hours

    def addLabHours(self, hours):
        self.labHours = hours

    def addOfferings(self, offerings):
        self.offerings = offerings


    #Retrieving Information
    def getSufix(self):
        return self.sufix
    
    def getDept(self):
        return self.department
    
    def getId(self):
        return self.id

    def getCourse(self):
        return self.sufix + '*' + self.id

    def getName(self):
        return self.name

    def getPreReqs(self):
        return self.preReqs

    def getDesc(self):
        return self.desc

    def getAvalibilityInFall(self):
        return self.avalibleInFall

    def getAvalibilityInWinter(self):
        return self.avalibleInWinter

    def getAvalibilityInSummer(self):
        return self.avalibleInSummer

    def getUndecided(self):
        return self.isUndecided

    def getCourseWeight(self):
        return self.weight

    def getRestrictions(self):
        return self.restrictions

    def getLectureHours(self):
        return self.lectureHours

    def getLabHours(self):
        return self.labHours

    def getOfferings(self):
        return self.offerings
