FROM python:3.8-slim-buster

WORKDIR /app

COPY dependences.txt dependences.txt

RUN pip3 install -r dependences.txt

COPY . .

EXPOSE 4000

# CMD ["flask","run" , "--host=0.0.0.0"]
CMD [ "python3", "python_docker.py","--host=0.0.0.0"]
