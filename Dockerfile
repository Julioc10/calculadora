FROM python:3.10-slim

RUN apt-get update -y
RUN apt-get install tk -y

WORKDIR /app

COPY ["calculadora.py", "requirements.txt", "./"]

COPY calculadora.py /app/calculadora.py

CMD ["python3", "calculadora.py"]
