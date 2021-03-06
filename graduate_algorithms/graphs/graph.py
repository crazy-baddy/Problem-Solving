class Graph:
    def __init__(self, v):
        self.v = v
        self.e = 0
        self.adj = [[] for _ in range(v)]

    def V(self):
        return self.v

    def E(self):
        return self.e

    def add_edge(self, v, w):
        self.adj[v].append(w) 
        self.adj[w].append(v) 
        
