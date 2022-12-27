class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}
        self.counter = 0


class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode(char)
            current = current.children[char]

        current.is_end = True
        current.counter += 1

    def search(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                return False
            else:
                current = current.children[char]

        return current.is_end

t = Trie()
t.insert("abc")
t.insert("abd")
t.insert("def")
t.insert("ijk")

print(t.search("abc"))
print(t.search("def"))
print(t.search("dek"))
print(t.search("qwe"))
