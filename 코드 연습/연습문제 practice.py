from collections import Counter, defaultdict
from dataclasses import dataclass

menu = {
    "아메리카노" : 1500,
    "카페라떼" : 2000,
    "바닐라라떼" : 2500,
    "카페모카" : 3000,
    "레몬에이드" : 4000,
    "오렌지에이드" : 4000,
    "딸기쥬스" : 4500,
    "토마토쥬스" : 4500
}

@dataclass
class Order:
    item: str
    price: int

orders = []
popular_menu = Counter(orders)
customer_orders_menu = defaultdict(list)

def add_order(item, customer):
    if item in menu:
        order = Order(item=item, price=menu[item]) # 이걸 어떻게 생각해내지...?
        orders.append(order)
        customer_orders_menu[customer].append(order)
        popular_menu[item] += 1
        print(f'{item}이/가 주문 목록에 추가되었습니다.')
    else:
        print('없는 메뉴입니다.')

add_order('아메리카노', '고객1')
add_order('카페라떼', '고객2')
add_order('바닐라라떼', '고객3')
add_order('카페모카', '고객1')
add_order('레몬에이드', '고객2')
add_order('오렌지에이드', '고객1')
add_order('딸기쥬스', '고객4')
add_order('토마토쥬스', '고객5')
add_order('아메리카노', '고객6')
add_order('아메리카노', '고객1')
add_order('아메리카노', '고객2')
add_order('카페라떼', '고객1')
add_order('카페라떼', '고객3')


def show_order_summary():
    total = 0
    for order in orders:
        print(order.item)
        total += order.price

    print(f'총액:{total:,}원')

show_order_summary()

def show_popular_menu():
    for top in popular_menu.most_common(1):
        name, number = top
        
    print(f'오늘의 인기메뉴는 {number}회 주문 받은 {name} 입니다.')

show_popular_menu()

def show_customer_orders():
    for customer, order_lst in customer_orders_menu.items():
        menu = [order.item for order in order_lst]
        print(f'{customer}님 주문 메뉴:{menu}')

show_customer_orders()