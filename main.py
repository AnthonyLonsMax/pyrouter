from typing import Self


class Trie:
    def __init__(self: Self):
        self.root: Node = Node(-1)

    def contains(self: Self, word: str):
        if word == "":
            return False
        c = ord(word[0])
        if not c in self.root.nodes:
            return False
        cursor = self.root.nodes[c]
        for index, char in enumerate(word[1:]):
            c = ord(char)
            if not c in cursor.nodes:
                return False
            else:
                cursor = cursor.nodes[c]
                continue
        if cursor.is_terminal:
            return True
        return False

    def add(self: Self, word: str):
        cursor = self.root
        for char in word:
            c = ord(char)
            if c in cursor.nodes:
                cursor = cursor.nodes[c]
                continue
            cursor.nodes[c] = Node(c)
            cursor = cursor.nodes[c]
        cursor.is_terminal = True


class Node:
    def __init__(self: Self, data: int):
        self.prefix: str = ""
        self.data: int = data
        self.nodes: dict[int, Node] = {}
        self.is_terminal: bool = False


trie = Trie()
trie.add("anthony")
trie.add("jose")
trie.add("marco")

if trie.contains("marcos"):
    print("trie contains marco")
else:
    print("element not found")
