class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors <= 2:
            return primeFactors
        
        MOD = pow(10,9) + 7
        
        if primeFactors % 3 == 0: return pow(3, primeFactors // 3)
        if primeFactors % 3 == 1: return 4 * pow(3, (primeFactors - 4)//2)
        return 2 * pow(3, (primeFactors - 2)//2)
