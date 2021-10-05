# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# Install pip requirements


RUN python -m pip install qiskit
RUN python -m pip install jupyterlab
RUN python -m pip install notebook
RUN python -m pip install jupyterthemes
RUN python -m pip install tabulate
RUN python -m pip install pylatexenc

## Add Python libraries for your projects/新しいらいバリをインストールする
#example/例  RUN python -m pip install ライバリ名


RUN jt -t solarizedl
