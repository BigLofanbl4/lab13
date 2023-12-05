#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def geom_mean_val(*nums):
    if nums:
        prod = 1
        for i in nums:
            prod *= i
        return prod ** (1 / len(nums))
    else:
        return None


if __name__ == "__main__":
    print(geom_mean_val(2, 2, 4))
    print(geom_mean_val())
