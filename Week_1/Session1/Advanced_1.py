# Problem 1
def linear_search(items, target):
    for index, value in enumerate(items):
        if value == target:
            return index 
    return -1
items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny' 
#print(linear_search(items, target))

# Problem 2
def final_value_after_operations(operations):
    tigger = 1
    for i in operations:
        if i == "bouncy" or i == "flouncy":
            tigger += 1
        else:
            tigger -= 1
    return tigger
operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))

# Problem 3
def tiggerfy(word):
    if 't' in word:
        word = word.replace("t", "")
    return word
word = "eggplant"
print(tiggerfy(word))

# alternative Problem 3
def altTiggerfy(word):
    substring = ["t", "i", "gg", "er"]
    result = word
    for sub in substring:
        result = result.replace(sub, "")
        result = result.replace(sub.upper(), "")
    return result
word = "eggplant"
print(altTiggerfy(word))

# Problem 4
def non_decreasing(nums):
    count = 0
    n = len(nums)
    for i in range (n-1):
        if nums[i] > nums[i+1]:
            count += 1
            if count > 1:
                return False
            if i == 0 or nums[i - 1] < nums[i+1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i] 
    return True     
nums = [4, 2, 3]           
print(non_decreasing(nums))

# Problem 5
def find_missing_clues(clues, lower, upper):
    
clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))