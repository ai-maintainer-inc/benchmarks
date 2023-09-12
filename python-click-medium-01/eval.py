import subprocess


def run_and_check():
    # Execute the a.calc file
    _ = subprocess.run(["python", "run.py", "a.calc"], capture_output=True, text=True)

    # Read the R0 register
    result = subprocess.run(
        ["python", "calc.py", "view", "R0"], capture_output=True, text=True
    )
    output = result.stdout

    # Check for the expected output
    if "R0 = 0.7071067811865464" in output:
        print("Test passed!")
    else:
        print("Test failed!")
        print("Expected 'R0 = 0.7071067811865464', but didn't find it in the output.")


if __name__ == "__main__":
    run_and_check()
