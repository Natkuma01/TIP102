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
print(count_digits(n))

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
print(move_zeroes(lst))

# Problem 6
def reverse_vowels(s):
    
s = "BATgirl"
print(reverse_vowels(s))