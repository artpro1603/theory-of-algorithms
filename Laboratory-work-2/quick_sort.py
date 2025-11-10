def quicksort(a, l, r):
    comparisons = 0
    assignments = 0
    recursive_calls = 1  # Поточний виклик є першим

    comparisons += 1
    if l < r:
        # Процес поділу
        # q - це індекс, де буде розміщено опорний елемент (pivot)
        q, c1, a1 = partition(a, l, r)
        comparisons += c1
        assignments += a1
        
        print(f"Після поділу (Pivot ставимо на {q}): {a}")
        print("--------------------------------------------------------------------------")

        # Рекурсивні виклики
        # Ліва частина (до опорного елемента, q-1)
        c2, a2, r2 = quicksort(a, l, q - 1)
        # Права частина (після опорного елемента, q+1)
        c3, a3, r3 = quicksort(a, q + 1, r)
        
        comparisons += c2 + c3
        assignments += a2 + a3
        recursive_calls += r2 + r3
    else: # нічого не робим
        return 0, 0, 0

    return comparisons, assignments, recursive_calls


def partition(a, l, r):
    comparisons = 0
    assignments = 0

    # Обираємо опорний елемент (Pivot) - використовуємо останній елемент
    pivot = a[r]
    assignments += 1
    print(f"Поділ: обираємо новий pivot = {pivot}, сортуємо діапазон {l}-{r}: {a[l:r+1]}")

    # Індекс меншого елемента. 'i' відстежує кінець підмасиву менших елементів.
    i = l - 1
    assignments += 1

    # Перебираємо елементи від l до r-1
    for j in range(l, r):
        # Порівняння: чи поточний елемент менший або дорівнює pivot
        comparisons += 1
        if a[j] <= pivot:
            # Збільшуємо індекс меншого елемента
            i += 1
            assignments += 1
            
            # Обмінюємо a[i] та a[j]
            # Це переміщує елемент менший за pivot у ліву частину
            print(f"   Обмін: {a[i]} <-> {a[j]}")
            a[i], a[j] = a[j], a[i]
            assignments += 3  # Обмін - це 3 присвоювання

    # Встановлюємо опорний елемент на його правильне місце (i+1)
    # Обмінюємо a[i+1] (перший елемент, більший за pivot) з pivot (a[r])
    print(f" -> Фінальний обмін: {a[i + 1]} <-> {a[r]} (Pivot)")
    a[i + 1], a[r] = a[r], a[i + 1]
    assignments += 3
    
    # Повертаємо індекс опорного елемента
    return i + 1, comparisons, assignments


my_list = [79, 97, 82, 18, 20, 2, 88, 61, 17]
original_list = my_list.copy()

print("Початковий список:", original_list)
print("--------------------------")

total_comparisons, total_assignments, total_recursive_calls = quicksort(my_list, 0, len(my_list) - 1)

print("--- Фінальний результат ---")
print("Відсортований список:", my_list)
print(f"Порівнянь: {total_comparisons}")
print(f"Присвоювань: {total_assignments}")
print(f"Рекурсивних викликів: {total_recursive_calls}")
