def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    # Зовнішній цикл ітерується по всьому списку
    for i in range(n - 1):
        # Припускаємо, що поточний елемент є мінімальним
        min_index = i
        assignments += 1  # Присвоєння змінній min_index

        # Внутрішній цикл шукає найменший елемент в решті списку
        for j in range(i + 1, n):
            comparisons += 1  # Операція порівняння
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1  # Присвоєння змінній min_index

        # Обмін елементів, якщо знайдено новий мінімальний
        comparisons += 1  # Операція порівняння
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3  # Три присвоєння при обміні

        print(f"Ітерація {i + 1}: {arr} | Мінімальний невідсортований елемент = {arr[i]})")

    return arr, comparisons, assignments


# Приклад використання
my_list = [79, 97, 82, 18, 20, 2, 88, 61, 17]
sorted_list, comps, assigs = selection_sort(my_list.copy())  # .copy() щоб не змінювати оригінал

print("Оригінальний список:", my_list)
print("Відсортований список:", sorted_list)
print(f"Кількість порівнянь: {comps}")
print(f"Кількість присвоєнь: {assigs}")

