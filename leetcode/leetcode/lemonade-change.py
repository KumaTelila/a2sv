class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        then = 0
        for i in bills:
            if i == 5:
                five+=1
            elif i == 10:
                five -=1
                then +=1
            else:
                five-=1
                then-=1
                if then < 0 and five >= 2:
                    then+=1
                    five-=2
            # print(i, five, then)
            if five < 0 or then < 0:
                return False
        return True
            

        