import json
from collections import Counter

data =   [{
    "order_id": 1,
    "user": "Ali",
    "items": ["phone", "case"],
    "total": 300000
  },{
    "order_id": 2,
    "user": "Dana",
    "items": ["laptop"],
    "total": 800000
  }, {
    "order_id": 3,
    "user": "Ali",
    "items": ["mouse", "keyboard"],
    "total": 70000
  }]


with open("orders.json", "w") as file:
    json.dump(data, file, indent=4)

with open("orders.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

total_sum = 0
buy_item_each_person = {}
bought_item = []
top_expensive_sum = 0
top_user_buy = ""


with open("orders.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    for order in data:
        total_sum += order["total"]

        user_id = order["user"]
        if user_id not in buy_item_each_person:
            buy_item_each_person[user_id] = 0
        buy_item_each_person[user_id] += 1

        bought_item.extend(order["items"])

        
        if order["total"] > top_expensive_sum:
            top_expensive_sum = order["total"]
            top_user_buy = user_id
        
most_popular_item = Counter(bought_item).most_common(1)[0][0]

summary = {
    "total_revenue": total_sum,
    "top_user": top_user_buy,
    "most_popular_item": most_popular_item,
    "total_orders": len(data)
}

with open('summary.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)

print("Файл summary.json успешно создан!")
