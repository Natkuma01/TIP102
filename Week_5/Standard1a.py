# ---------------------------- Problem 1 ------------------------------
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

# apollo = Villager("Apollo", "Eagle", "pah")

# print(apollo.name)  
# print(apollo.species)  
# print(apollo.catchphrase) 
# print(apollo.furniture) 


# ---------------------------- Problem 2 ------------------------------
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
bones = Villager("Bones", "Dog", "yip yip")
print(bones.greet_player("Tram"))


# ---------------------------- Problem 3 ------------------------------
bones = Villager("Bones", "Dog", "ruff it up!")
print(bones.greet_player("Samia"))


