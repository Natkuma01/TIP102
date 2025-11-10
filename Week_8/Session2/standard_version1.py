from collections import deque 

# Tree Node class and helper function for testing
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


# ---------------------- Problem 1 -------------------------
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def count_odd_splits(root):
    if root is None:
        return 0
    
    left_count = count_odd_splits(root.left)
    right_count = count_odd_splits(root.right)

    if root.val % 2 != 0:
        return 1 + left_count + right_count
    return left_count + right_count

values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

# print(count_odd_splits(monstera))
# print(count_odd_splits(None))   


# ---------------------- Problem 2 -------------------------
def find_flower(inventory, name):
    if inventory is None:
        return False
    
    if inventory.val == name:
        return True
    elif name < inventory.val:
        return find_flower(inventory.left, name)
    else:
        return find_flower(inventory.right, name)

values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

# print(find_flower(garden, "Lilac"))  
# print(find_flower(garden, "Sunflower")) 


# ---------------------- Problem 4 -------------------------
def add_plant(collection, name):
    if collection is None:
        return TreeNode(name)
    
    if name < collection.val:
        collection.left = add_plant(collection.left, name)
    else:
        collection.right = add_plant(collection.right, name)
    return collection


# values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
# collection = build_tree(values)

# print_tree(add_plant(collection, "Aloe"))


# ---------------------- Problem 5 -------------------------
class TreeNode:
    def __init__(self, val, key=None, left=None, right=None):
        self.val = val
        self.key = key 
        self.left = left
        self.right = right

def sort_plants(collection):
    result = []

    def inorder(node):
        if node:
            inorder(node.left)
            result.append((node.key, node.val))
            inorder(node.right)
    
    inorder(collection)
    return result
    

values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)

# print(sort_plants(collection))



# ---------------------- Problem 5 -------------------------
class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key      # Plant price
        self.val = val      # Plant name
        self.left = left
        self.right = right

def pick_plant(inventory, budget):
    if inventory.key < budget and inventory.right.key < budget:
        return inventory.right
    
    if budget < inventory.key:
        return pick_plant(inventory.left, budget)
    else:
        return pick_plant(inventory.right, budget)
    
values = [(50, "Fiddle Leaf Fig"), (25, "Monstera"), (70, "Snake Plant"), (15, "Aloe"), 
            (40, "Pothos"), (60, "Fern"), (80, "ZZ Plant")]
inventory = build_tree(values)

print(pick_plant(inventory, 50)) 
print(pick_plant(inventory, 25)) 
print(pick_plant(inventory, 15)) 


'''
Problem 6 solution
    if inventory is None:
        return None  # no plants here
    
    # If current node's price is >= budget, go left
    if inventory.key >= budget:
        return pick_plant(inventory.left, budget)
    
    # Otherwise, current node is < budget
    # Maybe there's a better candidate on the right
    right_candidate = pick_plant(inventory.right, budget)
    if right_candidate is not None:
        return right_candidate  # found a better one
    else:
        return inventory  # current node is the best so far

        '''