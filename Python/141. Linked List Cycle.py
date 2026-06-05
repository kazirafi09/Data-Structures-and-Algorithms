# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return None
        visited = set()
        visited.add(head)
        while head.next != None:
            if head.next in visited:
                return True
            else:
                visited.add(head.next)
                head = head.next
        return False

        