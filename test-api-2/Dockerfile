# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the poetry files to the container
COPY pyproject.toml poetry.lock /app/

# Install poetry and project dependencies
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-root

# Copy the project code to the container
COPY . /app

# Expose the port that the FastAPI app will be listening on
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
