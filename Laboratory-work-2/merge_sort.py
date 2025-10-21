def merge_sort_iterative(a):
    n = len(a)
    comparisons = 0
    assignments = 0
    i = 1
    iteration = 1  # лічильник ітерацій
    while i < n:
        j = 0
        print(f"\n--- Злиття підмасивів розміром {i} у підмасиви розміром {i * 2} ---")
        while j < n - i:
            left = j
            mid = j + i
            right = min(j + 2 * i, n)
            c, a_count = merge(a, left, mid, right)
            comparisons += c
            assignments += a_count
            print(f"Після злиття a[{left} - {right - 1}]: {a}")
            j += 2 * i
        i *= 2
        iteration += 1
    return a, comparisons, assignments


def merge(a, left, mid, right):
    comparisons = 0
    assignments = 0
    n1 = mid - left
    n2 = right - mid

    L = a[left:mid]
    R = a[mid:right]
    assignments += n1 + n2

    it1 = 0
    it2 = 0
    k = left
    assignments += 3

    while it1 < n1 and it2 < n2:
        comparisons += 1
        if L[it1] < R[it2]:
            a[k] = L[it1]
            it1 += 1
            assignments += 1
        else:
            a[k] = R[it2]
            it2 += 1
            assignments += 1
        k += 1
        assignments += 1

    while it1 < n1:
        a[k] = L[it1]
        it1 += 1
        k += 1
        assignments += 1

    while it2 < n2:
        a[k] = R[it2]
        it2 += 1
        k += 1
        assignments += 1

    return comparisons, assignments


# Приклад використання
my_list = [79, 97, 82, 18, 20, 2, 88, 61, 17]
print("Оригінальний список:", my_list)
sorted_list, comps, assigs = merge_sort_iterative(my_list.copy())
print("\nВідсортований список:", sorted_list)
print(f"Кількість порівнянь: {comps}")
print(f"Кількість присвоювань: {assigs}")
