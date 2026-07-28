class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def lowerBound(nums, target):
            n = len(nums)
            low, high = 0, n - 1
            lb = n

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] >= target:
                    lb = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return lb

        def upperBound(nums, target):
            n = len(nums)
            low, high = 0, n - 1
            ub = n

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] > target:
                    ub = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return ub

        lb = lowerBound(nums, target)

        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]

        ub = upperBound(nums, target)

        return [lb, ub - 1]