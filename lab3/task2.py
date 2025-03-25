import re

print("Введіть текст, з якого потрібно вилучити грошові суми в форматі '$ число' (наприклад, '$ 123.45'):")
input_text = input()
amounts = re.findall(pattern = r'\$\s(\d+\.?\d*)', string = input_text)
amounts_float = [float(amount) for amount in amounts]
total_amount = sum(amounts_float)
print("--- Результати ---")
print(f"Знайдені суми: {amounts_float}")
print(f"Загальна сума: ${total_amount:.2f}")
