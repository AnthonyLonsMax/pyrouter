from httprouter.radix_tree import Trie


def test_tree_add():
    ptrie = Trie()
    ptrie.add("word")
    ptrie.add("work")
    ptrie.add("wonderfull")
    ptrie.add("worry")
    ptrie.add("wallet")

    ptrie.dfs()
