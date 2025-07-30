# ukrpy_translator.py

# Словник відповідностей українських ключових слів
ukr_to_py_keywords = {
    "друк": "print",
    "якщо": "if",
    "інакше": "else",
    "для": "for",
    "в": "in",
    "діапазон": "range",
    "повернути": "return",
    "означити": "def",
    "поки": "while",
    "істина": "True",
    "хиба": "False",
    "нічого": "None",
    "клас": "class",
    "спробувати": "try",
    "вийняток": "except",
    "встановити": "set",
    "отримати": "get",
}

# Функція для перекладу українського коду на Python
def translate_ukrpy_to_python(ukr_code: str) -> str:
    translated = ukr_code
    for ukr, py in ukr_to_py_keywords.items():
        translated = translated.replace(ukr, py)
    return translated

# Приклад українського коду
example_code_ukr = """
означити привітати(ім’я):
    друк("Привіт,", ім’я)

привітати("Світ")
"""

# Переклад і виконання
translated_code = translate_ukrpy_to_python(example_code_ukr)
print("== Перекладений код ==")
print(translated_code)
exec(translated_code)
