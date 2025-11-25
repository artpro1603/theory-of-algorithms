# tree_traversals_with_stack.py
# Створюємо вручну задане дерево та робимо три обходи.
# Додатково: inorder з виводом стану стеку викликів рекурсивної функції.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# ---- Побудова дерева (точно як у тебе) ----
#            79
#         /      \
#       42        88
#      /  \     /    \
#    40   61  87     98
#             /      /
#           82     97

root = Node(79)

root.left = Node(42)
root.right = Node(88)

root.left.left = Node(40)
root.left.right = Node(61)

root.right.left = Node(87)
root.right.right = Node(98)

root.right.left.left = Node(82)   # 82 — лівий син 87
root.right.right.left = Node(97)  # 97 — лівий син 98

# ---- обходи ----
def preorder(node, res):
    if node:
        res.append(node.key)
        preorder(node.left, res)
        preorder(node.right, res)
    return res

def inorder(node, res):
    if node:
        inorder(node.left, res)
        res.append(node.key)
        inorder(node.right, res)
    return res

def postorder(node, res):
    if node:
        postorder(node.left, res)
        postorder(node.right, res)
        res.append(node.key)
    return res

# ---- inorder з виводом стану стеку (симетричний, як для BST) ----
def inorder_with_stack(node):
    stack = []
    def helper(n):
        if n is None:
            return
        stack.append(n.key)
        print(f"   [Stack] вхід у inorder (перед лівим): {stack}")
        helper(n.left)
        print(f"   [Stack] перед друком ключа: {stack}")
        print(" -> Відвідано:", n.key)
        helper(n.right)
        stack.pop()
        print(f"   [Stack] вихід із inorder (після вузла): {stack if stack else '<порожній>'}")
    helper(node)

# ---- Виконання та вивід результатів ----
if __name__ == "__main__":
    print("Preorder (NLR): ", preorder(root, []))
    print("Inorder  (LNR): ", inorder(root, []))
    print("Postorder(LRN): ", postorder(root, []))

    print("\nInorder зі стеком рекурсії:")
    inorder_with_stack(root)
