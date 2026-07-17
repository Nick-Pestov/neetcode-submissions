class TrieNode:
    def __init__(self):
        self.children = [None] * 26 # for each letter and take advantage of ord(char) - ord('a') to acheive this
        self.isEndOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i] is None:
                cur.children[i] = TrieNode() # create one new branch
            cur = cur.children[i]
        cur.isEndOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i] is None:
                return False
            cur = cur.children[i]
        return cur.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if cur.children[i] is None:
                return False
            cur = cur.children[i]
        return True