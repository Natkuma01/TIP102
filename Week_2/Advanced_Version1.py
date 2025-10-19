from collections import Counter
# Problem 1
def total_treasure(treasure_map):
    return sum(treasure_map.values())
treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}
#print(total_treasure(treasure_map2))

# Problem 2
def can_trust_message(message):
    message = message.replace(" ", "")
    message = set(message)
    return len(message) == 26   
message1 = "sphinx of black quartz judge my vow"
#print(can_trust_message(message1))

# Problem 3
def find_duplicate_chests(chests):
    res = []
    frequency = Counter(chests)
    for integer, times in frequency.items():
        if times == 2:
            res.append(integer)
    return res
chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
#print(find_duplicate_chests(chests1))

# Problem 4
def can_make_balanced(code):
    
code2 = "haha"
print(can_make_balanced(code2))