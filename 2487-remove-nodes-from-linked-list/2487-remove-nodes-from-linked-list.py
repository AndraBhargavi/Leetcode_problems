# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        if head==None or head.next==None:
            return head
        head=self.reverse(head)
        prev=head
        maxi=prev.val
        temp=head.next
        while temp:
            if temp.val<maxi:
                temp=temp.next
            else:
                maxi=temp.val
                prev.next=temp
                prev=temp
                temp=temp.next
        prev.next=temp
        return self.reverse(head)


    def reverse(self,head):
        if head==None or head.next==None:
            return head
        new_head=self.reverse(head.next)
        front=head.next
        front.next=head
        head.next=None
        return new_head