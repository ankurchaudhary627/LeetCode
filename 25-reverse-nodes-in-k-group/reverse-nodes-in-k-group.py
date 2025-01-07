# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse a segment of the linked list
        def reverse_segment(start, end):
            prev = None
            curr = start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev  # New head of the reversed segment

        # Create a dummy node to simplify handling of the head
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Check if there are enough nodes left to form a group
            group_end = group_prev
            for _ in range(k):
                group_end = group_end.next
                if not group_end:
                    return dummy.next
            
            # Reverse the current group
            group_start = group_prev.next
            next_group_start = group_end.next
            group_end.next = None  # Temporarily break the list
            
            # Reverse the group and connect it back
            new_group_head = reverse_segment(group_start, None)
            group_prev.next = new_group_head
            group_start.next = next_group_start
            
            # Move the group_prev pointer for the next group
            group_prev = group_start