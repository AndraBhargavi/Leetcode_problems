class Solution:
    def isValid(self, s: str) -> bool:
        list1=[]
        for i in s:
            if i=='(':
                list1.append(')')
            elif i=='{':
                list1.append("}")
            elif i=='[':
                list1.append(']')
            elif list1 and i==list1[-1]:
                list1.pop()
            else:
                return False
        return len(list1)==0
            

        