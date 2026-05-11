from .lcs import lcs


def test_longest_str():
    count = lcs("word", "wor")
    assert count == 3
