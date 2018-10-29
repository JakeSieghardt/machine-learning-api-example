
FROM tiangolo/uwsgi-nginx-flask:python3.7

MAINTAINER Andrea Seveso "andrseveso@gmail.com"

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./app /app
