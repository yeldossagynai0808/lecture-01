# numbers = [1,2,3]
# spl = map(lambda x: x*x,numbers)
import json
from collections import Counter

# 1️⃣ Читаем JSON
with open("orders.json", "r", encoding="utf-8") as f:
    data = json.load(f)

total_revenue = 0
orders_per_user = {}
all_items = []
most_expensive_order = 0
top_user_by_order = ""

# 2️⃣ Анализ заказов
for order in data:
    total_revenue += order["total"]

    # считаем заказы пользователя
    user = order["user"]
    if user not in orders_per_user:
        orders_per_user[user] = 0
    orders_per_user[user] += 1

    # собираем все товары
    all_items.extend(order["items"])

    # ищем самый дорогой заказ
    if order["total"] > most_expensive_order:
        most_expensive_order = order["total"]
        top_user_by_order = user

# 3️⃣ Самый популярный товар
item_counts = Counter(all_items)
most_popular_item = item_counts.most_common(1)[0][0]

# 4️⃣ Создаём summary
summary = {
    "total_revenue": total_revenue,
    "top_user": top_user_by_order,
    "most_popular_item": most_popular_item,
    "total_orders": len(data)
}

with open("summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)

print("Файл summary.json успешно создан!")