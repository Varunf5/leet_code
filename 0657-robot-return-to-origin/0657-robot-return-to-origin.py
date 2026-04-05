class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves=moves.strip()
        x=y=0
        for i in moves:
            if i not in "UDLR":
                return False
            if i=="R":x+=1
            elif i=="L":x-=1
            elif i=="D": y-=1
            elif i=="U" : y+=1
            else: continue
        return x==0 and y==0

        