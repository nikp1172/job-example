FROM python:3.7
COPY . ./app
WORKDIR /app
ENTRYPOINT python main.py