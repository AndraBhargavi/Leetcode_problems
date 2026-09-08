# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        new_head=dummy
        temp1=head
        while temp1:
            if temp1.val not in nums:
                dummy.next=temp1
                dummy=dummy.next
            temp1=temp1.next
        dummy.next=None
        return new_head.next
                
        