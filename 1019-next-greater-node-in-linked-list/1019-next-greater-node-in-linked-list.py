# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode | None) -> list[int]:
        ans=[]
        new_head=self.reverse(head)
        stack=[]
        temp=new_head
        while temp:
            
            while stack and stack[-1]<=temp.val:
                stack.pop()
            if len(stack)==0:
                ans.append(0)
            elif stack:
                ans.append(stack[-1])
            stack.append(temp.val)
            temp=temp.next
        return ans[::-1]


    
    def reverse(self,head):
        if head==None or head.next==None :
            return head
        new_head=self.reverse(head.next)
        front=head.next
        front.next=head
        head.next=None
        return new_head

        