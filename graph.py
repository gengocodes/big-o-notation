class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

        # For undirected graph, also add reverse edge
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)

    def display(self):
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")

    # BFS traversal
    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        print("BFS traversal:")
        while queue:
            node = queue.pop(0)
            print(node, end=' ')
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()

    # DFS traversal
    def dfs_util(self, node, visited):
        visited.add(node)
        print(node, end=' ')
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        print("DFS traversal:")
        self.dfs_util(start, visited)
        print()

# Demo execution
if __name__ == '__main__':
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    g.add_edge('D', 'E')

    g.display()
    g.bfs('A')
    g.dfs('A')