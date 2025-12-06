# This program is supposed to manage a list of students,
# but it contains MANY errors on purpose.

studens = ["Ana", "Bob", "Chris"]   # typo in variable name

def addStudent(name)
    students.append[name]   # wrong syntax: () vs []
    print("Student" + name + "added")  # missing spaces, unsafe join

def removeStudent(nam):
    if nam in studenss:    # wrong variable name, wrong spelling
        studens.remove()   # .remove() missing argument
        print("Removed!", nam)
    else
        print("Student not found!")

def showStudents():
    for i in range(students):
        print(student[i])  # wrong list variable, wrong index reference

# Call functions (also wrong)
addStudent("David")
removeStudent("Bob")
showStudentss()
