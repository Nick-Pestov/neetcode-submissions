class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for character in word:
            if character not in cur.children: # first time being added
                # add it
                cur.children[character] = TrieNode()
            # now recurse into it
            cur = cur.children[character]
        # finally end of the word
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for character in word:
            if cur.children[character] is None: # first time being added
                return False # never inserted, does not exist
            # now recurse into it
            cur = cur.children[character]
        # now just check if it is the end (it needs to be)
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for character in prefix:
            if cur.children[character] is None: # first time being added
                return False # never inserted, does not exist
            # now recurse into it
            cur = cur.children[character]
        # now just check if it is the end (it needs to be)
        return True
