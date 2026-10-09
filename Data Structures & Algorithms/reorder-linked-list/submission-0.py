# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = slow.next
        dummy = slow.next = None
        while prev:
            temp = prev.next
            prev.next = dummy
            dummy = prev
            prev = temp

        n1 = head
        n2 = dummy

        while n2:
            temp1 = n1.next
            temp2= n2.next

            n1.next = n2
            n2.next = temp1
            n1 = temp1
            n2 = temp2






