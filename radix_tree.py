from typing import Self
from lcs import lcs


class Trie:
    def __init__(self: Self):
        self.root: Node = Node("", False)

    def add(self: Self, cursor: Node | None, word: str) -> Node:
        if word == "":
            return Node("", False)
        if cursor is None:
            cursor = Node(word, True)
            return cursor

        if not word[0] in cursor.nodes:
            cursor.nodes[word[0]] = Node(word, True)
            return cursor

        word = word[1:]
        cursor = cursor.nodes[word[0]]

        common_prefix_length = lcs(cursor.prefix, word)

        if common_prefix_length == 0:
            if len(word) > 0:
                cursor.nodes[word[0]] = Node(word, True)
            return cursor

        if common_prefix_length < len(cursor.prefix):
            # Node split
            temp = Node(
                cursor.prefix[common_prefix_length:], False
            )  # Le agrego la nalga
            for k, v in cursor.nodes.items():
                temp.nodes[k] = v
            cursor.nodes.clear()
            cursor.prefix = cursor.prefix[:common_prefix_length]
            cursor.nodes[temp.prefix[0]] = temp

            # Add the new node
            cursor.nodes[word[common_prefix_length:][0]] = Node(
                word[common_prefix_length:], True
            )

        if common_prefix_length == len(cursor.prefix):
            if common_prefix_length == len(word):
                cursor.is_terminal = True
                return cursor
            else:
                return self.add(
                    cursor.nodes[word[common_prefix_length + 1]],
                    word[common_prefix_length:],
                )

        return cursor


class Node:
    def __init__(self: Self, prefix: str, is_terminal: bool):
        self.prefix: str = prefix
        self.nodes: dict[str, Node] = {}
        self.is_terminal: bool = is_terminal
