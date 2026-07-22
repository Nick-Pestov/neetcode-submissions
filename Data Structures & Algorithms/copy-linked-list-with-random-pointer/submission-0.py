"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.map = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        if head in self.map:
            return self.map[head]
        copy = Node(head.val) # make a copy of the node
        self.map[head] = copy # create current mapping
        copy.next = self.copyRandomList(head.next) # recursively build out the mappings
        copy.random = self.map.get(head.random)
        return copy