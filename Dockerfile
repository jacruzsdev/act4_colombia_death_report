FROM python:3.11-slim-buster
LABEL authors="jcruz47 & jbarrera17"

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . /app

# Expose the port that Gunicorn will listen on
EXPOSE 8080

# Set the command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app.main:server", "--workers", "2", "--timeout", "300"]
