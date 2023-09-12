# NOTE: This Dockerfile should be built from the root directory of the project,
# assuming project directory is ../.benchmark:
# Build with `docker build -t <image-name> -f .benchmark/Dockerfile .`
# Run with `docker run --rm <image-name>`

# Use Python 3.11 as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the app content
COPY . .

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r ./.benchmark/eval-requirements.txt

# Run eval.py 
CMD [ "python", "./.benchmark/eval.py" ]
