import json
from collections import Counter

data =   {
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
  }


with open("orders.json", "w") as file:
    json.dump(data, file, indent=4)

with open("orders.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Файл orders.json успешно создан!")
total_revenue = 0
user_orders_count = {}
all_items = []
max_order_value = 0
top_user_by_order = ""


for order in data:
    
    total_revenue += order["total"]
    
    
    user = order["user"]
    user_orders_count[user] = user_orders_count.get(user, 0) + 1
    
    
    all_items.extend(order["items"])
    
    
    if order["total"] > max_order_value:
        max_order_value = order["total"]
        top_user_by_order = user
item_counts = Counter(all_items)
most_popular_item = item_counts.most_common(1)[0][0]
summary = {
    "total_revenue": total_revenue,
    "top_user": top_user_by_order,
    "most_popular_item": most_popular_item,
    "total_orders": len(data)
}

with open('summary.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)

print("Файл summary.json успешно создан!")
