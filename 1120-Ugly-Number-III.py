class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(a,b):
            return a if b==0 else gcd(b, a%b)
        
        def lcm(a,b):
            return a*b//gcd(a,b)
        
        def count(N,a,b,c):
            # given num, count the ugly number n's position
            # when num is not ugly, this will return the smallest n's position
            return N//a + N//b + N//c - N//lcm(a,b) - N//lcm(a,c) - N//lcm(b,c) + N//lcm(lcm(a,b),c)
        
        #then use binary search, and we want it to be great or equal to
        # in another word, we search for the left boundry
        l = 0
        r = n*min(a,b,c)
        while l<r:
            mid = (l+r)//2
            #l<=mid<r
            if count(mid,a,b,c) < n:
                l = mid+1
            else:# count>=n
                r = mid
        return r

    
                
        # l, r = 1, 2 * 10**9
        # x, y, z = a * b // math.gcd(a, b), b * c // math.gcd(b, c), a * c // math.gcd(a, c)
        # w = x * y // math.gcd(x, y)
        # ans = 0
        # while l <= r:
        #     mid = (l + r) // 2
        #     cnt = mid // a + mid // b + mid // c - mid // x - mid // y - mid // z + mid // w
        #     if cnt >= n:
        #         r = mid - 1
        #         if cnt == n:
        #             ans = mid
        #     else:
        #         l = mid + 1
        # return ans
