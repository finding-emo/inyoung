FROM python:3.9
COPY . /app/server
WORKDIR /app/server
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python", "server.py"]
