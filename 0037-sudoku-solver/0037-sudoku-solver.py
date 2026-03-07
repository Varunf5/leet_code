class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row=[set() for i in range(9)]
        col=[set() for i in range(9)]
        box=[set() for i in range(9)]
        dots=[]
        for i in range(9):
            for j in range(9):
                x=board[i][j]
                if x=='.':dots.append((i,j))
                else:
                    row[i].add(x)
                    col[j].add(x)
                    box[(i//3)*3+j//3].add(x)
        def fun(i):
            if i==len(dots):return True
            r,c=dots[i]
            bid=3*(r//3)+c//3
            for x in "123456789":
                if x not in row[r] and x not in col[c] and x not in box[bid]:
                    row[r].add(x);col[c].add(x);box[bid].add(x)
                    board[r][c]=x
                    if(fun(i+1)):return True
                    board[r][c]='.'
                    row[r].remove(x);col[c].remove(x);box[bid].remove(x)
            return False
        fun(0)