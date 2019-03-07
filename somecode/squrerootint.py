def on(num):
    """
    find square root in O(n)
    :param num: int
    :return: int
    """
    for i in range(num+2):
        if i * i > num:
            return i - 1

def ologn(num):
    """
    in O(log(n))
    :param num: int
    :return: int
    """
    l = 0  # left
    r = num + 1  # right
    while l <= r:
        m = (l+r) // 2
        if m * m <= num < (m+1) * (m+1):
            return m
        elif num == (m+1) * (m+1):
            return m+1
        elif m * m > num:
            r = m - 1
        elif (m+1) * (m+1) < num:
            l = m + 1


for i in range(1, 10000, 1):
    if (ologn(i)-int(i**.5)) != 0:
        print(i)
print(on(i))