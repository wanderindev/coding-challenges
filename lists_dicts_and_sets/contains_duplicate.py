class Solution:
    def contains_duplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        checked_values = set()

        for num in nums:
            if num in checked_values:
                return True
            checked_values.add(num)
        return False


# Test cases
sol = Solution()
nums = [1, 2, 3, 1]
assert sol.contains_duplicate(nums)

nums = [1, 2, 3, 4]
assert not sol.contains_duplicate(nums)

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
assert sol.contains_duplicate(nums)
