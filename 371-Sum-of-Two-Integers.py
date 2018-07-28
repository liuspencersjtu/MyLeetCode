class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # This only works when both a and b is positive
        # but for java version, it works fine.
        def add(a,b):
            if b == 0:
                return a
            #XOR without carry-on
            sumadd = a ^ b
            carry = (a & b) << 1
            #print(carry,sumadd)
            #recurse with sum + carry
            return add(sumadd, carry)
        
        return add(a,b)