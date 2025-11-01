# Problem 1
def find_cruise_length(cruise_lengths, vacation_length):
    low = 0
    high = len(cruise_lengths) - 1

    while low <= high:
        mid = (low + high) // 2

        if cruise_lengths[mid] == vacation_length:
            return True
        elif cruise_lengths[mid] < vacation_length:
            low = mid + 1
        else :
            high = mid - 1

    return False

# print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))
# print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))

# Problem 2
def find_cabin_index(cabins, preferred_deck, left=0, right=None):
    if right is None: 
        right = len(cabins) - 1

    if left > right:
        return left
        
    mid = (left + right) // 2

    if cabins[mid] == preferred_deck:
        return mid
    elif cabins[mid] < preferred_deck:
        return find_cabin_index(cabins, preferred_deck, mid+1, right)
    else:
        return find_cabin_index(cabins, preferred_deck, left, mid-1)

# print(find_cabin_index([1, 3, 5, 6], 5))
# print(find_cabin_index([1, 3, 5, 6], 2))
# print(find_cabin_index([1, 3, 5, 6], 7))

# Problem 3
def count_checked_in_passengers(rooms):
    left = 0
    right = len(rooms) - 1

    while left <= right:
        mid = (left + right) // 2

        if rooms[mid] == 1:
            right = mid - 1
        else:
            left = mid + 1

    return len(rooms) - left

rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers(rooms1)) 
print(count_checked_in_passengers(rooms2))
print(count_checked_in_passengers(rooms3))

# Problem 4
def is_profitable(excursion_counts):
    pass

print(is_profitable([3, 5]))
print(is_profitable([0, 0]))