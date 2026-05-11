def lcs(one: str, two: str) -> int:
    largest = len(one)
    if len(two) > len(one):
        largest = len(two)
    count = 0
    for i in range(0, largest - 1):
        if one[i] == two[i]:
            count = count + 1
            continue
        else:
            break
    return count
