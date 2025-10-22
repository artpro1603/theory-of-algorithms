# Лічильники
comparisons = 0
assignments = 0

def swap(arr, i, j):
    """Міняє місцями два елементи в масиві."""
    global assignments
    arr[i], arr[j] = arr[j], arr[i]
    assignments += 3  # три присвоювання при обміні

def sink(arr, i, n):
    """
    Процедура 'занурення' елемента вниз по купі.
    arr: масив
    i: індекс поточного елемента
    n: розмір купи
    """
    global comparisons, assignments
    k = i
    while True:
        j = 2 * k + 1  # індекс лівого дочірнього
        if j >= n:
            break

        # порівняння дітей
        comparisons += 1
        if j + 1 < n and arr[j + 1] > arr[j]:
            j += 1
            assignments += 1

        # перевірка, чи треба обмінювати
        comparisons += 1
        if arr[k] >= arr[j]:
            break

        # обмін
        swap(arr, k, j)
        k = j
        assignments += 1  # оновлення індексу k

def heapsort(arr):
    """Сортування купою"""
    global comparisons, assignments

    n = len(arr)
    print(f"Початковий масив: {arr}\n")

    # --- Фаза 1: Побудова купи ---
    print("--- Фаза 1: Побудова максимальної купи ---")
    for i in range(n // 2 - 1, -1, -1):
        print(f"Занурюємо елемент з індексом {i}: {arr[i]}")
        sink(arr, i, n)
    print(f"\nМасив після побудови купи: {arr}\n")

    # --- Фаза 2: Сортування ---
    print("--- Фаза 2: Сортування ---")
    for i in range(n - 1, 0, -1):
        print(f"Міняємо місцями корінь ({arr[0]}) та останній елемент ({arr[i]})")
        swap(arr, 0, i)
        n -= 1
        print(f"Розмір купи зменшився до {n}. Відновлюємо властивості купи.")
        sink(arr, 0, n)
        print(f"Масив на поточному кроці: {arr}\n")

    print(f"Відсортований масив: {arr}")
    print(f"Порівнянь: {comparisons}")
    print(f"Присвоювань: {assignments}")
    return arr


# --- Моделювання ---
A = [79, 97, 82, 18, 20, 2, 88, 61, 17]
sorted_A = heapsort(A.copy())
