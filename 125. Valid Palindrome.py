class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        fp = 0
        sp = len(s) - 1
        while fp < sp:
            if s[fp] != s[sp]:
                return False
            else:
                fp += 1
                sp -= 1
        return True