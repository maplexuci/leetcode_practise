class Solution:
    def isPalindrome(self, x):
        self.x = x
        x = str(x)

        ls = [num for num in x]

        ls_rev = ls[::-1]

        if ls == ls_rev:
            return True
        else:
            return False
