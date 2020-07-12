from flask import Flask


app = Flask(__name__)
from student_api.students import views
