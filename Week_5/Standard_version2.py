# Problem 1
class Player:
    def __init__(self, character, kart, outcomes):
        self.character = character
        self.kart = kart
        self.items = []
        self.race_outcomes = outcomes

    def get_tournament_place(self, opponents):
        my_avg = sum(self.race_outcomes) / len(self.race_outcomes)
        averages = [my_avg] + [sum(o.race_outcomes) / len(o.race_outcomes) for o in opponents]
        sorted_averages = sorted(averages)
        return sorted_averages.index(my_avg) + 1
        
            
player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3])
player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])

opponents = [player2, player3]
print(player1.get_tournament_place(opponents))    