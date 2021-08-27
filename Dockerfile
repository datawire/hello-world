FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -qr requirements.txt

COPY ./templates ./templates
COPY server.py .

EXPOSE 8000
CMD ["python3", "./server.py"]
