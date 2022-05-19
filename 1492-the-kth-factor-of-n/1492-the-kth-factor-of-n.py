import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # n % i == 0
        big,small = [],[]
        
        for i in range(1,int(math.sqrt(n))+1):
            if n % i == 0:
                if i == n // i:
                    small.append(i)
                else:
                    small.append(min(i,n//i))
                    big.append(max(i,n//i))
                    
        big.reverse()
        all_factors = small + big
        
        if not len(all_factors) >= k:
            return -1
        
        return all_factors[k-1]
                