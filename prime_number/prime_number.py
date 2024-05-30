from prime_number import ARG_ERROR, SUCCESS

from typing import Tuple

# implementation of the sieve of eratosthenes algorithm to generate a list of
# prime numbers between 2 and a given number (inclusive)


def sieve_of_eratosthenes(upper_range: int) -> Tuple[list[int], int]:
    """Generate a list of prime numbers between 2 and a given number."""
    if (upper_range < 2):
        return ([], ARG_ERROR)
    # create a boolean array from 0 to n and initialize all elements as True
    prime_cantidates = [True for _ in range(upper_range + 1)]
    prime_cantidates[0] = prime_cantidates[1] = False
    # track current prime number starting with first known prime number
    prime = 2
    # loop through the numbers from 2 to the square root of n
    while pow(prime, 2) <= upper_range:
        # check if we have marked current number as prime
        if prime_cantidates[prime] is True:
            # mark all multiples of prime as not prime
            for i in range(pow(prime, 2), upper_range + 1, prime):
                prime_cantidates[i] = False
        # move to the next number
        prime += 1
    return (prime_cantidates, SUCCESS)


# function to coervce an array of booleans to an array of prime numbers
# (true is prime, false is not prime)
def bool_array_to_prime_array(prime_cantidates: list[bool]) -> Tuple[list[int], int]:
    """Coerce an array of booleans to an array of prime numbers."""
    prime_numbers = []
    # add prime numbers to the list
    for p in range(2, len(prime_cantidates)):
        if prime_cantidates[p]:
            prime_numbers.append(p)
    return (prime_numbers, SUCCESS)


# function to check if a number is prime
def is_prime(number: int, upper_bound=None) -> Tuple[bool, int]:
    """Check if a number is prime."""
    if number < 2:
        return (False, SUCCESS)
    (prime_cantidates, sieve_status_code) = sieve_of_eratosthenes(
        upper_bound or number)
    if (sieve_status_code != SUCCESS):
        return ([], sieve_status_code)
    (prime_numbers, convert_status_code) = bool_array_to_prime_array(prime_cantidates)
    if (convert_status_code != SUCCESS):
        return ([], convert_status_code)
    if number in prime_numbers:
        return (True, SUCCESS)
    return (False, SUCCESS)


def is_prime_list(list_of_numbers: list[int]) -> Tuple[list[{int, bool}], int]:
    """Check if a list of numbers are prime."""
    if (len(list_of_numbers) == 0):
        return ([], SUCCESS)
    prime_cantidates = []
    for n in list_of_numbers:
        (prime, status_code) = is_prime(n)
        if (status_code != SUCCESS):
            return ([], status_code)
        prime_cantidates.append(prime)
    return ([{n: p} for n, p in zip(list_of_numbers, prime_cantidates)], SUCCESS)


# function to generate a list of prime numbers between two given
# numbers (default 2 for lower bound) inclusive
def prime_numbers_between(upper_bound: int, lower_bound: int = 2) -> Tuple[list[int], int]:
    """Generate a list of prime numbers between two given numbers."""
    if (upper_bound == lower_bound):
        (prime, prime_status_code) = is_prime(upper_bound)
        if (prime_status_code != SUCCESS):
            return ([], prime_status_code)
        if prime:
            return ([upper_bound], SUCCESS)
        return ([], SUCCESS)
    min_bound = min(lower_bound, upper_bound)
    (prime_cantidates, sieve_status_code) = sieve_of_eratosthenes(
        max(upper_bound, lower_bound))
    if (sieve_status_code != SUCCESS):
        return ([], sieve_status_code)
    (prime_numbers, convert_status_code) = bool_array_to_prime_array(prime_cantidates)
    if (convert_status_code != SUCCESS):
        return ([], convert_status_code)

    # get the first index that is greater than or equal to the lower bound
    index_of_lower_bound = next(
        (i for i, n in enumerate(prime_numbers) if n >= min_bound), 0)

    return (prime_numbers[index_of_lower_bound:], SUCCESS)

# cache file functions if we get there ###

# TODO function to generate a list of prime numbers between two given
# numbers (default 2 for lower bound) inclusive (starting from the last number in the cached list if it exists)
