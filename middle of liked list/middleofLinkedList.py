# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Traverse the list using slow and fast pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow will be pointing to the middle node
        return slow


        