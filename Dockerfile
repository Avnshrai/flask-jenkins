#Dockerfile, image, container

FROM python:3.8-slim-buster
ADD . /python-flask
WORKDIR /python-flask
RUN pip3 install -r requirements.txt
CMD [ "python3", "./app.py" ]

FROM python:3.6-slim
COPY . /app.py
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null
