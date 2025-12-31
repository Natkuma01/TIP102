# Problem 1
def are_equivalent(word1, word2):
    res1 = "".join(word1)
    res2 = "".join(word2)
    return res1 == res2
word1  = ["cat", "wom", "an"]
word2 = ["catwoman"]
#print(are_equivalent(word1, word2))

# Problem 2
def count_evens(lst):
    count = 0
    for word in lst:
        if len(word) % 2 == 0:
            count += 1
    return count
lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
#print(count_evens(lst))

# problem 3
def remove_name(people, secret_identity):
    while secret_identity in people:
        people.remove(secret_identity)          # remove() return None
    return people
people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
secret_identity = 'Bruce Wayne'
#print(remove_name(people, secret_identity))   

# Problem 4
def count_digits(n):
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count
n = 964
# print(count_digits(n))

# Problem 5
def move_zeroes(lst):
    res = []
    zeros = lst.count(0)
    while 0 in lst:
        lst.remove(0)
    res += lst
    for i in range (zeros):
        res.append(0)
    return res
lst = [1, 0, 2, 0, 3, 0]
# print(move_zeroes(lst))

# Problem 6: Reverse Vowels of a String
# ********** REMIND: String is immutable *****************
def reverse_vowels(s):
    vowels = ['a', 'e', 'i', 'o' , 'u', 'A', 'E', 'I', 'O', 'U']
    s = list(s)
    left, right = 0, len(s)-1
    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] in vowels:
            right -= 1
        else:
            left += 1
    return ''.join(s)
         
s = "BATgirl"
print(reverse_vowels(s))


# Problem 7: Vantage Point
def highest_altitude(gain):
    current, max_altitude = 0, 0
    for num in gain:
        current += num
        max_altitude = max(max_altitude, current)
    return max_altitude
        
gain = [-5, 1, 5, 0, -7]
print(highest_altitude(gain))


# Problem 8: Left and Right Sum Differences
def left_right_difference(nums):
    left_sum = 0
    right_sum = sum(nums)
    res = []
    for num in nums:
        right_sum -= num
        res.append(left_sum - right_sum)
        left_sum += num
    return res
    
nums = [10, 4, 8, 3]
print(left_right_difference(nums))


# Problem 9: Common Cause
def common_elements(lst1, lst2):
    res = []
    for item in lst1:
        if item in lst2:
            res.append(item)
    return res

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["super speed", "time travel", "dimensional travel"]
print(common_elements(lst1, lst2))

# Problem 10: Exposing Superman
