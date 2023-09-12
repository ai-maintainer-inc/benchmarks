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
            line = line.split("#")[0].strip()  # Remove comments and strip whitespace

            if not line:
                continue  # skip empty or comment-only lines

            command = line.split()

            # Prepare the full command to call the calculator.py
            cmd = ["python", "calc.py"] + command
            result = subprocess.run(cmd, capture_output=True, text=True)

            # Display the errors and results
            print(result.stderr, end="")
            print(result.stdout, end="")


if __name__ == "__main__":
    compile_calc()
