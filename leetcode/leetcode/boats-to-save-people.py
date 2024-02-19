class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i = 0
        j = len(people)-1
        c = 0
        people.sort()
        while(j>=i):
            if people[i]+people[j]>limit:
                j-=1
            else:
                i+=1
                j-=1
            c+=1
        print(c)
        return c
                

        

       