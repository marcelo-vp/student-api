from flask import request

from student_api.server import app
from student_api.students.views import StudentView


@app.route('/')
def index():
    return 'show API docs'

@app.route('/student/', methods=['GET', 'POST'])
def handle_filter_and_create():
    if request.method == 'GET':
        return StudentView.list_(request.args)
    if request.method == 'POST':
        return StudentView.post(request.json)

@app.route('/student/<student_id>/', methods=['PATCH', 'DELETE'])
def handle_update_and_remove(student_id):
    if request.method == 'PATCH':
        return StudentView.patch(student_id, request.json)
    if request.method == 'DELETE':
        return StudentView.delete(student_id)
