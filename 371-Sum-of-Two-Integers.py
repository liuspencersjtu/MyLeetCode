class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
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