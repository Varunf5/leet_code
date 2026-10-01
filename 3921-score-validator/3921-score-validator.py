class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score=0
        counter=0
        for i in range(len(events)):
            if events[i]=="1":
                score+=1
            elif events[i]=="2":
                score+=2
            elif events[i]=="3":
                score+=3
            elif events[i]=="4":
                score+=4
            elif events[i]=="6":
                score+=6
            elif events[i]=="W":
                counter+=1
            elif events[i]=="WD":
                score+=1
            elif events[i]=="NB":
                score+=1
            if counter==10:
                break
        return [score,counter]

            
        