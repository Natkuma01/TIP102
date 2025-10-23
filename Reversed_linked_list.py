# -------------------- REVERSED LINKED LIST ------------------------
"""
UNDERSTAND:
- this is a singly linked list
- nodes hold integer
class Node {
    value
    next
}
edge:
>> empty or single node LL
>> cycles? 
>> runtime and space const. 

MATCH:
- singly LL
- update the pointers => modify
- one pass
- multiple pointers
- no temp head needed

PLAN:

Example: 
Input: [1 -> 2 -> 3 -> 4 -> 5]      
Output: [5 -> 4 -> 3 -> 2 -> 1]

IMPLEMENT:
"""

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


"""
Problem: Return the middle node of a linked list, and if the length of the linked list is even number,
         return the second middle node

         (use slow fast method)
Example:
Input: [3, 8, 2, 7, 5]
Output: [2]
Input: [1, 2]
Output:[2]
"""



# -------------------------------------- INSERT NODE ----------------------------------
"""
Example 1: Insert in the middle
Input:
Linked list: 1 -> 2 -> 4
Insert value: 3
Position: 2

Output:
1 -> 2 -> 3 -> 4 -> None


Example 2: Insert in the middle of a two-node list
Input:
Linked list: 10 -> 20
Insert value: 15
Position: 1

Output:
10 -> 15 -> 20 -> None
"""
def insert(head, value, position):
    print(position, value)
    new_node = ListNode(value)
    
    if position == 0:
        new_node.next = head
        return new_node
    
    current = head
    for i in range (position-1):
        current = current.next
 
    new_node.next = current.next
    current.next = new_node
    
    return head


# ----------------------------------- CREATE LINKED LIST FROM A LIST -----------------------------------
"""
Example 1:

Input: nums = [1, 2, 3, 4, 5]
Output: 1 -> 2 -> 3 -> 4 -> 5 -> None


Example 2:
Input: nums = []
Output: None
"""
class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def create_linked_list(values):
    if not values:
        return None
        
    head = Node(values[0])
    curr = head
    for i in range(1, len(values)):
        new_node = Node(values[i])
        curr.next = new_node
        curr = new_node
    return head


# ------------------------------------------ DELETE NODE ---------------------------------
def delete_node(head, value):
    if head is None:                                            # Handle empty Linked List
        return None
    
    if head.data == value:                                      # Handle deletion of head node
        return head.next
    
    curr = head         
    while curr.next is not None:                                # Search for node to delete
        if curr.next == value:
            curr.next.data == curr.next.next                    # set the next node become the next next node, so skip one node
            return head                                         # early return after deletion
        curr = curr.next

    return head                                                 # if value not found, reutrn the original LL





"""
Example 1:
List A: 2 -> 3 -> 4
a1 = SinglyLinkedListNode(2)
a2 = SinglyLinkedListNode(3)
a3 = SinglyLinkedListNode(4)
a1.next = a2
a2.next = a3

List B: 5 -> 6 -> 8
b1 = SinglyLinkedListNode(5)
b2 = SinglyLinkedListNode(6)
b3 = SinglyLinkedListNode(8)
b1.next = b2
b2.next = b3

Output: 2 (head of List A, because List A has two primes: [2,3] while List B has one: [5])


Example 2:
List A: 7 -> 8 -> 9
a1 = SinglyLinkedListNode(7)
a2 = SinglyLinkedListNode(8)
a3 = SinglyLinkedListNode(9)
a1.next = a2
a2.next = a3

List B: 11 -> 12 -> 13
b1 = SinglyLinkedListNode(11)
b2 = SinglyLinkedListNode(12)
b3 = SinglyLinkedListNode(13)
b1.next = b2
b2.next = b3

Output: 7 (head of List A, because both have the same number of primes: [7] vs [11, 13] but we return head_a by default)
"""