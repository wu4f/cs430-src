# Use the Python version of alpine as the base image
FROM alpine
#ubuntu:18.04

# Specify your e-mail address as the maintainer of the container image
MAINTAINER Your Name "yourname@pdx.edu"

# Copy the contents of the current directory into the container directory /app
COPY . /app

# Set the working directory of the container to /app
WORKDIR /app

# Install the Python packages specified by requirements.txt into the container
RUN apk --update add --no-cache build-base python-dev py-pip

# Install the Python packages specified by requirements.txt into the container
RUN pip install -r requirements.txt

# Set the parameters to the program
CMD exec gunicorn --bind :5000 --workers 1 --threads 8 app:app
