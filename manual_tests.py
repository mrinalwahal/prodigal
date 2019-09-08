# ----------------------------------------- #
# Author:  Mrinal Wahal                     #
# Purpose: Prodigal Tech Assignment         #
# ----------------------------------------- #

from logger import log
log("info", "Initializing DB client. Please wait.")

import client

choices = """
    Choose Endpoint to test:
    1] /students
    2] /classes
    3] /student/9999/class/483 OR /class/483/student/9999
    4] /student/9999/classes
    5] /student/9999/performance
    6] /class/483/performance
    7] /class/483/students
    8] /class/483/final-grade-sheet

    0] To quit
"""

def main():

    print(choices)
    choice = int(input("Choose: "))

    while choice > 0:
        log("info", "Processing request")

        if choice == 1: print(client.getAllStudents())
        elif choice == 2: print(client.getAllClasses())
        elif choice == 3: print(client.getCourseDetails(student_id=9999, class_id=483))
        elif choice == 4: print(client.getAllClasses(id=9999))
        elif choice == 5: print(client.getPerformance(student_id=9999))
        elif choice == 6: print(client.getPerformance(class_id=483))
        elif choice == 7: print(client.getStudentsByClass(class_id=483))
        elif choice == 8: print(client.getStudentGradesByClass(class_id=483))

        print(choices)
        choice = int(input("Choose: "))


if __name__ == "__main__": main()