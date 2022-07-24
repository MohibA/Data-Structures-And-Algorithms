class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
       # index of previously a encountered prefix sum
        prefix_sums = {0: -1}
        
        max_len = prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum - k in prefix_sums:
                max_len = max(max_len, i - prefix_sums[prefix_sum - k])
            # don't override the index of the earliest encoutered prefix sum
            if prefix_sum not in prefix_sums:
                prefix_sums[prefix_sum] = i
        return max_len

        