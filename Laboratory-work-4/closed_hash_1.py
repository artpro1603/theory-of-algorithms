# Константа розміру таблиці
M = 13

# Список вхідних слів (українською)
WORDS = ["НЕ", "ТОЙ", "УРОЖАЙ", "ЩО", "В", "ПОЛІ", "А", "ТОЙ", "ЩО", "В", "КОМОРІ"]

# Словник позицій українських літер
LETTER_POSITIONS = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7, 'Є': 8, 'Ж': 9, 'З': 10,
    'И': 11, 'І': 12, 'Ї': 13, 'Й': 14, 'К': 15, 'Л': 16, 'М': 17, 'Н': 18, 'О': 19,
    'П': 20, 'Р': 21, 'С': 22, 'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28,
    'Ш': 29, 'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}


def primary_hash(key: str) -> int:
    """h(k) = (сума позицій букв) mod M. Первинна хеш-функція."""
    sum_of_positions = 0
    for char in key.upper():
        position = LETTER_POSITIONS.get(char, 0)
        sum_of_positions += position
    return sum_of_positions % M


def build_closed_hash_table(words: list, m: int) -> list:
    """
    Будує хеш-таблицю з відкритою адресацією, використовуючи лінійне дослідження.
    """
    # 1. Ініціалізація таблиці: M порожніх слотів
    hash_table = [None] * m
    inserted_count = 0

    # 2. Обробка кожного слова
    for word in words:
        # Крок 2a: Обчислення початкової адреси
        start_address = primary_hash(word)
        address = start_address
        print(f"{word:>10} → початкова адреса {start_address}", end="")

        # Крок 2b: Лінійне дослідження (Linear Probing)
        for i in range(m):
            # h(k, i) = (h(k) + i) mod M
            address = (start_address + i) % m

            # Якщо комірка вільна — вставляємо
            if hash_table[address] is None:
                hash_table[address] = word
                inserted_count += 1
                print(f" → вставлено в {address}")
                break
            else:
                print(f" | колізія в {address}", end="")

        else:
            # Таблиця заповнена
            print(f"\nПомилка: Таблиця заповнена. Не вдалося додати слово: {word}")
            return hash_table

    return hash_table


def display_hash_table(table: list):
    """Виводить хеш-таблицю у зручному форматі."""
    print("\n--- Хеш-таблиця (Відкрита адресація, M=13) ---")
    print("Індекс | Слово")
    print("-------|-------")
    for i, item in enumerate(table):
        value = item if item is not None else "(NULL)"
        print(f"{i:02d} | {value}")


# Виконання:
hash_table = build_closed_hash_table(WORDS, M)
display_hash_table(hash_table)
