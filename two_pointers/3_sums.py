class Solution(object):
    def two_sum(self, nums, i, results):
        left_pointer = i + 1
        right_pointer = len(nums) - 1

        while left_pointer < right_pointer:
            total = nums[i] + nums[left_pointer] + nums[right_pointer]
            if total > 0:
                right_pointer -= 1
            elif total < 0:
                left_pointer += 1
            else:
                results.append(
                    [nums[i], nums[left_pointer], nums[right_pointer]]
                )
                left_pointer += 1
                right_pointer -= 1
                while (
                    left_pointer < right_pointer
                    and nums[left_pointer] == nums[left_pointer - 1]
                ):
                    left_pointer += 1

    def three_sum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                self.two_sum(nums, i, results)
        return results


# Test cases
sol = Solution()

nums = [-1, 0, 1, 2, -1, -4]
assert sol.three_sum(nums) == [[-1, -1, 2], [-1, 0, 1]]

nums = []
assert sol.three_sum(nums) == []

nums = [0]
assert sol.three_sum(nums) == []

nums = [-2, 0, 1, 1, 2]
assert sol.three_sum(nums) == [[-2, 0, 2], [-2, 1, 1]]
