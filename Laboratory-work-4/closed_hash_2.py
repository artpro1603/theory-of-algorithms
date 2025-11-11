import math

# Константа розміру таблиці
M = 16
# Константа A для методу множення
A = (math.sqrt(5) - 1) / 2

# Список вхідних слів (українською)
WORDS = ["НЕ", "ТОЙ", "УРОЖАЙ", "ЩО", "В", "ПОЛІ", "А", "ТОЙ", "ЩО", "В", "КОМОРІ"]

# Словник позицій українських літер
LETTER_POSITIONS = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7, 'Є': 8, 'Ж': 9, 'З': 10,
    'И': 11, 'І': 12, 'Ї': 13, 'Й': 14, 'К': 15, 'Л': 16, 'М': 17, 'Н': 18, 'О': 19,
    'П': 20, 'Р': 21, 'С': 22, 'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28,
    'Ш': 29, 'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}


def word_to_number(word: str) -> int:
    """Перетворює слово в числовий ключ — суму позицій букв."""
    return sum(LETTER_POSITIONS.get(ch.upper(), 0) for ch in word)


def multiplication_hash(key: str) -> int:
    """Хеш-функція за методом множення."""
    k = word_to_number(key)
    return int(M * ((k * A) % 1))


def build_closed_hash_table(words: list, m: int) -> list:
    """Будує хеш-таблицю з відкритою адресацією (лінійне дослідження)."""
    hash_table = [None] * m

    for word in words:
        start_address = multiplication_hash(word)
        print(f"{word:>10} → h(k)={start_address:2d}", end="")

        # Лінійне дослідження
        for i in range(m):
            address = (start_address + i) % m
            if hash_table[address] is None:
                hash_table[address] = word
                print(f" → вставлено в {address}")
                break
            else:
                print(f" | колізія в {address}", end="")
        else:
            print(f"\nТаблиця заповнена! Не вдалося вставити: {word}")

    return hash_table


def display_hash_table(table: list):
    """Виводить хеш-таблицю у зручному форматі."""
    print("\n--- Хеш-таблиця (Метод множення, M=16) ---")
    print("Індекс | Слово")
    print("-------|-------")
    for i, item in enumerate(table):
        value = item if item is not None else "(NULL)"
        print(f"{i:02d} | {value}")


# Виконання
hash_table = build_closed_hash_table(WORDS, M)
display_hash_table(hash_table)
