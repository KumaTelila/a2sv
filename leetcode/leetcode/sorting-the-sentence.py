class Solution:
    def sortSentence(self, s: str) -> str:
       sent =  s.split()
       cop  = sent
       le = len(sent)
       lst = []
       ls1 = []
       for i in sent:
           a = int(i[-1])
           ls1.append(a)
           lst.append(i[:-1])
       j = 0;
       for i in ls1:
           cop[i-1] = lst[j]
           j+=1
       print(ls1)
       print(cop)
       st = " "
       st = st.join(cop)
       return st
      
