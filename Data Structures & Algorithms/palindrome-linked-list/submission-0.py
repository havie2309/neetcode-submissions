# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        if fast is not None:
            curr = slow.next
        else:
            curr = slow
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        l1 = head
        l2 = prev
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True
        

        