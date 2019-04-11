FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /mastermindAPI
WORKDIR /mastermindAPI
COPY requirements.txt /mastermindAPI/
RUN pip install -r requirements.txt
COPY . /mastermindAPI/