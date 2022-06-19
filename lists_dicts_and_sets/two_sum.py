class Solution:
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        comp = {}
        for index, num in enumerate(nums):
            if num in comp:
                return [comp[num], index]
            comp[target - num] = index
        return []


# Test cases
solution = Solution()

# Test cases
nums, target = [2, 7, 11, 15], 9
assert solution.two_sum(nums, target) == [0, 1]

nums, target = [2, 7, 11, 15], 15
assert solution.two_sum(nums, target) == []

nums, target = [-2, -4, 11, 15], 11
assert solution.two_sum(nums, target) == [1, 3]

nums, target = [0, -4, -7, 15], -7
assert solution.two_sum(nums, target) == [0, 2]
