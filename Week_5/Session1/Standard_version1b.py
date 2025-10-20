from collections import Counter

# ---------------------------- Problem 4 ------------------------------
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    
    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20 and all(letter.isalpha() or letter.isspace() for letter in new_catchphrase):
            self.catchphrase = new_catchphrase
            print("Catchphrase updated")
        else:
            print("Invalid catchphrase.")
        

# alice = Villager("Alice", "Koala", "guvnor")
# alice.set_catchphrase("sweet dreams")
# print(alice.catchphrase)
# alice.set_catchphrase("#?!")
# print(alice.catchphrase)


# ---------------------------- Problem 5 ------------------------------
    def add_item(self, item_name):
        validation = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]   
        if item_name in validation:
            self.furniture.append(item_name)

# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)
# alice.add_item("acoustic guitar")
# print(alice.furniture)
# alice.add_item("cacao tree")
# print(alice.furniture)
# alice.add_item("nintendo switch")
# print(alice.furniture)


# ---------------------------- Problem 6 ------------------------------
    def print_inventory(self):
        if self.furniture == []:
            print("Inventory empty")
        else:
            lst = Counter(self.furniture)
            print(", ".join(f"{k}:{v}" for k, v in lst.items()))                

# alice = Villager("Alice", "Koala", "guvnor")
# alice.print_inventory()
# alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
# alice.print_inventory()

# output:
# Inventory empty
# acoustic guitar:1, ironwood kitchenette:1, kotatsu:2


# ---------------------------- Problem 7 ------------------------------
class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []

def of_personality_type(townies, personality_type):
    return [n.name for n in townies if n.personality == personality_type]

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")
# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))


# ---------------------------- Problem 8 ------------------------------
class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor

def message_received(start_villager, target_villager):
    current = start_villager
    
    while current is not None:
        if current == target_villager:
            
            return True
        current = current.neighbor
        
    return False

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

# print(message_received(isabelle, kk_slider))
# print(message_received(kk_slider, isabelle))


# ---------------------------- Problem 9 ------------------------------
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Tom Nook --> Tommy
tom_nook = Node("Tom Nook")
tommy = Node("Tommy") 
tom_nook.next = tommy 
# print(tom_nook.value) 
# print(tom_nook.next.value) 
# print(tommy.value) 
# print(tommy.next) 


# ---------------------------- Problem 10 ------------------------------
# Tom Nook --> Timmy --> Tommy
timmy = Node("Timmy")
tom_nook.next = timmy
timmy.next = tommy
# print(tom_nook.value)
# print(tom_nook.next.value)
# print(timmy.value)
# print(timmy.next.value)
# print(tommy.value)
# print(tommy.next)


# ---------------------------- Problem 11 ------------------------------
# Timmy --> Tommy --> Saharah
tom_nook.next = None
timmy.next = tommy
saharah = Node("Saharah")
tommy.next = saharah
print(tom_nook.next) 
print(timmy.value) 
print(timmy.next.value)  
print(tommy.value) 
print(tommy.next.value)
print(saharah.value)  
print(saharah.next) 


# ---------------------------- Problem 12 ------------------------------
# Output: Isabelle -> Saharah -> C.J.
isabelle = Node("Isabelle")
saharah = Node("Saharah")
cj = Node("C.J.")

isabelle.next = saharah
saharah.next = cj

def print_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.value))
        current = current.next
    return "-> ".join(values)
           
print(print_list(isabelle))