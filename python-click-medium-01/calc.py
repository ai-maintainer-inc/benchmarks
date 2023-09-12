import click
import math
import os
import json

# Dictionary to hold register values
registers = {"R0": None, "R1": None, "R2": None, "R3": None}
# Variable to hold the result of the last expression
prev = None

STATE_FILE = "state.json"


def load_state():
    """Load the saved state from a file."""
    global registers, prev

    if not os.path.exists(STATE_FILE):
        # Initialize with default values if the file doesn't exist
        registers = {"R0": None, "R1": None, "R2": None, "R3": None}
        prev = None
        save_state()  # Save the initial state
    else:
        with open(STATE_FILE, "r") as f:
            state = json.load(f)
            registers = state["registers"]
            prev = state["prev"]


def save_state():
    """Save the current state to a file."""
    with open(STATE_FILE, "w") as f:
        json.dump({"registers": registers, "prev": prev}, f)


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
@click.argument("a", type=str)
@click.argument("b", type=str)
def add(a, b):
    """Add two numbers."""
    load_state()
    a = maybe_dereference(a)
    b = maybe_dereference(b)
    if a is None or b is None:
        click.echo("Error: Invalid input.")
        return
    result = a + b
    store_result(result)
    save_state()


@cli.command()
@click.argument("a", type=str)
@click.argument("b", type=str)
def subtract(a, b):
    """Subtract two numbers."""
    load_state()
    a = maybe_dereference(a)
    b = maybe_dereference(b)
    if a is None or b is None:
        click.echo("Error: Invalid input.")
        return
    result = a - b
    store_result(result)
    save_state()


@cli.command()
@click.argument("a", type=str)
@click.argument("b", type=str)
def multiply(a, b):
    """Multiply two numbers."""
    load_state()
    a = maybe_dereference(a)
    b = maybe_dereference(b)
    if a is None or b is None:
        click.echo("Error: Invalid input.")
        return
    result = a * b
    store_result(result)
    save_state()


@cli.command()
@click.argument("a", type=str)
@click.argument("b", type=str)
def divide(a, b):
    """Divide two numbers."""
    load_state()
    a = maybe_dereference(a)
    b = maybe_dereference(b)
    if a is None or b is None:
        click.echo("Error: Invalid input.")
        return
    if b == 0:
        click.echo("Error: Division by zero.")
        return
    result = a / b
    store_result(result)
    save_state()


@cli.command()
@click.argument("a", type=str)
def sine(a):
    """Find the sine of an angle (in degrees)."""
    load_state()
    a = maybe_dereference(a)
    if a is None:
        click.echo("Error: Invalid input.")
        return
    result = math.sin(math.radians(a))
    store_result(result)
    save_state()


@cli.command()
@click.argument("a", type=str)
def cosine(a):
    """Find the cosine of an angle (in degrees)."""
    load_state()
    a = maybe_dereference(a)
    if a is None:
        click.echo("Error: Invalid input.")
        return
    result = math.cos(math.radians(a))
    store_result(result)
    save_state()


@cli.command()
@click.argument("a", type=str)
def tangent(a):
    """Find the tangent of an angle (in degrees)."""
    load_state()
    a = maybe_dereference(a)
    if a is None:
        click.echo("Error: Invalid input.")
        return
    result = math.tan(math.radians(a))
    store_result(result)
    save_state()


@cli.command()
@click.argument("src", type=click.STRING)
@click.argument("dst", type=click.Choice(["R0", "R1", "R2", "R3"]))
def mov(src, dst):
    """Move the value from the source register to the destination register."""
    load_state()
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
    save_state()


@cli.command()
@click.argument("register", type=click.Choice(["prev", "R0", "R1", "R2", "R3"]))
def view(register):
    """View the value in a register or 'prev'."""
    load_state()
    if register == "prev":
        click.echo(f"{register} = {prev}")
    else:
        click.echo(f"{register} = {registers[register]}")
    save_state()


if __name__ == "__main__":
    cli()
