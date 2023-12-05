#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def prod(*nums):
    if nums:
        max_elem = max([abs(i) for i in nums])
        max_elem_index = [abs(i) for i in nums].index(max_elem)
        res = 1

        for i in nums[max_elem_index + 1 :]:
            res *= i
        return res
    else:
        return None


if __name__ == "__main__":
    print(prod(1, 2, 3, 100, 2, -105, 7, 4))
    print(prod())
