class Solution(object):
    def max_area(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_volume = 0
        left_pointer = 0
        right_pointer = len(height) - 1

        while left_pointer < right_pointer:
            volume = (right_pointer - left_pointer) * min(
                height[left_pointer], height[right_pointer]
            )
            max_volume = max(max_volume, volume)
            if height[right_pointer] > height[left_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        return max_volume


# Test cases
sol = Solution()

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
assert sol.max_area(height) == 49

height = [1, 1]
assert sol.max_area(height) == 1
