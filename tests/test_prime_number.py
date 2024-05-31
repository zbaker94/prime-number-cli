from typer.testing import CliRunner
from prime_number import __appname__, __version__, cli, prime_number as prime, ARG_ERROR, SUCCESS

runner = CliRunner()

# unit tests for prime number functionality ###


# test the prime number generator (sieve of eratosthenes) for all
# numbers between 2 and 100
def test_sieve_of_eratosthenes():
    (prime_cantidates, sieve_status) = prime.sieve_of_eratosthenes(100)
    assert sieve_status == SUCCESS
    prime_count = filter(lambda x: x is True, prime_cantidates)
    # check that we have 25 prime numbers between 2 and 100
    assert len(list(prime_count)) == 25
    # check that known numbers are correct
    assert prime_cantidates[0] is False
    assert prime_cantidates[1] is False
    assert prime_cantidates[2] is True
    # check that we got the expected prime numbers
    (prime_numbers, convert_status) = prime.bool_array_to_prime_array(prime_cantidates)
    assert prime_numbers == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
        67, 71, 73, 79, 83, 89, 97
    ]
    assert convert_status == SUCCESS

# test the prime number generator (sieve of eratosthenes) for all
# numbers between 2 and 1 (invalid)


def test_sieve_of_eratosthenes_invalid_arg():
    (prime_cantidates, sieve_status) = prime.sieve_of_eratosthenes(1)
    assert sieve_status == ARG_ERROR


# test if 7 is prime
def test_is_prime_7():
    (is_prime, status_code) = prime.is_prime(7)
    assert is_prime is True
    assert status_code == SUCCESS


# test if 9 is not prime
def test_is_prime_9():
    (is_prime, status_code) = prime.is_prime(9)
    assert is_prime is False
    assert status_code == SUCCESS


# test if 1 is prime
def test_is_prime_1():
    (is_prime, status_code) = prime.is_prime(1)
    assert is_prime is False
    assert status_code == SUCCESS


# test if 0 is prime
def test_is_prime_0():
    (is_prime, status_code) = prime.is_prime(0)
    assert is_prime is False
    assert status_code == SUCCESS


# test a list of numbers to see if they are prime (all prime)
def test_is_prime_list_all_prime():
    (prime_list, status_code) = prime.is_prime_list(
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    assert prime_list == [
        {2: True}, {3: True}, {5: True}, {7: True}, {11: True}, {13: True},
        {17: True}, {19: True}, {23: True}, {29: True}
    ]
    assert status_code == SUCCESS


# test a list of numbers to see if they are prime (all not prime)
def test_is_prime_list_all_not_prime():
    (prime_list, status_code) = prime.is_prime_list(
        [4, 6, 8, 9, 10, 12, 14, 15, 18, 21])
    assert prime_list == [
        {4: False}, {6: False}, {8: False}, {9: False}, {10: False},
        {12: False}, {14: False}, {15: False}, {18: False}, {21: False}
    ]
    assert status_code == SUCCESS


# test a list of numbers to see if they are prime (mixed)
def test_is_prime_list_mixed():
    (prime_list, status_code) = prime.is_prime_list(
        [2, 4, 5, 6, 7, 9, 11, 12, 13, 15])
    assert prime_list == [
        {2: True}, {4: False}, {5: True}, {6: False}, {7: True},
        {9: False}, {11: True}, {12: False}, {13: True}, {15: False}
    ]
    assert status_code == SUCCESS


# test a list of numbers to see if they are prime (empty)
def test_is_prime_list_empty():
    (prime_list, status_code) = prime.is_prime_list([])
    assert prime_list == []
    assert status_code == SUCCESS


# test an arbitrary range [7-82] for prime numbers
def test_prime_numbers_between():
    (prime_range, status_code) = prime.prime_numbers_between(
        lower_bound=7, upper_bound=82)
    assert prime_range == [
        7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
        73, 79
    ]
    assert status_code == SUCCESS


# test an arbitrary inverted range [82-7] for prime numbers
def test_prime_numbers_between_inverted():
    (prime_range, status_code) = prime.prime_numbers_between(
        lower_bound=82, upper_bound=7)
    assert prime_range == [
        7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
        73, 79
    ]
    assert status_code == SUCCESS


# test prime numbers between with a bound < 2
def test_prime_numbers_between_invalid_bound():
    (empty_array, status_code) = prime.prime_numbers_between(1)
    assert empty_array == []
    assert status_code == ARG_ERROR


# test range where both bounds are the same [7-7] prime number
def test_prime_numbers_between_same_prime():
    (prime_range, status_code) = prime.prime_numbers_between(
        lower_bound=7, upper_bound=7)
    assert prime_range == [7]
    assert status_code == SUCCESS


# test range where both bounds are the same [4-4] non-prime number
def test_prime_numbers_between_same_not_prime():
    (prime_range, status_code) = prime.prime_numbers_between(
        lower_bound=4, upper_bound=4)
    assert prime_range == []
    assert status_code == SUCCESS


# test range [7900-7920] for prime numbers
def test_prime_numbers_between_7900_7920():
    (prime_range, status_code) = prime.prime_numbers_between(
        lower_bound=7900, upper_bound=7920)
    assert prime_range == [
        7901, 7907, 7919
    ]

    assert status_code == SUCCESS


# test range [0, 100] for prime numbers
def test_zero_lower_range():
    (prime_range, status_code) = prime.prime_numbers_between(
        lower_bound=0, upper_bound=100)
    assert prime_range == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    ]
    assert status_code == SUCCESS


# test range [100, 0] for prime numbers
def test_zero_upper_range():
    (prime_range, status_code) = prime.prime_numbers_between(
        lower_bound=100, upper_bound=0)
    assert prime_range == []
    assert status_code == ARG_ERROR


# test range [-5, 100] for prime numbers
def test_negative_lower_range():
    (prime_range, status_code) = prime.prime_numbers_between(
        lower_bound=-5, upper_bound=100)
    assert prime_range == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    ]
    assert status_code == SUCCESS


# test range [100, -5] for prime numbers
def test_negative_upper_range():
    (prime_range, status_code) = prime.prime_numbers_between(
        lower_bound=100, upper_bound=-5)
    assert prime_range == []
    assert status_code == ARG_ERROR


# test negative for both ranges
def test_negativeboth_range():
    (prime_range, status_code) = prime.prime_numbers_between(
        lower_bound=-100, upper_bound=-5
    )
    assert prime_range == []
    assert status_code == ARG_ERROR


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


def test_lessthan_invalid():
    result = runner.invoke(cli.app, ["lessthan", "1"])
    assert result.exit_code == 0
    assert result.stdout == "Finding all prime numbers less than or equal to 1...\nArgument Error\n"


# test calling the cli with the prime-generator param with a negative bound
def test_prime_generator_negative_bound():
    result = runner.invoke(cli.app, ["prime-generator", "--", "-2", "100"])
    assert result.exit_code == 0
    assert result.stdout == "Finding all prime numbers between -2 and 100...\nPrime numbers between -2 and 100:  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]\n"

# test calling the cli with the prime-generator param with a negative bound


def test_prime_generator_invalid_upper_bound():
    result = runner.invoke(cli.app, ["prime-generator", "2", "1"])
    assert result.exit_code == 0
    assert result.stdout == "Finding all prime numbers between 1 and 2...\nArgument Error\n"


# test calling the cli with the prime-generator param
def test_prime_generator():
    result = runner.invoke(cli.app, ["prime-generator", "2", "100"])
    assert result.exit_code == 0
    assert result.stdout == "Finding all prime numbers between 2 and 100...\nPrime numbers between 2 and 100:  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]\n"


# test calling the cli with the is-prime param with a prime number
def test_is_prime_true():
    result = runner.invoke(cli.app, ["is-prime", "7"])
    assert result.exit_code == 0
    assert result.stdout == "7 is a prime number.\n"


# test calling the cli with the is-prime param with a non-prime number
def test_is_prime_false():
    result = runner.invoke(cli.app, ["is-prime", "9"])
    assert result.exit_code == 0
    assert result.stdout == "9 is not a prime number.\n"


# test is_prime with invalid bound
def is_prime_invalid_number():
    result = runner.invoke(cli.app, ["is-prime", "1"])
    assert result.exit_code == 0
    assert result.stdout == "9 is not a prime number.\n"


# test calling the cli with the are-prime param with a list of prime numbers
def test_are_prime_true():
    result = runner.invoke(cli.app, ["are-prime", "2", "3", "5", "7"])
    assert result.exit_code == 0
    assert result.stdout == "2 is a prime number.\n3 is a prime number.\n5 is a prime number.\n7 is a prime number.\n"


# test calling the cli with the are-prime param with a list of non-prime numbers
def test_are_prime_false():
    result = runner.invoke(cli.app, ["are-prime", "4", "6", "8", "9"])
    assert result.exit_code == 0
    assert result.stdout == "4 is not a prime number.\n6 is not a prime number.\n8 is not a prime number.\n9 is not a prime number.\n"


# test calling the cli with the are-prime param with a mixed list of numbers
def test_are_prime_mixed():
    result = runner.invoke(
        cli.app, ["are-prime", "2", "4", "5", "6", "7", "9"])
    assert result.exit_code == 0
    assert result.stdout == "2 is a prime number.\n4 is not a prime number.\n5 is a prime number.\n6 is not a prime number.\n7 is a prime number.\n9 is not a prime number.\n"


# Filesystem Tests if we get there

# TODO test reading and writing cache file

# TODO test parsing the cache file

# TODO test checking if the cache directory exists

# TODO test creating the cache directory

# TODO test checking if the cache file exists

# TODO test creating the cache file

# TODO test all cli commands with --no-cache flag
