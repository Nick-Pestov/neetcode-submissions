class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost[0], cost[1])
        elif len(cost) == 3:
            return min(cost[0] + cost[2], cost[1])
        else:
            n1, n2 = cost[0], cost[1]
            for i in range(2, len(cost)):
                temp = min(n1, n2) + cost[i]
                n1 = n2
                n2 = temp
            return temp

            