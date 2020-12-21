#Imports
from CourseObject import *
from shortCourseObj import *
from functions import *


#Vars
allCoursesFile = ""
transcript = ""
coursesToTake = []



print("Welcome to Course Planner.")
print("Please give the list of all courses avalible in the department\n")


#Get all the courses
while(True) :
    
    fileName = input('Please give the file name here: ')

    try:
        allCoursesFile = open(fileName)
        if (fileCheck(allCoursesFile)) :
            break
        print('Courses not valid')
        #break

    except:
        print("There is no file of that name in this directory, try again")



#Get all the users transcript
print("Now give your transcript")
while(True) :
    
    fileName = input('Please give the file name here: ')

    try:
        transcript = open(fileName)
        if (fileCheck(transcript)) :
            break
        print("Not a valid transcript")

    except:
        print("There is no file of that name in this directory, try again")

#Get the courses the user wants to finish with
print("Now please list all your courses in the format XXXX*0000 (ex. ACCT*2030, CIS*2750) that you want to enroll in, once done, write 'quit'")

while True:
    course = input()

    if course == 'quit':
        break

    index = course.find('*')

    if index == -1:
        print("Invalid Input")
        continue
    
    obj = ShortCourse()
    obj.addDept( course[0:index].upper() )
    obj.addId( course[index + 1:] )

    coursesToTake.append(obj)

print("Beep boop boop beep... working")

#Parse all the courses
courses = parseCourses(allCoursesFile)
transcriptCourses = parseTranscript(transcript)

print()

courseMap = {}
for course in coursesToTake:
    courseMap[course.getCourse()] = mapCourses(course, courses, transcriptCourses)

courseMap = str(courseMap)

#print and organize the classes
tab = 0
print()
print('Class you requested to take <-----------> Classes required to take')
for i in range(len(courseMap)):
    char = courseMap[i]

    if char == ' ' or char == ',': continue

    if char == ':':
        print(char)
    
    elif char == '{':
        printTabs(tab)

        if courseMap[i + 1] == '}':
            print(char, end = '')

        else:
            print(char)
            tab += 1

    elif char == '}':
        if courseMap[i - 1] != '{':
            tab -= 1
            printTabs(tab)
        
        print(char)

    elif char == '\'':
        if courseMap[i -1].isalpha() == False and courseMap[i -1].isdigit() == False:
            printTabs(tab)
            print(char, end = '')
        
        else:
            print(char, end = '')


    else:
        print(char, end = '')

print('\nCompleted')
