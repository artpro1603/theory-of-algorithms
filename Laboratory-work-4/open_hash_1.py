# Константа розміру таблиці
M = 13

# Список вхідних слів
WORDS = ["НЕ", "ТОЙ", "УРОЖАЙ", "ЩО", "В", "ПОЛІ", "А", "ТОЙ", "ЩО", "В", "КОМОРІ"]

# Словник позицій
LETTER_POSITIONS = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7, 'Є': 8,
    'Ж': 9, 'З': 10, 'И': 11, 'І': 12, 'Ї': 13, 'Й': 14, 'К': 15,
    'Л': 16, 'М': 17, 'Н': 18, 'О': 19, 'П': 20, 'Р': 21, 'С': 22,
    'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28, 'Ш': 29,
    'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}

def simple_hash_from_map(key: str) -> int:
    """
    Хеш-функція: h(k) = (сума позицій букв) mod 13.
    Використовує пряме відображення позицій з LETTER_POSITIONS.
    """
    sum_of_positions = 0
    for char in key:
        # Отримання позиції. Якщо символ не знайдено (наприклад, не літера), повертаємо 0.
        position = LETTER_POSITIONS.get(char, 0)
        sum_of_positions += position
    
    # Обчислення фінальної хеш-адреси
    hash_address = sum_of_positions % M
    return hash_address

def build_open_hash_table(words: list, m: int) -> list:
    """
    Будує хеш-таблицю з ланцюжками (списками).
    """
    # 1. Ініціалізація таблиці: M порожніх ланцюжків
    hash_table = [[] for _ in range(m)]

    # 2. Обробка кожного слова
    for word in words:
        address = simple_hash_from_map(word)
        # Додавання слова до відповідного ланцюжка
        hash_table[address].append(word)
    
    return hash_table

def display_hash_table(table: list):
    """Виводить хеш-таблицю у зручному форматі."""
    print("\n--- Результат хешування (Таблиця M=13) ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")

# Виконання
hash_table = build_open_hash_table(WORDS, M)
display_hash_table(hash_table)
