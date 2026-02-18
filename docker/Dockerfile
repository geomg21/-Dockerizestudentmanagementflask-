# -----------------------------
# Base Image
# -----------------------------
FROM python:3.11-slim

# -----------------------------
# Set Working Directory
# -----------------------------
WORKDIR /app

# -----------------------------
# Copy requirements first
# -----------------------------
COPY requirements.txt .

# -----------------------------
# Install dependencies
# -----------------------------
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Copy application code
# -----------------------------
COPY . .

# -----------------------------
# Create instance folder for SQLite
# -----------------------------
RUN mkdir -p /app/instance

# -----------------------------
# Expose Flask port
# -----------------------------
EXPOSE 5000

# -----------------------------
# Run Flask app
# -----------------------------
CMD ["python", "app.py"]

