class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in '([{':
                stack.append({
                    '(': ')',
                    '{': '}',
                    '[': ']'
                }[char])
            else:
                if not stack or stack.pop() != char:
                    return False
        return not stack
