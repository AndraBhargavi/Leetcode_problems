class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            elif len(stack)>=2 and i=='+':
                stack.append(stack[-1]+stack[-2])
            elif stack and i=='D':
                stack.append(stack[-1]*2)
            elif stack and i=='C':
                stack.pop()
        

        sum1=0
        while stack:
            sum1+=stack.pop()
        return sum1
        