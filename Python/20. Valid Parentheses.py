class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in (')', '}', ']'):
                if len(stack) == 0:
                    return False
                if stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if len(stack) > 0:
            return False
        else:
            return True