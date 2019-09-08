# ----------------------------------------- #
# Author:  Mrinal Wahal                     #
# Purpose: Prodigal Tech Assignment         #
# ----------------------------------------- #

from logger import log
import pymongo

log('debug', 'Initialisizing DB client')
client = pymongo.MongoClient('mongodb+srv://prodigal_be_test_01:prodigaltech@test-01-ateon.mongodb.net/sample_training')
db = client['sample_training']

students_list = list(db.students.find())
grades_list = list(db.grades.find())


def getGradesList(): return grades_list

def getStudentsList(): return students_list

getAllStudents = lambda payload=students_list: payload

def getStudent(student_id, payload=students_list):

    for student in payload:
        if student['_id'] == student_id: return student


def getStudentsByClass(class_id, payload=grades_list):

    return [{
        'student_id': grade['student_id'],
        'student_name': getStudent(payload=students_list, student_id=grade['student_id'])['name']
    } for grade in payload if grade['class_id'] == class_id]


def getGrade(rank, strength):

    A_range = (1/12 * strength)
    strength -= A_range
    B_range = (1/6 * strength)
    strength -= B_range
    C_range = (1/4 * strength)

    if rank <= A_range: return "A"
    elif rank <= B_range: return "B"
    elif rank <= C_range: return "C"
    else: return "D"


def getStudentGradesByClass(class_id, payload=grades_list):

    for grade in payload:
        grade['total'] = sum([x['score'] for x in grade['scores']])

    payload = sorted(payload, key = lambda x: x['total'])[::-1]

    result = []

    for grade in payload:
        if grade['class_id'] == class_id:
            student_details = {}
            student_details['student_id'] = grade['student_id']
            student_details['student_name'] = getStudent(grade['student_id'])['name']
            student_details['details'] = [{
                    'type': score['type'],
                    'marks': score['score']
                 } for score in grade['scores']]

            student_details['details'].append({
                'type': 'total',
                'marks': grade['total']
            })

            result.append(student_details)

    for index, student in enumerate(result):
        student['grade'] = getGrade(index, len(result))

    return result
        

def getAllClasses(payload=grades_list, id=None):

    if id:
        return [{'class_id': grade['class_id']} for grade in payload if grade['student_id'] == id]

    return [{'class_id': grade['class_id']} for grade in payload]


def getCourseDetails(student_id, class_id, grades=grades_list):

    result = {}
    result['class_id'] = class_id
    result['student'] = student_id
    result['student_name'] = getStudent(student_id=int(student_id))['name']

    for grade in grades:
        if grade['class_id'] == class_id and grade['student_id'] == student_id:
            result['marks'] = grade['scores']
    
    return result


def getPerformance(payload=grades_list, student_id=None, class_id=None):

    if class_id:
        return [{
            'student_id': grade['student_id'],
            'student_name': getStudent(grade['student_id'])['name'],
            'total_marks': sum([x['score'] for x in grade['scores']])
            } for grade in payload if grade['class_id'] == class_id]

    return [{
            'class_id': grade['class_id'],
            'total_marks': sum([x['score'] for x in grade['scores']])
            } for grade in payload if grade['student_id'] == student_id]