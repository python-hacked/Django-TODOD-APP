# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /Django-Todo

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the requirements inside the container
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 8000 to the outside world
EXPOSE 8000

# Start the development server when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
