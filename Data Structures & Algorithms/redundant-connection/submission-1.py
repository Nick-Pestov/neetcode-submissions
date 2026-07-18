class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        def dfs(node, parent):
            if visit[node] == True: # already visited
                return True
            visit[node] = True # mark node as visited
            # start exploring other nodes
            for nei in adj[node]: # iterate through neighbours
                if parent == nei:
                    continue # previous node
                # dfs into each neighbour
                if dfs(nei, node): # mark current node as parent
                    return True # found a node again that appeared
            return False
        
        for u, v in edges:
            # populate neighbours
            adj[u].append(v)
            adj[v].append(u)
            visit = [False] * (n + 1)
            if dfs(u, -1):
                return [u, v]
        return []