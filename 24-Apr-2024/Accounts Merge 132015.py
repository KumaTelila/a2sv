# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_account = {}
        un = UnionFind(len(accounts))
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in email_to_account:
                    un.union(i, email_to_account[accounts[i][j]])
                else:
                    email_to_account[accounts[i][j]] = i
        email_group = defaultdict(list)
        for key, value in email_to_account.items():
            parent = un.find(value)
            email_group[parent].append(key)
        ans = []
        for key, val in email_group.items():
            name = accounts[key][0]
            ans.append([name]+ sorted(val))
        return ans
