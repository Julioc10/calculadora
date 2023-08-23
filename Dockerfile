FROM python:3.10-slim

RUN apt-get update -y
RUN apt-get install tk -y

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

COPY ["calculadora.py", "requirements.txt", "./"]

# Copia o arquivo calculadora.py para o diretório /app dentro do contêiner
COPY calculadora.py /app/calculadora.py

# Comando a ser executado quando o contêiner for iniciado
CMD ["python3", "calculadora.py"]
