from collections import Counter

# Problem 1
class Player():
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

player_one = Player("Yoshi", "Super Booper")

# print(player_one.character)
# print(player_one.kart)
# print(player_one.items)


# Problem 2
class Player():
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
    def get_player(self):
        return f"{self.character} driving the {self.kart}"
player_one = Player("Yoshi", "Super Booper")
player_two = Player("Bowser", "Pirahna Prowler")

print(f"Match: {player_one.get_player()} vs {player_two.get_player()}")

print(player_two.character)
print(player_two.kart)
print(player_two.items)


# Problem 3
player_one.kart = "Dolphin Dasher"
# print(player_one.get_player())


# Problem 4
class Player():
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
        
    def set_character(self, name):
        validate = ["Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", "Bowser"]
        if name in validate:
            print("Character updated")
            self.character = name
        else:
            print("Invalid character")


player_three = Player("Donkey Kong", "Standard Kart")

player_three.set_character("Peach")
print(player_three.character)
player_three.set_character("Baby Peach")
print(player_three.character)

# Problem 5
class Player():
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
        
    def add_item(self, item_name):
        validate = ["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"]
        if item_name in validate:
            self.items.append(item_name)

player_one = Player("Yoshi", "Dolphin Dasher")

# print(player_one.items)

# player_one.add_item("red shell")
# print(player_one.items)

# player_one.add_item("super star")
# print(player_one.items)

# player_one.add_item("super smash")
# print(player_one.items)



# Problem 6
class Player():
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def print_inventory(self):
        if not self.items:
            print("Inventory empty")
        else:
            res = Counter(self.items)
            print(", ".join(f"{k}:{v}" for k, v in res.items()))

player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]
player_two = Player("Peach", "Dolphin Dasher")

# player_one.print_inventory()
# player_two.print_inventory()


# Problem 7
class Player():
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

def print_results(race_results):
        n = len(race_results)
        for i in range (n):
            print(f"{i+1}. {race_results[i].character}")

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]

# print_results(race_one)     


# Problem 8
# peach --> mario --> luigi
class Player:
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent
        
def get_rank(my_player):
    place = 1
    current = my_player
    while current.ahead:
        place += 1
        current = current.ahead
    return place
peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

print("---------- probem 8 ----------")
print(get_rank(luigi))
print(get_rank(peach))
print(get_rank(mario))


# Problem 9
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

cat = Node("Tom")
mouse = Node("Jerry")
cat.next = mouse

print("---------- probem 9 ----------")
print(cat.value)
print(cat.next)
print(cat.next.value)
print(mouse.value)
print(mouse.next)

# Problem 10
# dog --> cat --> mouse
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
dog.next = cat
cat.next = mouse

print("---------- probem 10 ----------")
print(dog.value)
print(dog.next)
print(dog.next.value)
print(cat.next)
print(cat.next.value)


# Problem 11 (remove a node)
# Current:   dog --> cat --> mouse
# Change to: cat --> mouse --> cheese
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")
dog.next = None
cat.next = mouse
mouse.next = cheese


# Problem 12
dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

def chase_list(head):
    current = head
    lst = []
    while current:
        lst.append(current.value)
        current = current.next
    return " chase ".join(lst)
    
print("---------- probem 12 ----------")
print(chase_list(dog))