def binartSearch(input, target):
    low = 0
    high = len(input) - 1

    while low < high:
        mid = (low + high) // 2

        if input[mid] >= target:
            high = mid
        else:
            low = mid + 1
    
    if low < len(input) and input[low] == target:
        return low
    return -1

print(binartSearch([1, 3, 5, 7, 9, 11], 5))     # 2


def binartSearch1(input, target):
    low = 0
    high = len(input) - 1

    while low <= high:
        mid = (low + high) // 2

        if input[mid] == target:
            return mid
        elif target < input[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

print(binartSearch1([1, 3, 5, 7, 9, 11], 5)) 