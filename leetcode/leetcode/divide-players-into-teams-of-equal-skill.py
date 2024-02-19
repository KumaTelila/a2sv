class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i, j = 0, len(skill) -1
        if len(skill) == 2:
            return skill[0]*skill[1]
        sm = 0
        while i<j:
            if (skill[i] + skill[j]) == (skill[i+1] + skill[j-1]):
                sm+=(skill[i] *skill[j])
            else:
                return -1
            i+=1
            j-=1
        return sm
        