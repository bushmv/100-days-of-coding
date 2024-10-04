from functools import partial
import timeit
from typing import List


# (n - m + 1) * m => O(n * m)
# BEST O(n + m)
def naive_substr_search(t: str, p: str) -> int:
    for i in range(len(t) - len(p) + 1):
        j = 0
        while j < len(p) and t[i + j] == p[j]:
            j += 1
        if j == len(p):
            return i
    return -1


# O(m)
def build_pf(s: str) -> List[int]:
    pf = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = pf[j - 1]
        if s[i] == s[j]:
            j += 1
        pf[i] = j
    return pf


# O(n) + O(m) = O(n + m)
def KMP(t: str, p: str) -> int:
    pf = build_pf(p)
    j = 0
    for i in range(len(t)):  # O(n)
        while j > 0 and t[i] != p[j]:
            j = pf[j - 1]
        if t[i] == p[j]:
            j += 1  # max j = n
            if j == len(p):
                return i - j + 1
    return -1


def main() -> None:
    t = "abccabcabcabda"
    p = "abcabd"
    print(KMP(t, p))
    # t = "a" * 1000
    # p = "a" * 100 + "b"
    # ellapsed = timeit.timeit(partial(naive_substr_search, t, p), number=100)
    # print(ellapsed)

    # ellapsed = timeit.timeit(partial(KMP, t, p), number=100)
    # print(ellapsed)


if __name__ == "__main__":
    main()
