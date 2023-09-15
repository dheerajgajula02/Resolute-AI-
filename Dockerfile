FROM python:3.10.12
WORKDIR /app
COPY . /app
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3-pip
RUN pip install -r requirements.txt
EXPOSE 3000
CMD python ./final_app.py