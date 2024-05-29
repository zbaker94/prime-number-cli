# Prime Number Command Line Interface
## Description
The purpose of this project was to satisfy the requirements of a code challenge.

The brief requirements for that challenge are as follows:
- use test-driven development to implement a prime number generator that
returns prime numbers in a given range (inclusive of the endpoints).
- allow the user to specify the prime number range via
the command line.
- provide unit tests that all
pass as well as provide 100% code coverage.
- use Git to track your progress.
- not use the isprime method from sympy.
- The code should handle inverse ranges such that 1-10 and 10-1 are equivalent.

My initial approach for this project was to (using TDD) implement the Sieve of Eratosthenes algorithm (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) for finding prime numbers. Based on my research, this algorithm is one of, if not the fastest, methods to find prime numbers (up to ~4 million). Given that the problem domain is a static set of numbers, I also initially intended to cache the results of running the algorithm on disk. Because the algorithm outputs a boolean list whose indeces represent their value and whose value represents whether they are prime, susequent lookups would be progressively faster when using the cache. As I progressed, I realized just how fast the Sieve algorithm is and because of that have not implemented the on-disk cache at this time. Even though the algorithm must start at 2 in order to work, it is still incredibly fast when used with arbitrary ranges.

That being said, I believe I have met all of the requirements of the challenge and hope to add additional options for other algorithms, benchmarking, and caching in the future.

### Install 
`pip install -r requirements.txt`
### Tests
`coverage run -m pytest` then
`coverage report -m` or `coverage html`
### Help
`python -m prime_number --help` or `python -m prime_number COMMAND --help`
## Usage Examples
#### Get all of the prime numbers from 2 to 10
`python -m prime_number lessthan 10`
#### Gett all of the prime numbers between 10 and 1000
`python -m prime_number prime-generator 10 1000`
#### check if 10432 is prime
`python -m prime_number is-prime 10432`
#### check if [122, 77, 3, 4] are prime
`python -m prime_number are-prime 122 77 3 4`