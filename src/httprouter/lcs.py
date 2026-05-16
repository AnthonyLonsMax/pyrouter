def lcs(one: str, two: str) -> int:
    min_length = min(len(one), len(two))
    count = 0
    for i in range(0, min_length):
        if one[i] == two[i]:
            count = count + 1
            continue
        else:
            break
    return count
