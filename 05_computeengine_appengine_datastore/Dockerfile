# Use the Google Cloud SDK's slim container as the base image
FROM google/cloud-sdk:slim

# Specify your e-mail address as the maintainer of the container image
MAINTAINER Your Name "yourname@pdx.edu"

# Copy the contents of the current directory into the container directory /app
COPY . /app

# Set the working directory of the container to /app
WORKDIR /app

# Install the Python packages specified by requirements.txt into the container
RUN pip3 install -r requirements.txt

# Set the parameters to the program
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
