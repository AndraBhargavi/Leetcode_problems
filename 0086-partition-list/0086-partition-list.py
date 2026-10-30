# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        s_head=ListNode(-1)
        g_head=ListNode(-1)
        smaller=s_head
        greater=g_head
        temp=head
        while temp:
            if temp.val<x:
                smaller.next=temp
                smaller=temp
            else:
                greater.next=temp
                greater=temp
            temp=temp.next
        smaller.next=g_head.next
        greater.next=None
        return s_head.next