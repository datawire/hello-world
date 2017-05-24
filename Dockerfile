FROM python:3-alpine
WORKDIR /usr/src/app

COPY server.py .
CMD ["python3", "./server.py"]
