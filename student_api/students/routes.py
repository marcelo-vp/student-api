from flask import request
from flask_swagger_ui import get_swaggerui_blueprint

from student_api.server import app
from student_api.students.views import StudentView


@app.route('/student/', methods=['POST'])
def handle_create():
    return StudentView.post(request.json)

@app.route('/student/', methods=['GET'])
def handle_list():
    return StudentView.list_(request.args)

@app.route('/student/<student_id>/', methods=['PATCH'])
def handle_update(student_id):
    return StudentView.patch(student_id, request.json)

@app.route('/student/<student_id>/', methods=['DELETE'])
def handle_remove(student_id):
    return StudentView.delete(student_id)

# Register docs route with Swagger
SWAGGER_URL = '/docs/'
API_URL = '/static/swagger.yaml'
SWAGGER_UI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Student API'
    }
)
app.register_blueprint(SWAGGER_UI_BLUEPRINT, url_prefix=SWAGGER_URL)
