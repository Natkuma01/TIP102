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

