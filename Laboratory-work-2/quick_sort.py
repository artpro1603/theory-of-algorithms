def quicksort(a, l, r):
    comparisons = 0
    assignments = 0
    recursive_calls = 1

    if l < r:
        q, c1, a1 = partition(a, l, r)
        comparisons += c1
        assignments += a1

        print(f"Після поділу: {a}")
        print("--------------------------------------------------------------------------")

        c2, a2, r2 = quicksort(a, l, q)
        c3, a3, r3 = quicksort(a, q + 1, r)
        comparisons += c2 + c3
        assignments += a2 + a3
        recursive_calls += r2 + r3
    else:
        return 0, 0, 0

    return comparisons, assignments, recursive_calls


def partition(a, l, r):
    comparisons = 0
    assignments = 0

    pivot = a[l]
    assignments += 1
    print(f"Поділ: новий pivot = {pivot}, діапазон {l}-{r}: {a[l:r+1]}")

    i = l - 1
    j = r + 1
    assignments += 2

    while True:
        i += 1
        assignments += 1
        while a[i] < pivot:
            comparisons += 1
            i += 1
            assignments += 1
        comparisons += 1

        j -= 1
        assignments += 1
        while a[j] > pivot:
            comparisons += 1
            j -= 1
            assignments += 1
        comparisons += 1

        comparisons += 1
        if i >= j:
            print(f" -> Індекси перетнулися на позиції {j}")
            return j, comparisons, assignments

        print(f"   Обмін: {a[i]} <-> {a[j]}")
        a[i], a[j] = a[j], a[i]
        assignments += 3


# Приклад використання
my_list = [79, 97, 82, 18, 20, 2, 88, 61, 17]
original_list = my_list.copy()

print("Початковий список:", original_list)
print("--------------------------")

total_comparisons, total_assignments, total_recursive_calls = quicksort(my_list, 0, len(my_list) - 1)

print("Відсортований список:", my_list)
print(f"Порівнянь: {total_comparisons}")
print(f"Присвоювань: {total_assignments}")
print(f"Рекурсивних викликів: {total_recursive_calls}")
