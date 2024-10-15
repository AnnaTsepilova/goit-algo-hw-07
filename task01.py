class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_max_value(node):
    if node is None:
        return None  # Якщо дерево порожнє

    current = node
    # Рухаємося праворуч до кінця дерева
    while current.right is not None:
        current = current.right
    return current.key

# Приклад використання:
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.right.right = Node(40)

print("Найбільше значення в дереві:", find_max_value(root))
