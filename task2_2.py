import json

item = input('item')
quantity = input('quantity')
price = input('price')
buyer = input('buyer')
date = input('date')


def write_order_to_json(item, quantity, price, buyer, date):
    print(item, quantity, price, buyer, date)

    dict_to_json = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }

    with open('orders.json', 'w') as f_n:
        json.dump(dict_to_json, f_n, sort_keys=True, indent=4)


if __name__ == '__main__':
    write_order_to_json(item, quantity, price, buyer, date)
