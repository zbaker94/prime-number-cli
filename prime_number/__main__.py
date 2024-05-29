"""prime_number entry point script."""

from prime_number import cli, __appname__


def main() -> None:
    cli.app(prog_name=__appname__)


if __name__ == "__main__":
    main()
