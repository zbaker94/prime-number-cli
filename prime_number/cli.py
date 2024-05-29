"""This module provides the prime number cli."""
# weather/cli.py

from pathlib import Path
from typing import Optional

from prime_number import __appname__, __version__

from colorama import Fore

import typer

app = typer.Typer()

### Callbacks
def _version_callback(value: bool):
    if value:
        typer.echo(Fore.GREEN + f"{__appname__} version {__version__}")
        raise typer.Exit()

### Commands

# TODO callback to return a list of all prime numbers less than or equal to a given number

# TODO callback to return a list of prime numbers between two given numbers (inclusive)

# TODO callback to check if a single number is prime

# TODO callback to check if a list of numbers are prime


# main app callback for version
@app.callback()
def main(
    version: Optional[bool] = typer.Option(None, "--version", "-v", help="Show the app version and then exit.", callback=_version_callback, is_eager=True)
) -> None:
        # because we are forced to return None here and typer never actually calls this function, we can safely ignore this line from coverage
        None # pragma: no cover