# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code (app folder, tests, etc.)
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Expose port 8000 
EXPOSE 8000

# Run the application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]