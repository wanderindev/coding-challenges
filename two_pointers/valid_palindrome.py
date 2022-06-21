class Solution:
    def is_alpha_num(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )

    def is_palindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer:
            while left_pointer < right_pointer and not self.is_alpha_num(
                s[left_pointer]
            ):
                left_pointer += 1
            while left_pointer < right_pointer and not self.is_alpha_num(
                s[right_pointer]
            ):
                right_pointer -= 1
            if not s[left_pointer].lower() == s[right_pointer].lower():
                return False
            left_pointer += 1
            right_pointer -= 1
        return True


# Test cases
sol = Solution()

s = "A man, a plan, a canal: Panama"
assert sol.is_palindrome(s)

s = "race a car"
assert not sol.is_palindrome(s)

s = " "
assert sol.is_palindrome(s)

s = "OP"
assert not sol.is_palindrome(s)
