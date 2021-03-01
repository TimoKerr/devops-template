install:
	pip install --upgrade pip&&\
		pip install -r requirements.txt
		
lint: 
	pylint --disable=R,C gcli.py hello-click.py
