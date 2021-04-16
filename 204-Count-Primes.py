class Solution:
    def countPrimes(self, n: int) -> int:
        # def isPrime(n):
        #     i=2
        #     while i**2<=n:
        #         if n%i==0:
        #             return False
        #         i+=1
        #     return True
        # instead of checking whether number is prime or not
        # can we mark the multiples of a prime number as non-prime
        
        # Sieve of Eratosthenes
        if n == 0 or n == 1:
            return 0
        isPrime = [True]*n
        isPrime[0], isPrime[1] = 0, 0
        i = 2
        for i in range(2, n):
            if i*i >= n:
                break # count i bigger than sqrt(n) is dupliciated
            if isPrime[i] == False:
                continue
            j = i
            while i*j<n:
                isPrime[i*j] = False
                j += 1
        return sum(isPrime)
        # space complexity is O(n)
        # time complexity is more tricky, and that is O(sqrt(n)log log n)
