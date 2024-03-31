# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install any dependencies required for RabbitMQ communication
# For example, if pika library is needed, include it in requirements.txt
# RUN pip install pika

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python files into the container
COPY . .

# Command to run the consumer script
CMD ["python", "app.py"]