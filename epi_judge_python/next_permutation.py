from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:

    if(len(perm) < 2):
        return []

    candidate = len(perm) - 1

    while candidate >= 0:
        candidate -= 1
        if (perm[candidate] < perm[candidate + 1]):
            break

    if(candidate < 0):
        return []
    
    swappable_index = candidate + 1
    for i in range(candidate + 1, len(perm)):
        if (perm[candidate] >= perm[i]):
            break
        swappable_index = i
    
    perm[candidate], perm[swappable_index] = perm[swappable_index], perm[candidate]

    return perm[:candidate + 1] + perm[len(perm):candidate:-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
