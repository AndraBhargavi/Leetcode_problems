class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        for i in range(len(num)):
            while stack and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        if k > 0:
            stack = stack[:-k]
        result = ''.join(stack).lstrip('0')
        return result or "0"