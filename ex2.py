#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def avg_harmonic(*nums):
    if nums:
        res = 0
        for i in nums:
            res += 1 / i
        return len(nums) / res
    else:
        return None


if __name__ == "__main__":
    print(avg_harmonic(3, 2, 1))
    print(avg_harmonic())
