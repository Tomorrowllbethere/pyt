import re
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    pattern_delete = r"[^\d]"   # створення патерну для відкидання зайвих елементів
    replacement_symbol = "" 
    number_just = re.sub(pattern_delete, replacement_symbol, phone_number) #видалення будь-яких знаків, окрім цифр
    number_just = number_just.split("0", maxsplit=1) #розділення рядків за 0
    number_just[0] = "+380" # заміна першого підрядка
    number_formated= "".join(number_just) #об'єднання рядків
    return number_formated
for num in raw_numbers:       #перевірка коду
    print("Нормалізовані номери телефонів для SMS-розсилки:", normalize_phone(num))