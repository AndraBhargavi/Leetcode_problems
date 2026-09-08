# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        temp1=head
        temp2=head.next
        while temp1 and temp2:
            val1=self.gcd(temp1.val,temp2.val)
            new_node=ListNode(val1)
            temp1.next=new_node
            new_node.next=temp2
            temp1=temp2
            temp2=temp1.next
        return head


    def gcd(self,a,b):
        
        while b:
            a,b=b,a%b
        return a
