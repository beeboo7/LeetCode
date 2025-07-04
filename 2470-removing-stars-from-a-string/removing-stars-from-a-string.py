class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str

        at * remove * and left
        """
        stack = []

        for char in s:
            if char == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)