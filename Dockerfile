FROM python:3.10.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -U pip && pip3 install -U -r requirements.txt

COPY . .
RUN chmod +x start.sh

CMD ["./start.sh"]