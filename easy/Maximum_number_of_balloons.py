from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a = Counter('balloon')
        b = Counter(text)

        res = len(text)

        for i in a:
            res = min(res,b[i] // a[i])
        return res

"""
Given a string.Want the maximum number of ballons that can be created from the string it can be done using hashmap and min function
"""