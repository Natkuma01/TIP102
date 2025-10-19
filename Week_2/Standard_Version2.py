from collections import Counter
# Problem 1
def remove_low_rated_destinations(destinations, rating_threshold):
    # dict = {}
    # for key, value in destinations.items():
    #     if value < rating_threshold:
    #         dict[key] = value
    # print(f"NEW dictionary is : {dict}")
    # for key, value in dict.items():
    #     destinations.pop(key)
    # return destinations

    # alternative approach:
    for key,value in list(destinations.items()):
        if value < rating_threshold:
            destinations.pop(key)
    return destinations
    
destinations = {"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}
#print(remove_low_rated_destinations(destinations, 4.0))

# Problem 2
def unique_souvenir_counts(souvenirs):
    frequency = Counter(souvenirs)
    check_unique = []
    for num in frequency.values():
        if num not in check_unique:
            check_unique.append(num)
        else:
            return False
    return True
souvenirs1 = ["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"]
#print(unique_souvenir_counts(souvenirs1)) 

# Problem 3
def decode_message(key, message):

# use join to remove all the spaces in the key
# create a dictionary to assign key[0] = 'a' - can consider using ACSII
# iterate the message. for character in the message, find the character == the key: value
# add the value to an empty string

    result = ""
    key = key.replace(" ", "")
    reference = {}
    lst = []
    acsii = 97
    for letter in key:
        if letter not in lst:
            lst.append(letter)
    for char in lst:
        reference[char] = acsii
        acsii += 1
    for char in message:
        if char == " ":
            result += " "
        else:
            result += chr(reference[char])
    return result
key1 = "the quick brown fox jumps over the lazy dog"
message1 = "vkbs bs t suepuv"
#print(decode_message(key1, message1))

# Problem 5
def is_route_covered(trips, start_dest, end_dest):
    needed = set(range(start_dest, end_dest + 1))
    print(f"needed : {needed}")

    # Remove covered destinations from the set
    for start, end in trips:
        for dest in range(start, end + 1):
            if dest in needed:
                needed.remove(dest)

    # If the set is empty, all destinations were covered
    return len(needed) == 0


trips1 = [[1, 2], [3, 4], [5, 6]]
start_dest1, end_dest1 = 2, 5

trips2 = [[1, 10], [10, 20]]
tart_dest2, end_dest2 = 21, 21

trips3 = [[1, 2], [3, 5]]
start_dest3, end_dest3 = 2, 5

# print(is_route_covered(trips1, start_dest1, end_dest1))
# print(is_route_covered(trips2, start_dest2, end_dest2))
# print(is_route_covered(trips3, start_dest3, end_dest3))

# Problem 6
def most_popular_even_destination(destinations):
    frequency = Counter(destinations)
    frequency = dict(sorted(frequency.items()))
    max_frequency = max(frequency.values())
    for key, value in frequency.items():
        if key % 2 == 0 and value == max_frequency:
            return key
    return -1
    
destinations1 = [0, 1, 2, 2, 4, 4, 1]
destinations2 = [4, 4, 4, 9, 2, 4]
destinations3 = [29, 47, 21, 41, 13, 37, 25, 7]

#print(most_popular_even_destination(destinations1))
#print(most_popular_even_destination(destinations2))
#print(most_popular_even_destination(destinations3))

# Problem 7
def is_valid_itinerary(itinerary):
    largest = max(itinerary)
    if len(itinerary) != largest+1:
        return False
    if itinerary.count(largest) != 2:
        return False
    return True
itinerary1 = [2, 1, 3]
itinerary2 = [1, 3, 3, 2]
itinerary3 = [1, 1]

# print(is_valid_itinerary(itinerary1))
# print(is_valid_itinerary(itinerary2))
# print(is_valid_itinerary(itinerary3))

# Problem 8
def find_attractions(tourist_list1, tourist_list2):
    common = set(tourist_list1).intersection(set(tourist_list2))
    common = list(common)
    temp = 0
    lst = []
    for letter in common:
        temp += tourist_list1.index(letter)
        temp += tourist_list2.index(letter)
        lst.append(temp)
        temp = 0
    new_dict = dict(zip(common, lst))
    smallest = min(new_dict.values())
    result = []
    for k , y in new_dict.items():
        if y == smallest:
            result.append(k)
    return result

    

tourist_list1 = ["Eiffel Tower","Louvre Museum","Notre-Dame","Disneyland"]
tourist_list2 = ["Colosseum","Trevi Fountain","Pantheon","Eiffel Tower"]

print(find_attractions(tourist_list1, tourist_list2))

tourist_list1 = ["Eiffel Tower","Louvre Museum","Notre-Dame","Disneyland"]
tourist_list2 = ["Disneyland","Eiffel Tower","Notre-Dame"]

print(find_attractions(tourist_list1, tourist_list2))

tourist_list1 = ["beach","mountain","forest"]
tourist_list2 = ["mountain","beach","forest"]

print(find_attractions(tourist_list1, tourist_list2))

