def format_price(price):
    return 'ціна: ' + format(price, '.2f') + ' грн'

def check_availability(*items):
    store_inventory = {
        'яблуко': True,
        'банан': True,
        'хліб': False,
        'молоко': True,
        'сир': False
    }
    availability = {}
    for item in items:
        availability[item] = store_inventory.get(item, False)
    return availability

def process_order():
    store_prices = {
        'яблуко': 10.5,
        'банан': 8.75,
        'хліб': 15.0,
        'молоко': 20.0,
        'сир': 50.0
    }
    while True:
        action = input('Введіть "купити" для покупки або "переглянути" для перегляду ціни: ').strip().lower()
        if action not in ['купити', 'переглянути']:
            print('Невірна опція, спробуйте ще раз.')
            continue
        order_input = input('Введіть товари через кому: ').strip().lower()
        order_items = [item.strip() for item in order_input.split(',') if item.strip()]
        availability = check_availability(*order_items)
        if not all(availability.values()):
            print('Деякі товари відсутні в магазині:')
            for item, available in availability.items():
                if not available:
                    print(' - ' + item)
            continue
        total_price = 0
        for item in order_items:
            total_price += store_prices.get(item, 0)
        if action == 'переглянути':
            print(format_price(total_price))
        elif action == 'купити':
            print('Замовлення прийнято. ' + format_price(total_price))
        break

def main():
    process_order()

if __name__ == '__main__':
    main()
