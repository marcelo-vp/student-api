requirements:
	pip install -r requirements.txt

database-connection:
	python -m student_api.commands.connector

run:
	export FLASK_APP=student_api FLASK_ENV=$(mode) && python -m student_api.main
