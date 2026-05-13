from typing import Self
from lcs import lcs


class Trie:
    def __init__(self: Self):
        self.root: Node = Node("", False)

    def add(self: Self, cursor: Node, word: str):
        if word == "":
            return

        if not word[0] in cursor.nodes:
            cursor.nodes[word[0]] = Node(word, True)
            return

        word = word[1:]
        cursor = cursor.nodes[word[0]]

        common_prefix_length = lcs(cursor.prefix[1:], word)

        if common_prefix_length == 0:
            if len(word) > 0:
                cursor.nodes[word[0]] = Node(word, True)
                return

        if common_prefix_length < len(cursor.prefix):
            pass

        if common_prefix_length == len(word):
            cursor.is_terminal = True
            return


class Node:
    def __init__(self: Self, prefix: str, is_terminal: bool):
        self.prefix: str = prefix
        self.nodes: dict[str, Node] = {}
        self.is_terminal: bool = is_terminal
