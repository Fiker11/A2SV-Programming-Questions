class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s2 = ''.join(ch for ch in s if ch.isalpha() or ch.isnumeric())

        return s2 == s2[::-1]
        