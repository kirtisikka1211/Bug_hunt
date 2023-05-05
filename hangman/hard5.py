#hard5
#The code defines a class PrimeGenerator that generates a list of prime numbers up to a given number n
class PrimeGenerator:
    def __init__(self n):
        self.n = n
    
    def generate_primes():
        primes = []
    for num in range(2, self.n+1):
        is_prime = True
            for i in range(2, int(num**0.5 + 1)):
            if num % i == 0:
                is_prime = False
            break
            if is_prime
            primes.append(num)
    return primes
