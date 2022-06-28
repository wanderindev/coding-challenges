class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverse_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_node = None
        curr_node = head

        while curr_node:
            next = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next
        return prev_node


# Test cases
sol = Solution()

input_list = ListNode(1)
input_list.next = ListNode(2)
input_list.next.next = ListNode(3)
input_list.next.next.next = ListNode(4)
input_list.next.next.next.next = ListNode(5)

reversed_list = sol.reverse_list(input_list)

assert reversed_list.val == 5
assert reversed_list.next.val == 4
assert reversed_list.next.next.val == 3
assert reversed_list.next.next.next.val == 2
assert reversed_list.next.next.next.next.val == 1

input_list = ListNode(1)
input_list.next = ListNode(2)

reversed_list = sol.reverse_list(input_list)

assert reversed_list.val == 2
assert reversed_list.next.val == 1
