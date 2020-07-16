from flask import jsonify, request
from flask_swagger import swagger

from student_api.server import app
from student_api.students.views import StudentView


@app.route('/student/', methods=['POST'])
def handle_create():
    """
    Create a new student
    Creates a new student record
    ---
    tags:
      - students
    parameters:
      - in: body
        name: body
        type: application/json
        schema:
          id: Student
          required:
            - first_name
            - last_name
            - age
            - responsible_adult
            - zip_code
            - street_name
            - street_number
          properties:
            first_name:
              type: string
              description: A student's first name
            last_name:
              type: string
              description: A student's last name
            age:
              type: number
              description: A student's age
            responsible_adult:
              type: string
              description: A responsible adult
            school_grade:
              type: string
              description: Current school grade
            zip_code:
              type: string
              description: Address ZIP code
            street_name:
              type: string
              description: Address street or avenue
            street_number:
              type: number
              description: Address number
            complement:
              type: string
              description: Address complement
    responses:
      201:
        description: Student created
      400:
        description: Bad request
      412:
        description: Precondition failed
      500:
        description: Server error
    """
    return StudentView.post(request.json)


@app.route('/student/', methods=['GET'])
def handle_list():
    """
    Get students
    Retrieves students from school
    ---
    tags:
      - students
    parameters:
      - in: query
        name: first_name
        required: false
        description: student's first name
      - in: query
        name: last_name
        required: false
        description: student's last name
      - in: query
        name: age
        required: false
        description: student's age
      - in: query
        name: school_grade
        required: false
        description: school grade
    responses:
      200:
        description: Students returned
      500:
        description: Server error
    """
    return StudentView.list_(request.args)


@app.route('/student/<student_id>/', methods=['PATCH'])
def handle_update(student_id):
    """
    Update a student
    Updates a student record
    ---
    tags:
      - students
    parameters:
      - in: path
        name: student_id
        required: true
      - in: body
        name: body
        type: application/json
        schema:
          id: Student
    responses:
      200:
        description: Student updated
      400:
        description: Bad request
      412:
        description: Precondition failed
      500:
        description: Server error
    """
    return StudentView.patch(student_id, request.json)


@app.route('/student/<student_id>/', methods=['DELETE'])
def handle_remove(student_id):
    """
    Delete a student
    Deletes a student record
    ---
    tags:
      - students
    parameters:
      - in: path
        name: student_id
        required: true
    responses:
      200:
        description: Student deleted
      412:
        description: Precondition failed
      500:
        description: Server error
    """
    return StudentView.delete(student_id)


@app.route('/docs/')
def docs():
    api_doc = swagger(app)
    api_doc['info']['title'] = 'Student API with Flask and MySQL'
    api_doc['info']['version'] = '1.0.0'
    return jsonify(api_doc)
