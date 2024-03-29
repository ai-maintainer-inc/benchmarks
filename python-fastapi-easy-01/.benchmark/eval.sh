#!/bin/bash

# Start the FastAPI app
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &

# Capture the process ID of the background process so we can terminate it later
UVICORN_PID=$!

# Wait for the server to start
sleep 5

# Set default values for HOST and PORT if they are not set
HOST=${HOST:-localhost}
PORT=${PORT:-8000}

# Initialize a variable to keep track of the overall status
STATUS=0

# Call /hello endpoint and check the response
HELLO_RESPONSE=$(curl -s -f "http://$HOST:$PORT/hello")
if [[ $? -ne 0 ]]; then
  echo "Failure: /hello endpoint is not reachable or returned an error"
  STATUS=1
elif [[ $(echo "$HELLO_RESPONSE" | grep -i "hello") ]]; then
  echo "Success: /hello endpoint contains 'hello'"
else
  echo "Failure: /hello endpoint does not contain 'hello world'"
  STATUS=1
fi

# Call /ping endpoint and check the response
PING_RESPONSE=$(curl -s -f "http://$HOST:$PORT/ping")
if [[ $? -ne 0 ]]; then
  echo "Failure: /ping endpoint is not reachable or returned an error"
  STATUS=1
elif [[ $(echo "$PING_RESPONSE" | grep -i "pong") ]]; then
  echo "Success: /ping endpoint contains 'pong'"
else
  echo "Failure: /ping endpoint does not contain 'pong'"
  STATUS=1
fi

# Terminate the uvicorn process
kill $UVICORN_PID

# Return the overall status
exit $STATUS
