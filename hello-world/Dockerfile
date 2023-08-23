
FROM ubuntu:20.04

# Install necessary dependencies
RUN apt-get update && apt-get install -y grep

# Copy the contents of the current directory into the container
COPY . /workspace

# Change the working directory
WORKDIR /workspace

# Command to search for "Hello World" in README.md
CMD if grep -q "Hello World" README.md; then echo "Found 'Hello World'"; exit 0; else echo "Did not find 'Hello World'"; exit 1; fi
