import re


stop_word = "кінець"

print(f"Введіть Python код для очищення (закінчіть введення словом 'кінець'):")
code_lines = []
while True:
    line = input()
    if line.strip() == stop_word:
        break
    code_lines.append(line)

input_code = '\n'.join(code_lines)
code_without_comments = re.sub(r'#.*', '', input_code)
cleaned_lines = [line for line in code_without_comments.splitlines() if line.strip()]
clean_code = '\n'.join(cleaned_lines)
print("--- Очищений код без коментарів та порожніх рядків ---")
print(clean_code)
