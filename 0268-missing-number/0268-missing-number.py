class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        totalsum = sum(nums)
        expsum = n*(n+1)//2

        return expsum-totalsum
        