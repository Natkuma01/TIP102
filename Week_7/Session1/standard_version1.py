# Problem 1
def count_suits_iterative(suits):
    count = 0
    for _ in suits:
        count += 1
    return count    

def count_suits_recursive(suits):
    if not suits:
        return None
    return 1 + count_suits_iterative(suits[1:])

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))

# Problem 2
def sum_stones(stones):
    sum = 0
    for num in stones:
        sum += num
    return sum

def stones_recursive(stones):
    if not stones:
        return None
    return stones[0] + sum_stones(stones[1:])

print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))

# Problem 3
def count_suits_iterative(suits):
    seen = set()
    for suit in suits:
        seen.add(suit)
    return len(seen)
    

def count_suits_recursive(suits):

    if not suits: 
        return 0
    head = suits[0]
    lst = suits[1:]
    tail = [s for s in lst if s != head]

    return 1 + count_suits_recursive(tail)

print(count_suits_iterative(["Mark I", "Mark I", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

# Problem 4
def fibonacci_growth(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_growth(n-1) + fibonacci_growth(n-2)
    pass

print(fibonacci_growth(5))
print(fibonacci_growth(8))

# Problem 5
def power_of_four(n):
    if n == 0:
        return 0
    if n == 1:
        return 4
    if n < 0:
        return 1/power_of_four(-n)
    if n % 2 == 0:
        half_power = power_of_four(n // 2) #4^(n/2)^2
        return half_power * half_power
    
    return 4 * power_of_four(n-1) #4*4^(n-1)

# 4 ^ x 
# n is x.
# 4 ^ 2
# if n = 1 
# return 4
# poowerfour(n-1)

print(power_of_four(2))
print(power_of_four(-2))

# Problem 6
def strongest_avenger(strengths):
    if not strengths:
        return None
    else: 
        return strongest_avenger(strengths)

# print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
# print(strongest_avenger([50, 75, 85, 60, 90]))


# Problem 7
def count_deposits(resources):
    if len(resources) == 0:
        return 0
    else:
        count = 1 if resources[0] == 'V' else 0
        return count + count_deposits(resources[1:])

print(f"-------------------- Problem 7 --------------------")
print(count_deposits("VVVVV"))
print(count_deposits("VXVYGA"))


# Problem 8 
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

def merge_missions(mission1, mission2):
    # start at the mission1.next, check if mission2 head is > or < than mission1.next
    # if mission2 head > mission1.next, then mission1.next.next = mission2 head
    # else mission1.next = mission2 head
    pass                                


mission1 = Node(1, Node(2, Node(4)))
mission2 = Node(1, Node(3, Node(4)))

print_linked_list(merge_missions(mission1, mission2))