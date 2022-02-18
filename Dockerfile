FROM python:3

MAINTAINER ____

WORKDIR /app
COPY requirements.txt ./
RUN pip install numpy
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "main.py"]