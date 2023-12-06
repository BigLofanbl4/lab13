#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def min_max_avg(**kwargs):
    if kwargs:
        values = []
        for value in kwargs.values():
            if isinstance(value, int) or isinstance(value, float):
                values.append(value)
        if len(values) == 0:
            print("No numeric arguments")
            return None
        min_value = min(values)
        max_value = max(values)
        avg_value = sum(values) / len(values)
        return min_value, max_value, avg_value
    else:
        return None


if __name__ == "__main__":
    print(min_max_avg(a=14, b=-2, c=[1, 2, 3], d="sda", e=105.3, f=-24.4))