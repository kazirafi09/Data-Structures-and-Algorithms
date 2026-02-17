class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        multiplier = 1
        curr = l1
        while curr:
            num1 += curr.val * multiplier
            multiplier *= 10
            curr = curr.next
            
        num2 = 0
        multiplier = 1
        curr = l2
        while curr:
            num2 += curr.val * multiplier
            multiplier *= 10
            curr = curr.next
            
        total = num1 + num2
        
        if total == 0:
            return ListNode(0)
            
        dummy = ListNode(0)
        curr = dummy
        while total > 0:
            digit = total % 10      
            curr.next = ListNode(digit) 
            curr = curr.next       
            total //= 10       
            
        return dummy.next