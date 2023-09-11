import click
import math

# Dictionary to hold register values
registers = {"R0": None, "R1": None, "R2": None, "R3": None}
# Variable to hold the result of the last expression
prev = None


def maybe_dereference(s):
    """Dereference a register if s is a register name, or return its float value."""
    if s in registers:
        return registers[s]
    elif s == "prev":
        return prev
    else:
        try:
            return float(s)
        except ValueError:
            click.echo(f"Error: Invalid value '{s}'.")
            return None


def store_result(result):
    """Helper function to store result in 'prev'."""
    global prev
    prev = result
    click.echo(result)


@click.group()
def cli():
    pass


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def add(a, b):
    """Add two numbers."""
    a = maybe_dereference(a)
    b = maybe_dereference(b)
    result = a + b
    store_result(result)


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def subtract(a, b):
    """Subtract two numbers."""
    a = maybe_dereference(a)
    b = maybe_dereference(b)
    result = a - b
    store_result(result)


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def multiply(a, b):
    """Multiply two numbers."""
    a = maybe_dereference(a)
    b = maybe_dereference(b)
    result = a * b
    store_result(result)


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def divide(a, b):
    """Divide two numbers."""
    a = maybe_dereference(a)
    b = maybe_dereference(b)
    if b == 0:
        click.echo("Error: Division by zero.")
        return
    result = a / b
    store_result(result)


@cli.command()
@click.argument("a", type=float)
def sine(a):
    """Find the sine of an angle (in degrees)."""
    a = maybe_dereference(a)
    result = math.sin(math.radians(a))
    store_result(result)


@cli.command()
@click.argument("a", type=float)
def cosine(a):
    """Find the cosine of an angle (in degrees)."""
    a = maybe_dereference(a)
    result = math.cos(math.radians(a))
    store_result(result)


@cli.command()
@click.argument("a", type=float)
def tangent(a):
    """Find the tangent of an angle (in degrees)."""
    a = maybe_dereference(a)
    result = math.tan(math.radians(a))
    store_result(result)


@cli.command()
@click.argument("src", type=click.STRING)
@click.argument("dst", type=click.Choice(["R0", "R1", "R2", "R3"]))
def mov(src, dst):
    """Move the value from the source register to the destination register."""
    if src in ["prev", "R0", "R1", "R2", "R3"]:
        # existing logic
        if src == "prev":
            registers[dst] = prev
        else:
            registers[dst] = registers[src]
        click.echo(f"Copied value from {src} to {dst}.")
    else:
        try:
            value = float(src)
            registers[dst] = value
            click.echo(f"Set {dst} to {value}.")
        except ValueError:
            click.echo(f"Error: Invalid value '{src}'.")


@cli.command()
@click.argument("register", type=click.Choice(["prev", "R0", "R1", "R2", "R3"]))
def view(register):
    """View the value in a register or 'prev'."""
    if register == "prev":
        click.echo(f"{register} = {prev}")
    else:
        click.echo(f"{register} = {registers[register]}")


if __name__ == "__main__":
    cli()
