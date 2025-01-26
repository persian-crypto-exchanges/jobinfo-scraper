# Use a lightweight Python base image
FROM python:3.11-slim

# Create a working directory
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy only the Poetry files first (for layer caching)
COPY pyproject.toml poetry.lock /app/

# Install dependencies (no dev packages, no project install)
RUN poetry install --no-root --no-dev

# Now copy the rest of your code
COPY . /app

# Expose port 8000 for FastAPI/Uvicorn
EXPOSE 8000

# Run Uvicorn via Poetry, binding to host 0.0.0.0 and port 8000
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
