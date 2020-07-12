from student_api import app


@app.route('/')
def index():
    return 'Flask app running!!'
