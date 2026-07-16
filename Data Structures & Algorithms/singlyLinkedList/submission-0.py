class LinkNode:
    def __init__(self, val, nextNode=None):
        self.val = val
        self.nextNode = nextNode

class LinkedList:
    
    def __init__(self):
        self.head = LinkNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        i = 0
        curr = self.head.nextNode
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.nextNode
        return -1

    def insertHead(self, val: int) -> None:
        head_fake = self.head.nextNode
        new_head = LinkNode(val, head_fake)
        self.head.nextNode = new_head
        if self.tail == self.head:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        print(self.getValues())
        tail = self.tail
        new_tail = LinkNode(val)
        tail.nextNode = new_tail
        self.tail = new_tail

    def remove(self, index: int) -> bool:
        prev = self.head
        i = 0
        while prev.nextNode:
            if i == index:
                deleted = prev.nextNode
                prev.nextNode = deleted.nextNode
                if deleted == self.tail:
                    self.tail = prev
                return True
            i += 1
            prev = prev.nextNode
        
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.nextNode
        while curr:
            res.append(curr.val)
            curr = curr.nextNode
        return res
