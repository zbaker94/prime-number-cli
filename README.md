# Prime Number Command Line Interface
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