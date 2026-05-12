from typing import Self
from lcs import lcs


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

    def _add(self: Self, cursor: Node | None, word: str) -> Node:
        if cursor is None:
            return Node(word, True)
        if len(word) == 0:
            cursor.is_terminal = True
            return cursor
        common_prefix_legth = lcs(cursor.prefix, word)
        if common_prefix_legth == len(cursor.prefix):  # Avoid repetead words
            cursor.is_terminal = True
            return cursor
        remainding_word = cursor.prefix[common_prefix_legth:]

        # Copy the remainding nodes
        temp = Node(remainding_word, False)
        for k, v in cursor.nodes.items():
            temp.nodes[k] = v

        cursor.nodes.clear()
        cursor.prefix = cursor.prefix[:common_prefix_legth]
        cursor.nodes[remainding_word] = temp

        return self._add(cursor, word)


class Node:
    def __init__(self: Self, prefix: str, is_terminal: bool):
        self.prefix: str = prefix
        self.nodes: dict[str, Node] = {}
        self.is_terminal: bool = is_terminal


trie = Trie()

if trie.contains("marcos"):
    print("trie contains marco")
else:
    print("element not found")
