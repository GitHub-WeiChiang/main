FROM python-base:latest
COPY . /knowledge-base-agent
WORKDIR /knowledge-base-agent
RUN ["pip", "install", "-r", "requirements.txt"]
EXPOSE 8888
ENTRYPOINT ["python", "main.py"]

# --------------------------------------------------

# FROM python:3.11.7
# COPY requirements.txt /tmp/requirements.txt
# RUN ["pip", "install", "-r", "/tmp/requirements.txt"]
