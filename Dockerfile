FROM python:3.10
# Path: requirements.txt


WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt


WORKDIR /app/src

CMD ["python3", "main.py"]

