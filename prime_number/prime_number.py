# implementation of the sieve of eratosthenes algorithm to generate a list of prime numbers between 2 and a given number inclusive
def sieve_of_eratosthenes(upper_range: int) -> list[int]:
    """Generate a list of prime numbers between 2 and a given number inclusive."""
    # create a boolean array from 0 to n and initialize all elements as True
    prime_cantidates = [True for _ in range(upper_range + 1)]
    prime_cantidates[0] = prime_cantidates[1] = False
    # track current prime number
    prime = 2
    # loop through the numbers from 2 to the square root of n
    while prime * prime <= upper_range:
        # check if we have marked current number as prime
        if prime_cantidates[prime] == True:
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

# TODO function to generate a list of prime numbers between two given numbers (default 2 for lower bound) inclusive ignoring the cached list

# TODO function to check if a number is prime


### cache file functions if we get there ###

# TODO function to generate a list of prime numbers between two given numbers (default 2 for lower bound) inclusive (starting from the last number in the cached list if it exists)
