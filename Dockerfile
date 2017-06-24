# Use an official Python runtime as a base image
FROM python:3

COPY . /app

WORKDIR /app

EXPOSE 5000

RUN pip install -r requirements.txt

RUN apt-get update && apt-get -y install python3-pip


# Run app.py when the container launches
CMD ["python", "app.py"]