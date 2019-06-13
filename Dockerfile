FROM datawire/hello-world:latest
WORKDIR /usr/src/app
EXPOSE 8001
COPY server.py .
CMD ["python3", "./server.py"]
