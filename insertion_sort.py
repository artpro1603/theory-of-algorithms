def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    # Цикл ітерується від другого елемента до кінця
    for i in range(1, n):
        # Зберігаємо поточний елемент для вставки
        key = arr[i]
        assignments += 1

        # j - індекс попереднього елемента
        j = i - 1
        assignments += 1

        # Пересуваємо елементи, що більші за key, вправо
        while j >= 0 and arr[j] > key:
            comparisons += 1  # Порівняння в умові while
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            assignments += 1

        # Додаткове порівняння, коли while зупинився (якщо j >= 0)
        if j >= 0:
            comparisons += 1

        # Вставляємо key на його правильне місце
        arr[j + 1] = key
        assignments += 1

        print(f"Ітерація {i}: {arr} | Вставлений елемент = {key}")

    return arr, comparisons, assignments


# Приклад використання
my_list = [79, 97, 82, 18, 20, 2, 88, 61, 17]
sorted_list, comps, assigs = insertion_sort(my_list.copy())

print("Оригінальний список:", my_list)
print("Відсортований список:", sorted_list)
print(f"Кількість порівнянь: {comps}")
print(f"Кількість присвоєнь: {assigs}")
