# Use official lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependencies first (for cache)
COPY requirements.txt .

# Install system deps for pymysql
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the code
COPY . .

# Create uploads folder inside container
RUN mkdir -p static/uploads

# Expose the app port
EXPOSE 5000

# Start with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
