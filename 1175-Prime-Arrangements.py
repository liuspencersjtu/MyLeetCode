import math
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def is_prime(n):
            if (n % 2 == 0 and n > 2) or n==1:
                return False
            return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
        primes, nprimes = 0, 0
        for n in range(1,n+1):
            if is_prime(n):
                primes+=1
            else:
                val = n
                nprimes+=1
        return (math.factorial(primes) * math.factorial(nprimes))%(10**9+7)
