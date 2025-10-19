from collections import Counter
# Problem 1
def lineup(artists, set_times):
    # create exmpty dict
    # use for loop, - i in rannge
    res_dict = {}
    for i in range (len(artists)):
        res_dict[artists[i]] = set_times[i]
    return res_dict

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]
#print(lineup(artists1, set_times1))

# Problem 2
def get_artist_info(artist, festival_schedule):
    if artist not in festival_schedule:
        return {"message" : "Artist not found"}
    else:
        return festival_schedule.get(artist)

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}
#print(get_artist_info("Blood Orange", festival_schedule)) 
#print(get_artist_info("Taylor Swift", festival_schedule))  

# Problem 3
def total_sales(ticket_sales):
    return sum(ticket_sales.values())
ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
#print(total_sales(ticket_sales))

# Problem 4
def identify_conflicts(venue1_schedule, venue2_schedule):
    # create new dict
    # check key
    # check value
    # if key: value same, add to new dict
    conflicts = {}
    for artist in venue1_schedule:
        if artist in venue2_schedule:
            if venue1_schedule.get(artist) == venue2_schedule.get(artist):
                conflicts[artist] = venue1_schedule.get(artist)
    return conflicts

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

#print(identify_conflicts(venue1_schedule, venue2_schedule))

# Problem 5
def best_set(votes):
    frequency = Counter(votes.values())
    result = max(frequency.values())
    for key in frequency:
        if frequency[key] == result:
            return key
votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}
#print(best_set(votes1))

# Problem 6
def max_audience_performances(audiences):
    frequency = Counter(audiences)
    highest = max(frequency.keys())
    for key, value in frequency.items():
        if key == highest:
            return key * value
audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]
#print(max_audience_performances(audiences1))
#print(max_audience_performances(audiences2))

# Problem 7
def max_audience_performances(audiences):
    in_order = sorted(audiences)
    frequency = in_order.count(in_order[-1])
    return in_order[-1] * frequency

audiences1 = [100, 200, 200, 150, 100, 250]
#print(max_audience_performances(audiences1))
 
# Problem 8
def num_popular_pairs(popularity_scores):
    # (n * n-1 ) / 2. ===> this is how many unique(index wise) pair can get
    # score 1 is 3 times: ( 3 * 3-1 ) / 2 ==> 3
    # score 2 is 1 time: cannot make any pair
    # score 3 is 2 times: only 1 unique pair
    # return 3 + 0 + 1
    frequency = Counter(popularity_scores)
    unique = 0
    for value in frequency.values():
        unique += (value * (value-1) / 2)
    return int(unique)
popularity_scores2 = [1, 2, 3, 1, 1, 3]
#print(num_popular_pairs(popularity_scores2))

# Problem 9
def find_stage_arrangement_difference(s, t):
    s_dict = {}
    t_dict = {}
    for index, value in enumerate(s):
        s_dict[value] = index
    for index, value in enumerate(t):
        t_dict[value] = index
    total = 0
    for key in s_dict:
        total += abs(s_dict[key] - t_dict[key])
    return total    
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]
#print(find_stage_arrangement_difference(s2, t2))

# Problem 10
def num_VIP_guests(vip_passes, guests):
    count = 0
    for i in guests:
        if i in vip_passes:
            count += 1
    return count
vip_passes1 = "aA"
guests1 = "aAAbbbb"
print(num_VIP_guests(vip_passes1, guests1))

# Problem 12
def sort_performers(performer_names, performance_times):
    i = 0
    new_dict = {}
    temp = max(performance_times)
    res = []
    for i in range (len(performer_names)):
        new_dict[performance_times[i]] = performer_names[i]
    for times, name in enumerate (new_dict):
        if times == temp:
            res.append(name)
        else. # FIX
performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]
print(sort_performers(performer_names2, performance_times2))
