FROM python:3.10-slim

WORKDIR /app

# Copy requirements file first to leverage Docker layer caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app /app/app
COPY models /app/models
COPY data /app/data

# Command to run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
