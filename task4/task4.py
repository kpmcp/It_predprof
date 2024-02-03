# Подключение библиотеки для считывания csv-файла
import csv


def generate_prom(name: str, date: str):
    """ Описание функции generate_prom:
            Функция для генерации промокода товара

            Описание аргументов:
            name - название продукта
            date - дата поступления товара
    """
    day, month, year = date.split(".")
    return f"{name[:2]}{day}{name[-2:][::-1]}{month[::-1]}".upper()


all_products = []
with open("../products.csv", encoding="utf-8-sig", newline="") as f:  # Открытие файла
    reader = csv.DictReader(f, delimiter=";", quotechar='"')  # считывание данных из файла products.csv
    for line in reader:
        line["promocode"] = generate_prom(line["product"], line["Date"])  # добавление и генерация колонки promocode
        all_products.append(line)

# Сохранение нового файла со столбцом promocode
with open("product_promo.csv", "w", encoding="utf-8-sig", newline="") as new_f:
    writer = csv.DictWriter(new_f, fieldnames=["Category", "product", "Date", "Price per unit", "Count", "promocode"], delimiter=";")
    writer.writeheader()  # запись заголовков в файл
    writer.writerows(all_products)  # запись новых данных в файл
