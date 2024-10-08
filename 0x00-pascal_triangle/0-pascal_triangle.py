#!/usr/bin/python3
"""Module that has pascal_triangle method"""


def pascal_triangle(n):
    """Method for pascal's triangle"""
    res = [[1]]

    if (n <= 0):
        return []

    for i in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)

    return res
