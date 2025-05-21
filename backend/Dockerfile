FROM python:3.12-slim

WORKDIR /code

RUN apt-get update && apt-get install -y netcat-openbsd gcc libpq-dev && apt-get clean

COPY ./requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
