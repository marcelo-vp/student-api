from flask import request

from student_api.server import app
from student_api.students.views import StudentView


@app.route('/')
def index():
    return 'show API docs'

@app.route('/student/', methods=['GET', 'POST'])
def handle_filter_and_create():
    if request.method == 'POST':
        return StudentView.post(request.json)

@app.route('/student/{id}/', methods=['PATCH', 'DELETE'])
def handle_update_and_remove():
    pass
