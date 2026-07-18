class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(ch.lower() for ch in s if ch.isalnum())
        def func (s,left,right):
            if left>=right:
                return True
            if s[left] != s[right]:
                return False   

            return func(s, left +1 , right - 1)     
        return func(s, 0, len(s)-1)