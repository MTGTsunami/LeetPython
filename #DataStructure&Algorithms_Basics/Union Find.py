class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.p[y]

