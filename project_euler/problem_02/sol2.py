"""
Problem:
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

    1,2,3,5,8,13,21,34,55,89,..

By considering the terms in the Fibonacci sequence whose values do not exceed
n, find the sum of the even-valued terms. e.g. for n=10, we have {2,8}, sum is
10.
"""


def solution(n):
    """Returns the sum of all fibonacci sequence even elements that are lower
    or equals to n.

    >>> solution(10)
    [2, 8]
    >>> solution(15)
    [2, 8]
    >>> solution(2)
    [2]
    >>> solution(1)
    []
    >>> solution(34)
    [2, 8, 34]
    """
    ls = []
    a, b = 0, 1
    while b <= n:
        if b % 2 == 0:
            ls.append(b)
        a, b = b, a + b
    return ls


if __name__ == "__main__":
    print(solution(int(input().strip())))
