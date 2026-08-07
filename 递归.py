from unittest import result


def jc(n):
    if n >= 1:
        return n * jc(n - 1)
    else:
        return 1


result = jc(10)
print(result)