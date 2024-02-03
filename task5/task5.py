# Подключение библиотеки для считывания csv-файла
import csv

# Открытие файла
with open("../products.csv", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f, delimiter=";", quotechar='"')
    hash_table = dict()  # создание хэш-таблицы
    for line in reader:
        if (line["product"], line["Category"]) not in hash_table:
            hash_table[line["product"], line["Category"]] = float(line["Count"])
        else:
            hash_table[line["product"], line["Category"]] += float(line["Count"])

# Алгоритм для нахождения 10 наименее продаваемых продуктов
k = 0
for values in sorted(hash_table.items(), key=lambda x: x[1]):
    print(f"{values[0][1]}, {values[1]}")
    k += 1
    if k == 10:
        break
