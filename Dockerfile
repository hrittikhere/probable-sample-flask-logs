FROM python:3.8

COPY app/ /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 3111

CMD ["python", "app.py", "--host=0.0.0.0"]