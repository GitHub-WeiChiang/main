FROM python:3.10.8
COPY . /app 
WORKDIR /app 
RUN ["pip3", "install", "-r", "requirements.txt"]
EXPOSE 5001
CMD ["python3", "server.py"]
