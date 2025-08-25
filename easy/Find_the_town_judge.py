from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        t_count = [0]*(n + 1)

        if len(trust) == 0 and n == 1:
            return 1
        for i in trust:
            t_count[i[0]] -= 1
            t_count[i[1]] += 1
        print(t_count)
        for i in range(len(t_count)):
            if t_count[i] == n - 1:
                return i
        return -1
    """
    Here finding a person with zero trust to others but everyone trust this person means indegree is one less then total number of persons and outdegree is zero
    """