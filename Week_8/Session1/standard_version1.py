#Problem 1
from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

    # def createInOrderTraversal(root):
    #     result = []

    #     def inOrderHelper(node):
    #         if not node:
    #             return
    #         inOrderHelper(node.left)
    #         result.append(node.val)

# def print_tree(root):
#     if not root:
#         return "Empty"
#     result = []
#     queue = deque([root])
#     while queue:
#         node = queue.popleft()
#         if node:
#             result.append(node.val)
#             queue.append(node.left)
#             queue.append(node.right)
#         else:
#             result.append(None)
#     while result and result[-1] is None:
#         result.pop()
#     print(result)


# root = TreeNode("Poseidon")
# root.left = TreeNode("Atlantis")
# root.left.left = TreeNode("Coral")
# root.left.right = TreeNode("Pearl")
# root.right = TreeNode("Oceania")
# root.right.left = TreeNode("Kelp")
# root.right.right = TreeNode("Reef")
# # print_tree(root)
# ['Poseidon', 'Atlantis', 'Oceania', 'Coral', 'Pearl', 'Kelp', 'Reef']

# Problem 2

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

""" def mertwins(root):
    if root.left and root.right:
        return root.left.val == root.right.val
    
    return False

root1 = TreeNode("Mermother", TreeNode("Coral"), TreeNode("Coral"))
root2 = TreeNode("Merpapa", TreeNode("Calypso"), TreeNode("Coral"))
root3 = TreeNode("Merenby", None, TreeNode("Calypso"))
print(mertwins(root1))
print(mertwins(root2))
print(mertwins(root3)) """
""" 
# Problem 3
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def get_decision(root):
    if root.val == "OR":
        return root.left.val or root.right.val
    elif root.val == "AND":
        return root.left.val and root.right.val
    
    return False




expression1 = TreeNode("OR", TreeNode(True), TreeNode(False))

expression2 = TreeNode(False)

print(get_decision(expression1))
print(get_decision(expression2))
 """

# Problem 4
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def leftmost_path(root):
    result = []
    
    currNode = root
    result.append(currNode.val)
    while currNode.left:
        result.append(currNode.left.val)
        currNode = currNode.left
    
    return result


system_a = TreeNode("CaveA", 
                  TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")), 
                          TreeNode("CaveC", None, TreeNode("CaveF")))
system_b = TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))
print(leftmost_path(system_a))
print(leftmost_path(system_b))

# Nice working eith 