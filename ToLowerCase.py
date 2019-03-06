//Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

class Solution:
    def toLowerCase(self, str: str) -> str:
        ans = ''
        for s in str:
            if ord(s) >= ord('A') and ord(s) <= ord('Z'):
                ans += chr(ord(s) - (ord('A') - ord('a')))
            else:
                ans += s
        return ans
