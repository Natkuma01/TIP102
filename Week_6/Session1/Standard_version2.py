# Problem 1
class Node:
    def __init__(self, house, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# head = Node("Harry")
# ron = Node("Ron")
# hermione = Node("Hermione")
# head.next = ron
# ron.next = hermione

# print_linked_list(head)


# Problem 2 
def count_element(house_points, score):
    curr = house_points
    count = 0
    while curr:
        if curr.value == score:
            count += 1
        curr = curr.next
    return count

house_points = Node("Gryffindor", 600, 
                Node("Ravenclaw", 300,
                    Node("Slytherin", 500,
                        Node("Hufflepuff", 600))))                  

print(count_element(house_points, 600))

