# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev=ListNode(-1)
        temp=list1
        c=1
        while c<a:
            c+=1
            temp=temp.next
        prev=temp
        while c<=b+1:
            temp=temp.next
            c+=1
        prev.next=list2
        l2temp=list2
        while l2temp.next:
            l2temp=l2temp.next
        l2temp.next=temp
        return list1



        
            
        
        
        