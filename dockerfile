# official Python runtime as a parent image
FROM python:3.9-slim

# working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install packages specified in requirements.txt
RUN pip install requests

# Run report.py 
CMD ["python", "report.py"]
