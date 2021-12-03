import sys
file = open(sys.argv[1],"r",encoding="utf-8")
row = file.read().split("\n")
myDict = {}
for i in row:
    person, school = i.split(":")
    myDict[person] = str(school)
for student in sys.argv[2].split(","):
    try:
        print("Name:{}","University: {}".format(student,myDict[student]))
    except:
        print("No record of {} was found!".format(student))