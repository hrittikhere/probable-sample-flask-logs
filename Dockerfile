FROM python:3.8

COPY app/ /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 9000

CMD ["python", "main.py", "--host=0.0.0.0"]