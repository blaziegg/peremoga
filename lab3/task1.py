import re

print("Введіть текст:")
input_text = input()
print("--- Результат ---")

cleaned_text = re.sub(pattern=r'[^\w\s]', repl="", string=input_text, flags=re.UNICODE)
print("1. Видалення спеціальних символів:")
print(f"  Оригінальний текст: {input_text}")
print(f"  Очищений текст: {cleaned_text}")

char = "у"
found_words = re.findall(pattern=rf'\b\w*{char}\w*\b', string=input_text)
print(f"2. Пошук слова, що містить '{char}':")
print(f"  Слова, що містять '{char}': {found_words}")

length = 5
found_words_of_length = re.findall(pattern=rf'\b\w{{{length}}}\b', string=input_text)
print(f"3. Пошук слова")
print(f"  Слова довжиною {length} символів: {found_words_of_length}")

found_words = re.findall(pattern=r'\b[ab]\w*s\b', string=input_text)
print("4. Пошук слова, що починається з 'a' або 'b' і закінчується на 's':")
print(f"  Слова, що відповідають умові: {found_words}")
