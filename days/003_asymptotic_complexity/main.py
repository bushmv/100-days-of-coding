import bisect
from functools import partial
import timeit
from typing import List, Set


# O(n)
def lin_search(arr: List[int], target: int) -> bool:
    return target in arr


# O(log N)
def bin_search(arr: List[int], target: int) -> bool:
    return bisect.bisect(arr, target, 0, len(arr))


# O(1)
def set_search(s: Set[int], target: int) -> bool:
    return target in s


# O(N ** 2)
def square_search(arr: List[int], target: int) -> bool:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False


def main() -> None:
    N = 100
    arr = [i for i in range(N)]
    # s = set(arr)
    target = N
    res = timeit.timeit(partial(lin_search, arr, target))
    print(res)


if __name__ == "__main__":
    main()
