class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # create the matrix of neighbours of each node
        n = len(edges)
        adjacent = [[] for _ in range(n + 1)] # keep 1 extra for the -1 case

        def dfs(node, parent):
            # case 1, if already explored, already a cycle:
            if visited[node] == True: # node is a number between 1 - n
                return True
            visited[node] = True # mark as visited in this iteration, meaning that if curr --> child_1 --> child_2 ... --> curr == True meaning return and cycle exists
            # iterate through neighbours
            for nei in adjacent[node]:
                # ignore parent
                if nei == parent: # prevents case of curr --> child --> curr (2 levels)
                    continue
                # recursively go through each child, upon first case, return true
                if dfs(nei, node):
                    return True
            return False # all children have unique nodes (no cycles)


        for u, v in edges: # iterate through each edge
            # add neighbours
            adjacent[u].append(v)
            adjacent[v].append(u)
            # now mark as unvisited for each possible combination
            visited = [False] * (n + 1) 
            # now check if the edge already exists in a cycle (we have it stored as both u --> v and v --> so only need to check one)
            if dfs(u, -1): # no parent and true only if it's in a cycle
                return [u, v]
        return []
