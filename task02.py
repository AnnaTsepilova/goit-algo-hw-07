class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_min_value(node):
    # Якщо дерево порожнє
    if node is None:
        return None
    
    # Рухаємося ліворуч до самого кінця
    current = node
    while current.left is not None:
        current = current.left
    
    # Повертаємо значення останнього лівого вузла
    return current.value

# Приклад використання:
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)

print(find_min_value(root))  # Виведе: 5
