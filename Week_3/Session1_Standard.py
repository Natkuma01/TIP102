# Problem 1
def is_valid_post_format(posts):
    temp = []
    for char in posts:
        if char == '(' or char == '[' or char == '{':
            temp.append(char)
        elif temp:
            if char == ')' and '(' not in temp:
                return False
            if char == ']' and '[' not in temp:
                return False
            if char == '}' and '{' not in temp:
                return False
    return True
# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))

# Problem 2     stack - FILO
def reverse_comments_queue(comments):
    stack = []
    for i in range (len(comments)):
        item = comments.pop()
        stack.append(item)
    return stack
# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

# Problem 3
# ===========** STRING IS IMMUTABLE **===============
def is_symmetrical_title(title):
    title = title.replace(" ", "").lower()
    original_title = title
    title_list = list(title)
    j = len(title) - 1
    i = 0
    while i < j:
        temp = title_list[i]
        title_list[i] = title_list[j]
        title_list[j] = temp
        j -= 1
        i += 1
    new = str("".join(title_list))
    return new == original_title
# print(is_symmetrical_title("A Santa at NASA"))
# print(is_symmetrical_title("Social Media"))    

## use less code but also use two-pointer method:
def is_symmetrical_title(title):
    title = title.replace(" ", "").lower()
    reversed_list = [''] * len(title)
    i = 0
    j = len(title) - 1
    while i < len(title):
        reversed_list[i] = title[j]
        i += 1
        j -= 1
    return ''.join(reversed_list) == title

# Problem 4 - add comment
def engagement_boost(engagements):
    squared_engagements = []                                    # create a new list
    
    for i in range(len(engagements)):                           # iterate each element in the list engagement
        squared_engagement = engagements[i] * engagements[i]    # assign the square of the element to variable: squared_engagement
        squared_engagements.append((squared_engagement, i))     # add squared_engagement to index i
    
    squared_engagements.sort(reverse=True)                      # if add print statement here, return None
    
    result = [0] * len(engagements)                             # create new list result = [0, 0, 0, 0, 0]
    position = len(engagements) - 1                             # start position at the last index of the result list
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result
print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))