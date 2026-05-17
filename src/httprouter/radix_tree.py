from typing import Self, override
from httprouter.lcs import lcs


class Trie:
    def __init__(self: Self):
        self.root: Node | None = None

    def dfs(self: Self):
        self._dfs(self.root or Node("", True), {})

    def _dfs(self: Self, cursor: Node, visted: dict[Node, int]):
        if cursor in visted:
            return
        visted[cursor] = 0
        print(cursor.prefix)
        for _, node in cursor.nodes.items():
            self._dfs(node, visted)

    def add(self: Self, word: str):
        self.root = self._add(self.root, word)

    def _add(self: Self, cursor: Node | None, word: str) -> Node:
        if cursor is None:
            cursor = Node(word, True)
            return cursor

        common_prefix_length = lcs(cursor.prefix, word)

        if common_prefix_length == 0:
            if len(word) > 0:
                if word[0] in cursor.nodes:
                    return self._add(cursor.nodes[word[0]], word)
                else:
                    cursor.nodes[word[0]] = Node(word, True)
            return cursor

        elif common_prefix_length == len(cursor.prefix) and common_prefix_length < len(
            word
        ):
            if word[common_prefix_length + 1] in cursor.nodes:
                return self._add(
                    cursor.nodes[word[common_prefix_length + 1]],
                    word[common_prefix_length:],
                )
            else:
                cursor.nodes[word[common_prefix_length + 1]] = Node(
                    word[common_prefix_length + 1 :], True
                )
            return cursor
        else:
            # Node split
            temp = Node(
                cursor.prefix[common_prefix_length:], False
            )  # Create a new node with the rest

            # Copy the nodes
            for k, v in cursor.nodes.items():
                temp.nodes[k] = v

            # Delete the nodes becouse the are copied
            cursor.nodes.clear()

            # Update the prefix
            cursor.prefix = cursor.prefix[:common_prefix_length]

            # Add the splited node
            cursor.nodes[temp.prefix[0]] = temp

            # Add the new node
            cursor.nodes[word[common_prefix_length:][0]] = Node(
                word[common_prefix_length:], True
            )

        return cursor


class Node:
    def __init__(self: Self, prefix: str, is_terminal: bool):
        self.prefix: str = prefix
        self.nodes: dict[str, Node] = {}
        self.is_terminal: bool = is_terminal

    @override
    def __repr__(self) -> str:
        return f"Node{self.prefix}"
