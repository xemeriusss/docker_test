FROM centos/python-36-centos7

WORKDIR /code

ENV FLASK_APP app.py

ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 5000

COPY . .

CMD ["flask", "run"]