class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if value <= root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
        return root

def is_complete(root, index, node_count):
    if root is None:
        return True
    if index >= node_count:
        return False
    return is_complete(root.left, 2 * index + 1, node_count) and \
           is_complete(root.right, 2 * index + 2, node_count)

def nodes_count(root):
    if root is None:
        return 0
    return 1 + nodes_count(root.left) + nodes_count(root.right)

def is_full(root):
    if root is None:
        return True
    if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
        return False
    return is_full(root.left) and is_full(root.right)

def is_perfect(root):
    if root is None:
        return True
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    return left_height == right_height and is_full(root)

def get_height(root):
    if root is None:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))

def get_tree_type(root):
    if root is None:
        return "empty"
    node_count = nodes_count(root)
    if is_perfect(root):
        return "perfect"
    elif is_full(root) and is_complete(root, 0, node_count):
        return "perfect" # Prioritize perfect
    elif is_complete(root, 0, node_count):
        return "complete"
    elif is_full(root):
        return "full"
    else:
        return "не є complete або full"

def pre_order_traversal(root):
    if root:
        print(root.value, end=" ")
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=" ")
        in_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value, end=" ")

block_values = [5, 3, 8, 1, 4, 7, 9, 2, 6, 10]

bst_root = None
for value in block_values:
    bst_root = insert(bst_root, value)

tree_type = get_tree_type(bst_root)
print(f"Тип побудованого бінарного дерева пошуку: {tree_type}")
print("Прямий обхід:")
pre_order_traversal(bst_root)
print()
print("Симетричний обхід:")
in_order_traversal(bst_root)
print()
print("Зворотний обхід:")
post_order_traversal(bst_root)
print()