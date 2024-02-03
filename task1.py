import csv

with open("products.csv", encoding="utf-8-sig", newline="") as f:
    reader = list(csv.DictReader(f, delimiter=";", quotechar='"'))
    for line in reader:
        line["total"] = float(line["Price per unit"]) * float(line["Count"])

with open("products_new.csv", "w", encoding="utf-8-sig", newline="") as new_f:
    writer = csv.DictWriter(new_f, fieldnames=["Category", "product", "Date", "Price per unit", "Count", "total"])
    writer.writeheader()
    writer.writerows(reader)

out = 0
for line in reader:
    if "Закуски" in line["Category"]:
        out += float(line["total"])
print(out)