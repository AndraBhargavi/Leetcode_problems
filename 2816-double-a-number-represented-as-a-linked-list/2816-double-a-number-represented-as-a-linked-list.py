# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head=self.reverse(head)
        temp=head
        prev=head
        carry=0
        sum1=0
        while temp:
            sum1=carry
            if temp:
                sum1+=temp.val+temp.val
            temp.val=sum1%10
            carry=sum1//10
            prev=temp
            temp=temp.next
        if carry:
            node=ListNode(carry)
            prev.next=node
        return self.reverse(head)
    def reverse(self,head):
        if head==None or head.next==None:
            return head
        new_head=self.reverse(head.next)
        front=head.next
        front.next=head
        head.next=None
        return new_head