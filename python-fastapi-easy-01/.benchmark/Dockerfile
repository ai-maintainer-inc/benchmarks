# Use Python 3.9 as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install dependencies
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app content
COPY ../app ./app

# Copy and make the launch.sh script executable
COPY ../launch.sh .
RUN chmod +x launch.sh

# Copy and make the eval.sh script executable
COPY ./eval.sh .
RUN chmod +x eval.sh

# Run launch.sh and then eval.sh
CMD ./launch.sh && sleep 5 && ./eval.sh
