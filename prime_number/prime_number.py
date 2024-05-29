# implementation of the sieve of eratosthenes algorithm to generate a list of
# prime numbers between 2 and a given number (inclusive)
def sieve_of_eratosthenes(upper_range: int) -> list[int]:
    """Generate a list of prime numbers between 2 and a given number."""
    # create a boolean array from 0 to n and initialize all elements as True
    prime_cantidates = [True for _ in range(upper_range + 1)]
    prime_cantidates[0] = prime_cantidates[1] = False
    # track current prime number starting with first known prime number
    prime = 2
    # loop through the numbers from 2 to the square root of n
    while prime * prime <= upper_range:
        # check if we have marked current number as prime
        if prime_cantidates[prime] is True:
            # mark all multiples of prime as not prime
            for i in range(prime * prime, upper_range + 1, prime):
                prime_cantidates[i] = False
        # move to the next number
        prime += 1
    return prime_cantidates


# function to coervce an array of booleans to an array of prime numbers
# (true is prime, false is not prime)
def bool_array_to_prime_array(prime_cantidates: list[bool]) -> list[int]:
    """Coerce an array of booleans to an array of prime numbers."""
    prime_numbers = []
    # add prime numbers to the list
    for p in range(2, len(prime_cantidates)):
        if prime_cantidates[p]:
            prime_numbers.append(p)
    return prime_numbers


# function to check if a number is prime
def is_prime(number: int, upper_bound=None) -> bool:
    """Check if a number is prime."""
    if number < 2:
        return False
    prime_cantidates = sieve_of_eratosthenes(upper_bound or number)
    prime_numbers = bool_array_to_prime_array(prime_cantidates)
    if number in prime_numbers:
        return True
    return False


def is_prime_list(list_of_numbers: list[int]) -> list[{int, bool}]:
    """Check if a list of numbers are prime."""
    if (len(list_of_numbers) == 0):
        return []
    prime_cantidates = [is_prime(n) for n in list_of_numbers]
    return [{n: p} for n, p in zip(list_of_numbers, prime_cantidates)]


# function to generate a list of prime numbers between two given
# numbers (default 2 for lower bound) inclusive
def prime_numbers_between(upper_bound: int, lower_bound: int = 2) -> list[int]:
    """Generate a list of prime numbers between two given numbers."""
    min_bound = min(lower_bound, upper_bound)
    prime_cantidates = sieve_of_eratosthenes(max(upper_bound, lower_bound))
    prime_numbers = bool_array_to_prime_array(prime_cantidates)

    # get the first index that is greater than or equal to the lower bound
    index_of_lower_bound = next(
        (i for i, n in enumerate(prime_numbers) if n >= min_bound), None)

    return prime_numbers[index_of_lower_bound:]

# cache file functions if we get there ###

# TODO function to generate a list of prime numbers between two given
# numbers (default 2 for lower bound) inclusive (starting from the last number in the cached list if it exists)
