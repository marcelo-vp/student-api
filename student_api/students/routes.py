from student_api.server import app


@app.route('/')
def index():
    return 'Flask app running!!'
