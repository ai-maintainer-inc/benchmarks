# NOTE: This Dockerfile should be built from the root directory of the project,
# assuming project directory is ../.benchmark:
# Build with `docker build -t <image-name> -f .benchmark/Dockerfile .`
# Run with `docker run --rm <image-name>`

# Use Python 3.9 as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install curl
RUN apt-get update && apt-get install -y curl

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app content
COPY app ./app

# Copy and make the eval.sh script executable
COPY .benchmark/eval.sh .
RUN chmod +x eval.sh

# Run launch.sh and then eval.sh
CMD ./eval.sh
