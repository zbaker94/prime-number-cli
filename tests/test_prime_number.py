from typer.testing import CliRunner
from prime_number import __appname__, __version__, cli, prime_number as prime

runner = CliRunner()

# unit tests for prime number functionality ###


# test the prime number generator (sieve of eratosthenes) for all
# numbers between 2 and 100
def test_sieve_of_eratosthenes():
    prime_cantidates = prime.sieve_of_eratosthenes(100)
    prime_count = filter(lambda x: x is True, prime_cantidates)
    # check that we have 25 prime numbers between 2 and 100
    assert len(list(prime_count)) == 25
    # check that known numbers are correct
    assert prime_cantidates[0] is False
    assert prime_cantidates[1] is False
    assert prime_cantidates[2] is True
    # check that we got the expected prime numbers
    assert prime.bool_array_to_prime_array(prime_cantidates) == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
        67, 71, 73, 79, 83, 89, 97
    ]


# test if 7 is prime
def test_is_prime_7():
    assert prime.is_prime(7) is True


# test if 9 is not prime
def test_is_prime_9():
    assert prime.is_prime(9) is False


# test if 1 is prime
def test_is_prime_1():
    assert prime.is_prime(1) is False


# test if 0 is prime
def test_is_prime_0():
    assert prime.is_prime(0) is False


# test a list of numbers to see if they are prime (all prime)
def test_is_prime_list_all_prime():
    assert prime.is_prime_list([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == [
        {2: True}, {3: True}, {5: True}, {7: True}, {11: True}, {13: True},
        {17: True}, {19: True}, {23: True}, {29: True}
    ]


# test a list of numbers to see if they are prime (all not prime)
def test_is_prime_list_all_not_prime():
    assert prime.is_prime_list([4, 6, 8, 9, 10, 12, 14, 15, 18, 21]) == [
        {4: False}, {6: False}, {8: False}, {9: False}, {10: False},
        {12: False}, {14: False}, {15: False}, {18: False}, {21: False}
    ]


# test a list of numbers to see if they are prime (mixed)
def test_is_prime_list_mixed():
    assert prime.is_prime_list([2, 4, 5, 6, 7, 9, 11, 12, 13, 15]) == [
        {2: True}, {4: False}, {5: True}, {6: False}, {7: True},
        {9: False}, {11: True}, {12: False}, {13: True}, {15: False}
    ]


# test a list of numbers to see if they are prime (empty)
def test_is_prime_list_empty():
    assert prime.is_prime_list([]) == []


# test an arbitrary range [7-82] for prime numbers
def test_prime_numbers_between():
    assert prime.prime_numbers_between(lower_bound=7, upper_bound=82) == [
        7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
        73, 79
    ]


# test an arbitrary inverted range [82-7] for prime numbers
def test_prime_numbers_between_inverted():
    assert prime.prime_numbers_between(lower_bound=82, upper_bound=7) == [
        7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
        73, 79
    ]


# test range [7900-7920] for prime numbers
def test_prime_numbers_between_7900_7920():
    assert prime.prime_numbers_between(lower_bound=7900, upper_bound=7920) == [
        7901, 7907, 7919
    ]


# integration tests for calling the cli with various arguments ###
# test calling the cli with no arguments
def test_no_args():
    result = runner.invoke(cli.app, [])
    assert result.exit_code == 2


# test calling the cli with the --version flag
def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert result.stdout == f"{__appname__} version {__version__}\n"


# test calling the cli with the lessthan param
def test_lessthan():
    result = runner.invoke(cli.app, ["lessthan", "100"])
    assert result.exit_code == 0
    assert result.stdout == "Finding all prime numbers less than or equal to 100...\nPrime numbers less than or equal to 100:  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]\n"


# test calling the cli with the prime_generator param
def test_prime_generator():
    result = runner.invoke(cli.app, ["prime-generator", "2", "100"])
    assert result.exit_code == 0
    assert result.stdout == "Finding all prime numbers between 2 and 100...\nPrime numbers between 2 and 100:  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]\n"

# TODO test calling the cli with the --check and --number flags

# TODO test calling the cli with the --check and --list flags


# Filesystem Tests if we get there

# TODO test reading and writing cache file

# TODO test parsing the cache file

# TODO test checking if the cache directory exists

# TODO test creating the cache directory

# TODO test checking if the cache file exists

# TODO test creating the cache file

# TODO test all cli commands with --no-cache flag
