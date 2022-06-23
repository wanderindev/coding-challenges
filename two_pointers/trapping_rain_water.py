class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_pointer = 0
        right_pointer = len(height) - 1
        left_max = 0
        right_max = 0
        trapped_water = 0

        while left_pointer < right_pointer:
            if height[left_pointer] <= height[right_pointer]:
                trapped_water += (
                    left_max - height[left_pointer]
                    if left_max - height[left_pointer] > 0
                    else 0
                )
                left_max = max(left_max, height[left_pointer])
                left_pointer += 1
            else:
                trapped_water += (
                    right_max - height[right_pointer]
                    if right_max - height[right_pointer] > 0
                    else 0
                )
                right_max = max(right_max, height[right_pointer])
                right_pointer -= 1
        return trapped_water


# Test cases
sol = Solution()

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# assert sol.trap(height) == 6

height = [4, 2, 0, 3, 2, 5]
assert sol.trap(height) == 9
