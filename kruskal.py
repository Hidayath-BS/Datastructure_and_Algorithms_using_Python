class UnionFind:
    def __init__(self,n):
        self.parent =[i for i in range(n)]
        self.rank = [1] * n
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        root_x,root_y = self.find(x),self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] +=1
            return True
        return False
    
def kruskal(vertices,edge):
    edges.sort()
    uf = UnionFind(vertices)
    mst = []
    for weight, u, v in edges:
        if uf.union(u,v):
            mst.append((u,v,weight))
            if len(mst) == vertices -1:
                break
    return mst

edges = [(1,0,1),(3,0,2),(2,1,2),(5,1,3), (4,2,3), (6,3,4)]
vertices  = 5
mst = kruskal(vertices,edges)
print("edges in minimum spanning tree")
for u,v, weigh in mst:
    print(f"{u}---{v} == {weigh}")