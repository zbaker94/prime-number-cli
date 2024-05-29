"""This module provides the prime number cli."""
# weather/cli.py

from pathlib import Path
from typing import Optional

from prime_number import __appname__, __version__, prime_number as prime

from colorama import Fore

import typer

app = typer.Typer()


# Callbacks ###
def _version_callback(value: bool):
    if value:
        typer.echo(Fore.GREEN + f"{__appname__} version {__version__}")
        raise typer.Exit()


# Commands ###
# command to return a list of all prime numbers less than or
# equal to a given number
@app.command()
def lessthan(
    number: int = typer.Argument(
        2,
        help="The number to find all prime numbers less than or equal to.",
    )
):
    """Return a list of all prime numbers less than or equal to a given number."""
    typer.echo(
        Fore.YELLOW +
        f"Finding all prime numbers less than or equal to {number}...")
    prime_numbers = prime.prime_numbers_between(upper_bound=number)
    typer.echo(
        Fore.LIGHTMAGENTA_EX +
        f"Prime numbers less than or equal to {number}: {Fore.GREEN} {prime_numbers}"
    )


# TODO command to return a list of prime numbers between two given numbers (inclusive)
@app.command()
def prime_generator(
    lower_bound: int = typer.Argument(
        2,
        help="The lower bound of the range to find prime numbers between.",
    ),
    upper_bound: int = typer.Argument(
        3,
        help="The upper bound of the range to find prime numbers between.",
    )
):
    """Return a list of prime numbers between two given numbers (inclusive)."""
    typer.echo(
        Fore.YELLOW +
        f"Finding all prime numbers between {min(lower_bound, upper_bound)} and {max(upper_bound, lower_bound)}...")
    prime_numbers = prime.prime_numbers_between(
        lower_bound=lower_bound, upper_bound=upper_bound)
    typer.echo(
        Fore.LIGHTMAGENTA_EX +
        f"Prime numbers between {lower_bound} and {upper_bound}: {Fore.GREEN} {prime_numbers}"
    )


# command to check if a single number is prime
@app.command()
def is_prime(
    number: int = typer.Argument(
        2,
        help="The number to check if it is prime.",
    )
):
    """Check if a single number is prime."""
    if prime.is_prime(number):
        typer.echo(
            Fore.GREEN +
            f"{number} is a prime number."
        )
    else:
        typer.echo(
            Fore.RED +
            f"{number} is not a prime number."
        )


# command to check if a list of numbers are prime
@app.command()
def are_prime(
    numbers: list[int] = typer.Argument(
        help="The list of numbers to check if they are prime.",
    )
):
    """Check if a list of numbers are prime."""
    prime_list = prime.is_prime_list(numbers)
    for item in prime_list:
        for key, value in item.items():
            if value:
                typer.echo(
                    Fore.GREEN +
                    f"{key} is a prime number."
                )
            else:
                typer.echo(
                    Fore.RED +
                    f"{key} is not a prime number."
                )


# main app callback for version
@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version", "-v",
        help="Show the app version and then exit.",
        callback=_version_callback,
        is_eager=True
    )
) -> None:
    # because we are forced to return None here and typer never actually
    # calls this function, we can safely ignore this line from coverage
    None  # pragma: no cover
