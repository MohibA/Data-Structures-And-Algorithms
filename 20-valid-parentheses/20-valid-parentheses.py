class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        
        paranthesis_key_value = {")":"(", "]":"[", "}":"{"}
        
        if len(s) <= 1:
            return False

        for c in s:
            if c in paranthesis_key_value:
                if stack and stack[-1] == paranthesis_key_value[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        