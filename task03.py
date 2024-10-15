class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_tree(node):
    # Якщо вузол порожній, повертаємо 0
    if node is None:
        return 0
    
    # Сума значення поточного вузла + сума лівого піддерева + сума правого піддерева
    return node.value + sum_tree(node.left) + sum_tree(node.right)

# Приклад використання:
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)

print(sum_tree(root))  # Виведе: 80
