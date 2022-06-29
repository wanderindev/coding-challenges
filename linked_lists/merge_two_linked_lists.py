class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def merge_two_lists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        return dummy.next


# Test cases
sol = Solution()

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

merged_list = sol.merge_two_lists(list1, list2)

assert merged_list.val == 1
assert merged_list.next.val == 1
assert merged_list.next.next.val == 2
assert merged_list.next.next.next.val == 3
assert merged_list.next.next.next.next.val == 4
assert merged_list.next.next.next.next.next.val == 4

list1 = []

list2 = ListNode(0)

merged_list = sol.merge_two_lists(list1, list2)

assert merged_list.val == 0
