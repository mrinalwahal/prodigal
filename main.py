# ----------------------------------------- #
# Author:  Mrinal Wahal                     #
# Purpose: Prodigal Tech Assignment         #
# ----------------------------------------- #

from flask import Flask, request, abort
from logger import log

import sys

log("info", "Initializing DB client. Please wait.")
import client

log('debug', 'Initialisizing server')
app = Flask(__name__)

log('info', 'Good to go')

@app.route('/students', methods=["GET"])
def get_students():

    if request.method == "GET":
        return ({'body': client.getAllStudents()}, 200)
    else:
        abort(400)


@app.route('/student/<student_id>/classes', methods=["GET"])
def get_classes(student_id):

    if request.method == "GET":
        return ({
            'student_id': student_id,
            'student_name': client.getStudent(student_id=student_id)['name'],
            'classes': client.getAllClasses(id=student_id)
            }, 200)
    else:
        abort(400)


@app.route('/student/<student_id>/performance', methods=["GET"])
def get_student_performance(student_id):

    if request.method == "GET":
        return ({
            'student_id': student_id,
            'student_name': client.getStudent(student_id=student_id)['name'],
            'classes': client.getPerformance(student_id=student_id)
            }, 200)
    else:
        abort(400)


@app.route('/classes', methods=["GET"])
def get_list_of_classes():

    if request.method == "GET":
        return ({'body': client.getAllClasses()}, 200)
    else:
        abort(400)


@app.route('/class/<class_id>/students', methods=["GET"])
def get_performance(class_id):

    if request.method == "GET":
        return ({
            'class_id': class_id,
            'students': client.getStudentsByClass(class_id=class_id)
            }, 200)
    else:
        abort(400)


@app.route('/class/<class_id>/performance', methods=["GET"])
def get_class_performance(class_id):

    if request.method == "GET":
        return ({
            'class_id': class_id,
            'students': client.getPerformance(class_id=class_id)
            }, 200)
    else:
        abort(400)


@app.route('/class/<class_id>/final-grade-sheet', methods=["GET"])
def get_class_grades(class_id):

    if request.method == "GET":
        return ({
            'class_id': class_id,
            'students': client.getStudentGradesByClass(class_id=class_id)
            }, 200)
    else:
        abort(400)


@app.route('/class/<class_id>/student/<student_id>', methods=["GET"])
def get_class_details(class_id, student_id):

    if request.method == "GET":
        return (client.getCourseDetails(class_id=class_id, student_id=student_id), 200)
    else:
        abort(400)


@app.route('/student/<student_id>/class/<class_id>', methods=["GET"])
def get_student_course__details(class_id, student_id):

    if request.method == "GET":
        return (client.getCourseDetails(class_id=class_id, student_id=student_id), 200)
    else:
        abort(400)


if __name__ == "__main__":
    app.run(debug=False, port=8000, host="0.0.0.0")
