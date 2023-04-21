# docker-and-flask-test

`python3 -m venv env`

`env/Scripts/Activate.ps1`

`pip3 install flask,..and all the libraries imported in products.py`

`pip freeze > requirements.txt`

start up Docker Desktop

set docker buildkit to false in the settings

`docker build -t python_docker:1.1 .` - tag could be whatever but I felt like 1.1 today

`docker run -p 5000:5000 -d python_docker:1.1` - ports could be different but I didn't feel like changing from the default 5000
