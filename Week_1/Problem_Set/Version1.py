# Problem 1: Hundred Acre Wood
def welcome(s):
    print(s)
s = "Welcome to The Hundred Acre Wood!"
print(welcome(s))


# Problem 2: Greeting
def greetings(name):
    return f"Welcom to The Hundred Acre Wood {name}! My name is Christopher Robin"
print(greetings("Michael"))


# Problem 3: Catchphrase
def print_catchphrase(character):
    data = {"pooh": "Oh, bother!",
            "Tigger": "TTFN: Ta-ta for now!",
            "Eeyore": "Thanks for noticing me",
            "Christopher Robin": "Silly old bear"}
    
    if character not in data:
        return f"Sorry! I don't know {character}'s catchphrase!"
    else:
        return data[character]
    
character = "piglet"
print(print_catchphrase(character))


# Problem 4: Return Item
def get_item(items, x):
    return items[x]
items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
print(get_item(items, x))


# Problem 5: Total Honey
def sum_honey(hunny_jars):
    return sum(hunny_jars)
hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))


# Problem 6: Double Trouble
def doubled(hunny_jars):
    for i in range (len(hunny_jars)):
        hunny_jars[i] = hunny_jars[i] * 2
    return hunny_jars
hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))


# Problem 7: Poohsticks
def count_less_than(race_times, threshold):
    count = 0
    for num in race_times:
        if num < threshold:
            count += 1
    return count
race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))


# Problem 8: Pooh's To Do's
def print_todo_list(task):
    result = ""
    for i in range (len(task)):
        result += f"{i+1}. {task[i]}. \n"
    return result
    
task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print(print_todo_list(task))


# Problem 9: Pairs
def can_pair(item_quantities):
    for num in item_quantities:
        if num % 2 != 0:
            return False
    return True
item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))


# Problem 10: Split Haycorns
def split_haycorns(quantity):
    res = []
    for i in range (1, quantity+1):
        if quantity % i == 0:
            res.append(i)
    return res
quantity = 6
print(split_haycorns(quantity))


# Problem 11: Thistle Hunt
def locate_thistles(items):
    res = []
    for i, value in enumerate(items):
        if value == "thistle":
            res.append(i)
    return res
items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))


# Problem 12: Goldilocks Number
def goldilocks_approved(nums):
    if len(nums) <= 2:
        return -1
    min_num = min(nums)
    max_num = max(nums)
    for num in nums:
        if num != max_num and num != min_num:
            return num
    return -1

nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))


# Problem 13: Count Vowels
def count_vowels(sentence):
    vowels = 'aeiou'

    # LIST COMPREHENSION
    # return sum(1 for char in sentence.lower() if char in vowels)

    sentence = sentence.lower()
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

sentence = "The quick brown fox jumps over the lazy dog"
print(count_vowels(sentence))


# Problem 14: Acronym
def is_acronym(words, s):
    check = ""
    for word in words:
        check += word[0]
    return check == s
words = ["christopher", "robin", "milne"]
s = "crm"
print(is_acronym(words, s))