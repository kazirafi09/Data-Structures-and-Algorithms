# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        reversed_list = None
        cur = head
        while cur is not None:
            next_node = cur.next
            cur.next = reversed_list
            reversed_list = cur      
            cur = next_node         
        return reversed_list      