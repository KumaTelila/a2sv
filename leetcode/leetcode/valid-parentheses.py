class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if len(stack) > 0:
                top = stack[-1]
                if (top == '(' and i == ')') or (top == '{' and i == '}') or (top == '[' and i == ']'):
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return len(stack) == 0

        