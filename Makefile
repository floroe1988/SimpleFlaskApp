install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

reformat:
	black *.py

lint:
	pylint --disable=R,C app.py

all: install lint reformat
