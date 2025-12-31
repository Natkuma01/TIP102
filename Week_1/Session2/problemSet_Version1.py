# Problem 1
def reverse_sentence(sentence):
    return sentence[::-1]
sentence = "tubby little cubby all stuffed with fluff"
# print(reverse_sentence(sentence))

# Problem 2
def goldilocks_approved(nums):
    n = len(nums)
    if n <= 2:
        return -1
    else:
        in_order = sorted(nums)
        nn = int(n/2)
        return nums[nn-1]
nums = [2, 1, 3]
# print(goldilocks_approved(nums))

# Problem 3
def delete_minimum_elements(hunny_jar_sizes):
    return sorted(hunny_jar_sizes)
hunny_jar_sizes = [5, 2, 1, 8, 2] 
# print(delete_minimum_elements(hunny_jar_sizes))

# Problem 4
def sum_of_digits(num):
    total_sum = 0
    while num > 0:
        total_sum += num % 10
        num //= 10
    return total_sum
num = 42367
# print(sum_of_digits(num))

# Problem 5
def final_value_after_operations(operations):
    res = 1
    for i in operations:
        if i == "bouncy" or i == "flouncy":
            res += 1
        else:
            res -= 1
    return res
operations = ["trouncy", "flouncy", "flouncy"]
#print(final_value_after_operations(operations))

# Problem 6
def is_acronym(words, s):
    res = ""
    for word in words:
        res += word[0]
    return res == s   
words = ["christopher", "robin", "milne"]
s = "crm"
#print(is_acronym(words, s))

# Problem 7
def make_divisible_by_3(nums):
    count = 0
    for num in nums:
        if num % 3 != 0:
            if (num+1) % 3 == 0 or (num-1) % 3 == 0:
                count += 1
    return count
nums = [3, 6, 9]
print(make_divisible_by_3(nums))

# Problem 8
def exclusive_elemts(lst1, lst2):
    combine = lst1 + lst2
    new = []
    for word in combine:
        if word not in new:
            new.append(word)
    return new
lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
#print(exclusive_elemts(lst1, lst2))

# Problem 9
def merge_alternately(word1, word2):
    i, j = 0, 0
    res = []
    while i < len(word1) and j < len(word2):
        res.append(word1[i])
        res.append(word2[j])
        i += 1
        j += 1
    if i < len(word1):
        res.append(word1[i:])
    if j < len(word2):
        res.append(word2[j:])
    return "".join(res)    
word1 = "hfa"
word2 = "eflump"
print(merge_alternately(word1, word2))

# Problem 10
def good_pairs(pile1, pile2, k):
    count = 0
    for i in range (len(pile1)):
        for j in range (len(pile2)):
            if pile1[i] % (pile2[j] * k) == 0:
                count += 1
    return count
pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))