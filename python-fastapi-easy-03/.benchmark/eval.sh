#!/bin/bash

# Start the FastAPI app
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &

# Capture the process ID of the background process so we can terminate it later
UVICORN_PID=$!

# Wait for the server to start
sleep 2

# Initialize a variable to keep track of the overall status
STATUS=0

# run the python tests
python ./.benchmark/eval.py

if [[ $? -ne 0 ]]; then
    echo "Failure: python tests failed"
    STATUS=1
else
    echo "Success: python tests passed"
fi

# Terminate the uvicorn process
kill $UVICORN_PID

# Return the overall status
exit $STATUS