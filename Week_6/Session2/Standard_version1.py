# Problem 1
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
 
# def is_circular(clues):
#     curr = clues
#     while curr:
#         if curr.next != clues:
#               return True
#     return False

# clue1 = Node("The stolen goods are at an abandoned warehouse")
# clue2 = Node("The mayor is accepting bribes")
# clue3 = Node("They dumped their disguise in the lake")
# clue1.next = clue2
# clue2.next = clue3
# clue3.next = clue1

# print(is_circular(clue1))

# Problem 2 
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_false_evidence(evidence):
    res = []
    curr = evidence
    slow = fast = curr

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            start = fast
            while True:
                res.append(fast.value)
                fast = fast.next
                if fast == start:
                    break
            break
    
    return res

clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))

# Problem 3
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def partition(suspect_ratings, threshold):
    curr = suspect_ratings
    while curr:
        pass

suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(suspect_ratings, 3))