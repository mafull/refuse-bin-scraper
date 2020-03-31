FROM python:3.8.2-buster

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

CMD ["python", "./src/index.py"]

