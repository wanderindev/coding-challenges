class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            mid = (left_pointer + right_pointer) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right_pointer = mid - 1
            else:
                left_pointer = mid + 1
        return -1


# Test cases
sol = Solution()

nums = [-1, 0, 3, 5, 9, 12]
target = 9
assert sol.search(nums, target) == 4

nums = [-1, 0, 3, 5, 9, 12]
target = 2
assert sol.search(nums, target) == -1
