class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        result = []
        remainingTotal = (mean *(n + len(rolls)) - sum(rolls))
        
        if remainingTotal < n or remainingTotal > n*6:
            return []
        
        while remainingTotal:
            dice = min(remainingTotal - n+1, 6)
            result.append(dice)
            n -= 1
            remainingTotal -= dice
        return result
        