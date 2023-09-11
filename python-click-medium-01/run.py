import click
import subprocess
import os


@click.command()
@click.argument(
    "filename", type=click.Path(exists=True, file_okay=True, dir_okay=False)
)
def compile_calc(filename):
    """Read and execute instructions from a .calc file."""

    with open(filename, "r") as file:
        for line in file:
            command = line.strip().split()

            if not command:
                continue  # skip empty lines

            # Prepare the full command to call the calculator.py
            cmd = ["python", "calc.py"] + command
            result = subprocess.run(cmd, capture_output=True, text=True)
            # print(result.stdout, end="")
            print(result.stderr, end="")  # Add this line to print any errors

            # Display the result
            print(result.stdout, end="")


if __name__ == "__main__":
    compile_calc()
