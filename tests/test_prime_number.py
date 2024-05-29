from typer.testing import CliRunner
from prime_number import __appname__, __version__, cli, prime_number as prime

runner = CliRunner()

### unit tests for prime number functionality ###
# test the prime number generator (sieve of eratosthenes) for all numbers between 2 and 100
def test_sieve_of_eratosthenes():
    prime_cantidates = prime.sieve_of_eratosthenes(100)
    prime_count = filter(lambda x: x == True, prime_cantidates)
    # check that we have 25 prime numbers between 2 and 100
    assert len(list(prime_count)) == 25
    # check that known numbers are correct
    assert prime_cantidates[0] == False
    assert prime_cantidates[1] == False
    assert prime_cantidates[2] == True
    # check that we got the expected prime numbers
    assert prime.bool_array_to_prime_array(prime_cantidates) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# TODO test if 7 is prime

# TODO test if 9 is not prime

# TODO test if 1 is prime

# TODO test if 0 is prime

# TODO test a list of numbers to see if they are prime (all prime)

# TODO test a list of numbers to see if they are prime (all not prime)

# TODO test a list of numbers to see if they are prime (mixed)

# TODO test a list of numbers to see if they are prime (empty)

# TODO test an arbitrary range [7-82] for prime numbers

# TODO test an arbitrary inverted range [82-7] for prime numbers

# TODO test range [7900-7920] for prime numbers

### integration tests for calling the cli with various arguments ###
# test calling the cli with no arguments
def test_no_args():
    result = runner.invoke(cli.app, [])
    assert result.exit_code == 2

# test calling the cli with the --version flag
def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert result.stdout == f"{__appname__} version {__version__}\n"

# TODO test calling the cli with the --lessthan flag

# TODO test calling the cli with the --range flag

# TODO test calling the cli with the --check and --number flags

# TODO test calling the cli with the --check and --list flags

# TODO test calling the cli with the --help flag?

### Filesystem Tests if we get there

# TODO test reading and writing cache file

# TODO test parsing the cache file

# TODO test checking if the cache directory exists

# TODO test creating the cache directory

# TODO test checking if the cache file exists

# TODO test creating the cache file

# TODO test all cli commands with --no-cache flag
