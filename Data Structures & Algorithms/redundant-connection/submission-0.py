class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # edge = []
        # go through the graph
        # 2 -> 1 connect 1 : {2}
        # 1 -> 3 connect and thus 2 -> 3 1: {2, 3}
        # 1 --> 4 connect and thus  1: {2, 3, 4}
        # 3 --> 4 connect --> 3: {4} <-- both exist in 1: {2, 3, 4}, edge = [3, 4]
        # 3--> 5 connect

        # idea, just build a connected graph, see which points connect to one another
        graph = set()
        res = []
        for (x, y) in edges:
            if x in graph and y in graph:
                res.append([x, y])
            graph.add(x)
            graph.add(y)
        return res[-1]