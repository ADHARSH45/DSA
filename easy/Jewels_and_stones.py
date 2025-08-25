from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        out = 0
        a = Counter(jewels)
        for i in stones:
            if i in a:
                out = out + 1
        return out
        
    """
    Here return the number of stones that are in jewels done by creating a map of jewels and for each stone check whether it in the jewel map
    """