def count_stair_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)

def count_k(n, k):
    """This solution comes from the video"""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    total, i = 0, 1
    while i <= k:
        total += count_k(n-i, k)
        i += 1
    return total