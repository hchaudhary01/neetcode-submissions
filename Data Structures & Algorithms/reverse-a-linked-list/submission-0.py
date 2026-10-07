class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        while head:
            cur=head
            head = head.next
            cur.next = dummy
            dummy = cur
        return dummy