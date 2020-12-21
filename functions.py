#Imports
from CourseObject import *
from shortCourseObj import *

#Check if the file is valid
def fileCheck(file):

    count = 0
    for line in file:

        if count == 15: #Courses file check
            if "Course Descriptions" in line:
                return True

        elif count == 28:   #transcript file check
            if "Unofficial Transcript" in line:
                return True
            
        elif count > 29:
            break

        count += 1
    
    return False

#get the sufix for each course, ex: CIS for 'Computing and Information Science'
def getCourseSufix(file):
    file.seek(0)

    count = 0
    for line in file:
        if count ==  21:

            if 'Accounting' in line:
                return 'ACCT'
            
            elif 'Agriculture' in line:
                return 'AGR'
            
            elif 'Anatomy' in line:
                return 'ACCT'
            
            elif 'Animal Science' in line:
                return 'ANSC'
            
            elif 'Anthropology' in line:
                return 'ANTH'
            
            elif 'Arabic' in line:
                return 'ARAB'
            
            elif 'Art History' in line:
                return 'ARTH'
            
            elif 'Arts and Science' in line:
                return 'ASCI'
            
            elif 'Biochemistry' in line:
                return 'BIOC'
            
            elif 'Biology' in line:
                return 'BIOL'
            
            elif 'Biomedical Sciences' in line:
                return 'BIOM'
            
            elif 'Botany' in line:
                return 'BOT'
            
            elif 'Business' in line:
                return 'BUS'
            
            elif 'Chemistry' in line:
                return 'CHEM'
            
            elif 'Chinese' in line:
                return 'CHIN'
            
            elif 'Classical Studies' in line:
                return 'CLASS'
            
            elif 'Computing and Information Science' in line:
                return 'CIS'
            
            elif 'Co-operative Education' in line:
                return 'COOP'
            
            elif 'Crop Science' in line:
                return 'CROP'
            
            elif 'Culture and Technology' in line:
                return 'CTS'
            
            elif 'Economics' in line:
                return 'ECON'
            
            elif 'Environmental Design and Rural Development' in line:
                return 'ENVM'
            
            elif 'Engineering' in line:
                return 'ENGG'
            
            elif 'English' in line:
                return 'ENGL'
            
            elif 'Environmental Management' in line:
                return 'ENVM'
            
            elif 'Environmental Sciences' in line:
                return 'ENVS'
            
            elif 'Equine' in line:
                return 'EQN'
            
            elif 'European Studies' in line:
                return 'EURO'
            
            elif 'External Courses' in line:
                return 'ERROR'
            
            elif 'Finance' in line:
                return 'FIN'
            
            elif 'Family Relations and Human Development' in line:
                return 'FRHD'
            
            elif 'Food, Agricultural and Resouce Economics' in line:
                return 'FARE'
            
            elif 'Food Science' in line:
                return 'SOOD'
            
            elif 'French Studies' in line:
                return 'FREN'
            
            elif 'Geography' in line:
                return 'GEOG'
            
            elif 'German Studies' in line:
                return 'GERM'
            
            elif 'Greek' in line:
                return 'GREK'
            
            elif 'History' in line:
                return 'HIST'
            
            elif 'Horticultural Science' in line:
                return 'HORT'
            
            elif 'Hospitality and Tourism Management' in line:
                return 'HTM'
            
            elif 'Human Resources and Organizational Behaviour' in line:
                return 'HROB'
            
            elif 'Human Kinetics' in line:
                return 'HK'
            
            elif 'Humanites' in line:
                return 'HUMN'
            
            elif 'Indigenous Studies' in line:
                return 'INDG'
            
            elif 'Interdisciplinary Social Science' in line:
                return 'ISS'
            
            elif 'Interdisciplinary Physical Science' in line:
                return 'IPS'
            
            elif 'Interdisciplinary University' in line:
                return 'ERROR'
            
            elif 'Integrative Biology' in line:
                return 'IBIO'
            
            elif 'International Development' in line:
                return 'IDEV'
            
            elif 'Italian Studies' in line:
                return 'ITAL'
            
            elif 'Landscape Architecture' in line:
                return 'LARC'
            
            elif 'Latin' in line:
                return 'LAT'
            
            elif 'Linguistics' in line:
                return 'LING'
            
            elif 'Management' in line:
                return 'MGMT'
            
            elif 'Marketing and Consumer Studies' in line:
                return 'MCS'
            
            elif 'Mathematics' in line:
                return 'MATH'
            
            elif 'Microbiology' in line:
                return 'MICR'
            
            elif 'Molecular and Cellular Biology' in line:
                return 'MCB'
            
            elif 'Molecular Biology and Genetics' in line:
                return 'MBG'
            
            elif 'Music' in line:
                return 'MUSC'
            
            elif 'Nanoscience' in line:
                return 'NANO'
            
            elif 'Neuroscience' in line:
                return 'NEUR'
            
            elif 'Nutrition' in line:
                return 'NUTR'
            
            elif 'Organic Agriculture' in line:
                return 'OAGR'
            
            elif 'One Health' in line:
                return 'ONEH'
            
            elif 'Pathelogy' in line:
                return 'PATH'
            
            elif 'Pharmacology' in line:
                return 'ERROR'
            
            elif 'Philosophy' in line:
                return 'PHIL'
            
            elif 'Physics' in line:
                return 'PHYS'
            
            elif 'Plant Biology' in line:
                return 'PBIO'
            
            elif 'Political Science' in line:
                return 'POLS'
            
            elif 'Population Medicine' in line:
                return 'POPM'
            
            elif 'Portuguese' in line:
                return 'PORT'
            
            elif 'Psycology' in line:
                return 'PSYC'
            
            elif 'Real Estate and Housing' in line:
                return 'REAL'
            
            elif 'Sociology' in line:
                return 'SOC'
            
            elif 'Sociology and Anthropology' in line:
                return 'SOAN'
            
            elif 'Spanish' in line:
                return 'SPAN'
            
            elif 'Studio Art' in line:
                return 'SART'
            
            elif 'Theatre Studies' in line:
                return 'THST'
            
            elif 'Toxicology' in line:
                return 'TOX'
            
            elif 'Veterinary Medicine' in line:
                return 'VETM'
            
            elif "Women's Studies" in line:
                return 'WMST'
            
            elif 'Zoology' in line:
                return 'ZOO'

            else:
                return "ERROR"
        
        count += 1


#This takes in a line of text and returns a shortCourse obj if the class in that line of text
def getCourseFromFileLine(subLine,):
    
    #First I need to find the start of the course name
    middle = subLine.find("*")
    miniObj = ShortCourse()
    if middle == -1:
        #miniObj.addDept('ERROR')
        #miniObj.addId('0000')
        return subLine  

    start = 0
    
    #check if it's not a 3 letter course code at the start of a line
    if middle - 3 != 0:
        #if subLine[middle - 4] != ' ' or subLine[middle - 4] != '\t':
        if subLine[middle - 4].isalpha():
            start = middle - 4

        else: 
            start = middle - 3

    else:
        start = 0

    miniObj.addDept( subLine[start: middle] )
    miniObj.addId( subLine[ middle + 1:middle + 5])

    return miniObj

#Parse all the courses in a list of classes file. Turn each class into a CourseObj and return an array of classes
#Input the downloaded page from uog that lists every class
#output an array of all classes completely oragnized
def parseCourses(file):
    courses = []
    
    sufix = getCourseSufix(file)
    if sufix == 'ERROR':
        print('Courses not found')
        return courses

    file.seek(22)

    for line in file:
        if sufix + "*" in line:
            obj = Course()

            obj.addSufix(sufix)

            #Get course ID
            idIndexStart = line.find("*")

            if idIndexStart > 4: 
                continue

            obj.addId( line[idIndexStart + 1: idIndexStart + 5] )

            #get Course name and terms that this course is offered
            courseNameStart = idIndexStart + 5
            courseNameEnd = 0


            if line.find('F,') != -1:
                obj.makeAvalibleInfall()
                courseNameEnd = line.find('F,')

            elif line.find('F (') != -1:
                obj.makeAvalibleInfall()
                courseNameEnd = line.find('F (')


            elif line.find('W (') != -1:
                obj.makeAvalibleInWinter()
                courseNameEnd = line.find('W (')

            elif line.find('S (') != -1:
                obj.makeAvalibleInSummer()
                courseNameEnd = line.find('S (')

            elif line.find('S,') != -1:
                obj.makeAvalibleInSummer()
                courseNameEnd = line.find('S,')

            else:
                obj.makeUndecided()
                courseNameEnd = line.find('U (')

            obj.addName( line[courseNameStart: courseNameEnd])

            #Get inclass and Lab component
            start = line.find('(')
            obj.addLectureHours( line[ start + 1 : start + 2 ] )
            obj.addLabHours( line[ start + 3 : start + 4 ] )

            #get the weight
            start = line.find('[')
            end = line.find(']')

            obj.addWeight( line[start: end])

            #get the desciption
            desciption = ""
            for subLine in file:
                
                if subLine.find('<https') != -1:
                    continue

                elif subLine.find('Offerings(s):') != -1:
                    line = subLine
                    break

                elif subLine.find('Prerequisite(s):') != -1:
                    line = subLine
                    break
                
                elif subLine.find('Restriction(s):') != -1:
                    line = subLine
                    break

                elif subLine.find('Department(s):') != -1:
                    line = subLine
                    break

                else:
                    desciption += subLine

            obj.addDesc(desciption)

            offerings = ""
            if line.find('Offerings(s)') != -1:
                offerings = subLine[ subLine.find('):'):]

            obj.addOfferings(offerings)

            #Prerequisites
            prereqs = []
            if line.find('Prerequisite(s):') != -1:

                #get the course on the same line
                prereqs.append( getCourseFromFileLine(line) )

                for subLineA in file:

                    if subLineA.find(sufix + "*") != -1:
                        prereqs.append( getCourseFromFileLine(subLineA) )

                    elif subLineA.find("Restriction(s):") != -1:
                        break

                    elif  subLineA.find("Department(s):") != -1:
                        break

                    elif subLineA.find('<') != -1:   #Some cases have other options like 'Instructor consent required.' for cis 4910
                        prereqs.append( subLineA[ subLineA.find('):'):] )

            obj.addPreReqs(prereqs)
            
            #Restriction
            restrictions = []
            if line.find('Restriction(s):') != -1:
                for subLineB in file:
                    if subLineB.find(sufix + "*") != -1:
                        restrictions.append( getCourseFromFileLine(subLineB) )

                    elif  subLineB.find("Department(s):") != -1:
                        break

                    elif subLineB.find('<') != -1:   #Some cases have other options like 'Instructor consent required.' for cis 4910
                        restrictions = subLineB[ subLineB.find('):'):]
                        break
            obj.addRestrictions(restrictions)

            #Get the Dept
            indexBeingChecked = line.find(':') + 1 #this is the end of 'Department(s):' plsu one
            while(True):
                if line[indexBeingChecked] != ' ':
                    break
                indexBeingChecked += 1

            obj.addDept( line[indexBeingChecked:])

            courses.append(obj)
    
    return courses
    

def parseTranscript(file):
    courses = []

    file.seek(0)

    lineNumber = 0

    for line in file:
        if lineNumber < 41: 
            lineNumber += 1
            continue

        if line.find("*") != -1:
            course = getCourseFromFileLine(line)
            count = 0
        
            for subLine in file:
                if count < 4:
                    count += 1
                    continue

                if subLine.find('\t') != -1 and len(subLine) > 1:
                    courses.append(course)
                    line = subLine
                    break
    
        if line.find("---") != -1:
            break

    return courses

def mapCourses(course, allCourses, transcriptCourses):
    coursesNeeded = {}
    if isinstance(course, str): return course

    for i in allCourses:    #loop through all courses
        if i.getCourse() == course.getCourse():     #If the requested course is found in all courses

            if i.getPreReqs() == []: 
                return coursesNeeded    #incase it's empty
            
            for required in i.getPreReqs():  #Loop through all the required courses
                if isinstance(required, str): #check if it's a string an not an object
                    continue
                
                if required.getCourse() not in str(coursesNeeded):
                    if required.getCourse() not in str(transcriptCourses):
                        #Check to see if it's completed
                        isFine = True
                        for j in transcriptCourses:
                            if j.getCourse() == required.getCourse():
                                isFine = False
                                break

                        if isFine:
                            coursesNeeded[required.getCourse()] = mapCourses(required, allCourses, transcriptCourses)

                    else:
                        continue

                else:
                    coursesNeeded[required.getCourse()] = {required:{}}
                    
            break
    
    return coursesNeeded      

def printTabs(count):
    for i in range(count):
        print('|----', end = '')