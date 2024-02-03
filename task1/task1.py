# Подключение библиотеки для считывания csv-файла
import csv

# Открытие файла
with open("../products.csv", encoding="utf-8-sig", newline="") as f:
    reader = list(csv.DictReader(f, delimiter=";", quotechar='"'))  # считывание данных из файла products.csv
    for line in reader:
        line["total"] = float(line["Price per unit"]) * float(line["Count"])  # добавление ключа total

# Сохранение нового файла со столбцом total
with open("products_new.csv", "w", encoding="utf-8-sig", newline="") as new_f:
    writer = csv.DictWriter(new_f, fieldnames=["Category", "product", "Date", "Price per unit", "Count", "total"],
                            delimiter=";")
    writer.writeheader()  # запись заголовков в файл
    writer.writerows(reader)  # запись новых данных в файл

# просчитвание итоговой суммы для категории Закуски
out = 0
for line in reader:
    if "Закуски" in line["Category"]:
        out += float(line["total"])
print(out)  # вывод итоговой суммы в консоль
