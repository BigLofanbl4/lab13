#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def func(**info):
    for key, value in info.items():
        print("{}: {}".format(key, value))


if __name__ == "__main__":
    func(name="Apple", amount=12, price=10)