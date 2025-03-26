import re

input_text = input("Введіть текст:")
print("--- Результат ---")

cleaned_text = re.sub(pattern=r'[^\w\s]', repl="", string=input_text, flags=re.UNICODE)
print(f"1. Видалення спеціальних символів:{cleaned_text}")

char = "у"
found_words = re.findall(pattern=rf'\b\w*{char}\w*\b', string=input_text)
print(f"2. Cлова, що містять '{char}':{found_words}")


length = 5
found_words_of_length = re.findall(pattern=rf'\b\w{{{length}}}\b', string=input_text)
print(f"3.Слова довжиною {length} символів: {found_words_of_length}")

found_words = re.findall(pattern=r'\b[ab]\w*s\b', string=input_text)
print(f"4. Пошук слова, що починається з 'a' або 'b' і закінчується на 's':{found_words}")

