import re

print("Введіть дату у форматі 'yyyy-mm-dd':")
date_str = input()

match = re.match(pattern = r'(\d{4})-(\d{2})-(\d{2})', string=date_str)

year, month, day = match.groups()
converted_date = f'{day}-{month}-{year}'
print("Перетворена дата:", converted_date)
