# Подключение библиотеки для считывания csv-файла
import csv

# Открытие файла
with open("../products.csv", encoding="utf-8-sig", newline="") as f:
    reader = list(csv.DictReader(f, delimiter=";", quotechar='"'))  # считывание данных из файла products.csv
    sorted_reader = sorted(reader, key=lambda x:x["Category"])  # сортировка данных по столбцу Category


category_name = input()  # Пользовательский ввод
while category_name != "молоко":
    min_count = 10000.0
    product = ""
    for line in sorted_reader:
        if line["Category"] == category_name and float(line["Count"]) < min_count:
            min_count = min(float(line["Count"]), min_count)
            product = line["product"]
    if product == "":
        print("Такой категории не существует в нашей БД")
    else:
        print(f"В категории: {category_name} товар: {product} был куплен {min_count} раз")
    category_name = input()