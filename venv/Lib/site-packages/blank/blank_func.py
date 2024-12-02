# -*- coding: utf-8 -*-


def reverse(value):
    if not isinstance(value, str):
        return None
    result = ''
    for i in reversed(range(len(value))):
        result += value[i]
    return result
