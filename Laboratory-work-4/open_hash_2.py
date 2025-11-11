# Константа розміру таблиці
M = 16
A = 0.618034  # Константа для методу множення (≈ (√5 - 1)/2)

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

def word_to_number(word: str) -> int:
    """Перетворює слово у число — суму позицій букв."""
    return sum(LETTER_POSITIONS.get(ch, 0) for ch in word.upper())

def multiplication_hash(key: str) -> int:
    """
    Хеш-функція за методом множення:
    h(k) = ⌊ M × (k × A mod 1) ⌋
    """
    k = word_to_number(key)
    fractional_part = (k * A) % 1
    return int(M * fractional_part)

def build_open_hash_table(words: list, m: int) -> list:
    """Будує хеш-таблицю з ланцюжками (списками)."""
    hash_table = [[] for _ in range(m)]
    for word in words:
        address = multiplication_hash(word)
        hash_table[address].append(word)
    return hash_table


def display_hash_table(table: list):
    """Виводить хеш-таблицю."""
    print("\n--- Результат хешування (метод множення, M=16) ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")

# Виконання
hash_table = build_open_hash_table(WORDS, M)
display_hash_table(hash_table)
