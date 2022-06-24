class Solution(object):
    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for bracket in s:
            if bracket in bracket_map:
                if stack and stack[-1] == bracket_map[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return not stack


# Test cases
sol = Solution()

assert sol.is_valid("()")
assert sol.is_valid("()[]{}")
assert not sol.is_valid("(]")
