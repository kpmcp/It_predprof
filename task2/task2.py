# Подключение библиотеки для считывания csv-файла
import csv

# Открытие файла
with open("../products.csv", encoding="utf-8-sig", newline="") as f:
    reader = list(csv.DictReader(f, delimiter=";", quotechar='"'))  # считывание данных из файла products.csv
    # далее написан алгоритм для сортировки вставками
    for i in range(len(reader)):
        temp = reader[i]
        j = i-1
        while j >= 0 and (reader[j]["Category"]) > (temp["Category"]):
            reader[j+1] = reader[j]
            j -= 1
        reader[j+1] = temp

first_category = reader[0]["Category"]  # первая категория в отсортированных данных
max_price = 0.0
product = ""
# алгоритм нахождения самого дорого товара в первой категории
for line in reader:
    if first_category == line["Category"] and float(line["Price per unit"]) > max_price:
        max_price = max(max_price, float(line["Price per unit"]))
        product = line["product"]

print(f"В категории: {first_category} самый дорогой товар: {product} его цена за единицу товара составляет {max_price}")
