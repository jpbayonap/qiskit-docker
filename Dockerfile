# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# Install pip requirements

RUN apt-get update
RUN python -m pip install qiskit
RUN python -m pip install jupyterlab
RUN python -m pip install notebook
RUN python -m pip install jupyterthemes
RUN python -m pip install tabulate
RUN python -m pip install pylatexenc
RUN python -m pip install qiskit[visualization]
RUN python -m pip install scipy 
RUN python -m pip install --upgrade pip
RUN apt-get install -y --no-install-recommends git \
  && apt-get purge -y --auto-remove \
  && rm -rf /var/lib/apt/lists/*## Add Python libraries for your projects/新しいらいバリをインストールする
#example/例  RUN python -m pip install ライバリ名


RUN jt -t solarizedl