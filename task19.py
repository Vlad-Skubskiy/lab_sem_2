from typing import List


def print_partition(block):
    partition = {}
    for i, b in enumerate(block[1:], start=1):
        if b not in partition:
            partition[b] = []
        partition[b].append(i)
    return list(partition.values())


def generate_partitions(n: int) -> List[List[List[int]]]:

    block = [0] + [1] * n
    forward = [False] + [True] * n
    next_block = [0] * (n + 1)
    prev_block = [0] * (n + 1)
    partitions = [print_partition(block)]

    j = n
    while j > 1:
        k = block[j]
        if forward[j] == True:
            if next_block[k] == 0:
                next_block[k] = j
                prev_block[j] = k
                next_block[j] = 0
            if next_block[k] > j or next_block[k] == 0:
                prev_block[j] = k
                next_block[j] = next_block[k]
                if next_block[j] != 0:
                    prev_block[next_block[j]] = j
                next_block[k] = j
            block[j] = next_block[k]
        else:
            block[j] = prev_block[k]
            if k == j:
                if next_block[k] == 0:
                    next_block[prev_block[k]] = 0
                else:
                    next_block[prev_block[k]] = next_block[k]
                    prev_block[next_block[k]] = prev_block[k]
        partitions.append(print_partition(block))
        j = n
        while j > 1 and ((forward[j] and block[j] == j) or (not forward[j] and block[j] == 1)):
            forward[j] = not forward[j]
            j -= 1
    return partitions

partitions_n4 = generate_partitions(4)
for p in partitions_n4:
    print(p)