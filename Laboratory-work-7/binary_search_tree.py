# ------------------- Вузол дерева -------------------
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# ------------------- Побудова дерева -------------------
def build_bst(arr):
    root = None
    print("Початок побудови BST:")
    for x in arr:
        print(f"Вставляємо {x}")
        root = insert(root, x)
    print("Побудова завершена.\n")
    return root


def insert(x, z):
    if x is None:
        print(f"  Створюємо новий вузол {z}")
        return Node(z)
    elif z < x.key:
        print(f"  {z} < {x.key}: йдемо в ліве піддерево")
        x.left = insert(x.left, z)
    elif z > x.key:
        print(f"  {z} > {x.key}: йдемо в праве піддерево")
        x.right = insert(x.right, z)
    else:
        print(f"  {z} вже існує дублікат!")
    return x


# ----------------------- Обходи -----------------------
def inorder(x):
    if x:
        inorder(x.left)
        print(x.key, end=" ")
        inorder(x.right)


def preorder(x):
    if x:
        print(x.key, end=" ")
        preorder(x.left)
        preorder(x.right)


def postorder(x):
    if x:
        postorder(x.left)
        postorder(x.right)
        print(x.key, end=" ")


# --- Симетричний обхід зі стеком рекурсії ---
def inorder_with_stack(x, stack):
    if x:
        stack.append(x.key)
        print_stack(stack, "вхід у inorder (перед лівим):")
        inorder_with_stack(x.left, stack)

        print_stack(stack, "перед друком ключа:")
        print(f" -> Відвідано: {x.key}")

        inorder_with_stack(x.right, stack)

        stack.pop()
        print_stack(stack, "вихід із inorder (після вузла):")


def print_stack(stack, caption):
    print(f"   [Stack] {caption} {stack if stack else '<порожній>'}")


# ----------------------- Видалення -----------------------
def delete(root, z):
    if root is None:
        print(f"delete({z}): досягнуто None — нічого не робимо")
        return None

    print(f"delete({z}): поточний вузол = {root.key}")

    if z < root.key:
        print(f"  {z} < {root.key} => йдемо в ліве піддерево")
        root.left = delete(root.left, z)

    elif z > root.key:
        print(f"  {z} > {root.key} => йдемо в праве піддерево")
        root.right = delete(root.right, z)

    else:
        print(f"  Знайдено вузол {z} для видалення")

        # 2 дитини
        if root.left and root.right:
            successor = minimum(root.right)
            print(f"    Дві дитини. Заміна ключа на мінімум правого піддерева: {successor.key}")
            root.key = successor.key
            root.right = delete(root.right, successor.key)

        # 1 або 0 дітей
        else:
            if root.left:
                print(f"    Лише ліва дитина. Замінюємо на {root.left.key}")
                root = root.left
            elif root.right:
                print(f"    Лише права дитина. Замінюємо на {root.right.key}")
                root = root.right
            else:
                print("    Лист. Видаляємо (None)")
                root = None

    return root


def minimum(x):
    while x.left:
        x = x.left
    return x


# ----------------------- Друк обходів -----------------------
def print_all_traversals(root):
    print("Inorder(симетричний):  ", end="")
    inorder(root)
    print()

    print("Preorder(прямий): ", end="")
    preorder(root)
    print()

    print("Postorder(зворотній):", end=" ")
    postorder(root)
    print()


# ----------------------- Приклад виконання -----------------------
def run_example():
    arr = [98, 40, 42, 88, 61, 87, 79, 97, 82]
    print("=== Побудова BST ===")
    root = build_bst(arr)

    print("Результуючі обходи:")
    print_all_traversals(root)
    print()

    print("=== Inorder зі стеком рекурсії ===")
    inorder_with_stack(root, [])
    print()

    print("=== Послідовні видалення: правий корінь → лівий корінь → основний корінь ===")

    # 1) корінь правого піддерева
    if root and root.right:
        key_right = root.right.key
        print(f"\n1) Видаляємо корінь правого піддерева: {key_right}")
        root = delete(root, key_right)
        print_all_traversals(root)

    # 2) корінь лівого піддерева
    if root and root.left:
        key_left = root.left.key
        print(f"\n2) Видаляємо корінь лівого піддерева: {key_left}")
        root = delete(root, key_left)
        print_all_traversals(root)

    # 3) основний корінь
    if root:
        key_root = root.key
        print(f"\n3) Видаляємо основний корінь: {key_root}")
        root = delete(root, key_root)
        print_all_traversals(root)

    print("\n=== Кінець прикладу ===")


# ---------------------- Запуск прикладу ----------------------
if __name__ == "__main__":
    run_example()
