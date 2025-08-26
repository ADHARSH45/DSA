from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = defaultdict(set)
        c = defaultdict(set)
        b = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in r[i] or board[i][j] in c[j] or board[i][j] in b[(i//3,j//3)]:
                    return False
                else:
                    r[i].add(board[i][j])
                    c[j].add(board[i][j])
                    b[(i//3,j//3)].add(board[i][j])
        print(r,c,b)

        return True
    
    """
    give  a certain instance of a sodoku and find wheter is valid. it done by checking duplicates in row,column and in each sub boxes by using dictonary of hashsets.
    
    """
        