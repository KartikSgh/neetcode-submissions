# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h = head
        n = 10**9+7
        while h:
            if h.val==n:
                return True
            h.val = n
            h = h.next
        return False