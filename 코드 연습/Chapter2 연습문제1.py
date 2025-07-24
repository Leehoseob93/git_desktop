from collections import Counter, defaultdict
from dataclasses import dataclass

menu ={
    '아메리카노':4700,
    '카페라떼':5200,
    '레몬에이드':6000,
    '수박주스':6500,
    '초코쉐이크':7000
}

@dataclass
class Order:
    item: str
    price: int


orders = []
popular_menu = Counter(orders)
customer_orders = defaultdict(list)

def add_order(item, customer='익명'):
    if item in menu:
        order = Order(item=item, price=menu[item])
        orders.append(order)

        customer_orders[customer].append(order)
        
        popular_menu[item] += 1

        print(f"{item} 주문이 추가되었습니다.")
    else:
        print(f"{item}은/는 없는 메뉴입니다.")

add_order('카페라떼', '주문자1')
add_order('아메리카노', '주문자2')
add_order('레몬에이드', '주문자3')
add_order('수박주스', '주문자1')
add_order('초코쉐이크', '주문자1')
add_order('카페라떼', '주문자6')
add_order('아메리카노', '주문자7')
add_order('아메리카노', '주문자8')
add_order('아메리카노', '주문자9')

def show_order_summary():
    total = 0
    for order in orders:
        print(f'{order.item}:{order.price:,}원')
        total += order.price
    print(f'총액:{total:,}원')

show_order_summary()

def show_popular_menu():
    top3 = popular_menu.most_common(3)
    rank = 0
    for name, number in top3:
        rank += 1
        print(f'{rank}위 메뉴: {name} - {number}잔')

show_popular_menu()    

def show_customer_orders():
    print(f'[고객별 주문 내역]')
    for customer, order_lst in customer_orders.items():
        print(f'{customer}님께서 {[order.item for order in order_lst]}메뉴를 {[order.price for order in order_lst]} 가격에 주문하였습니다.')

show_customer_orders()