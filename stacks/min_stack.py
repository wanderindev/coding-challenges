from collections import deque


class MinStack(object):
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        min_val = min(val, self.items[-1][1]) if not self.is_empty() else val
        self.items.append((val, min_val))

    def pop(self):
        """
        :rtype: None
        """
        if self.is_empty():
            return None
        return self.items.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        if self.is_empty():
            return None
        return self.items[-1][0]

    def get_min(self):
        """
        :rtype: int
        """
        if self.is_empty():
            return None
        return self.items[-1][1]


# Test cases
stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)

assert stack.get_min() == -3
assert stack.pop() == -3
assert stack.top() == 0
assert stack.get_min() == -2
