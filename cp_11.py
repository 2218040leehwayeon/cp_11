class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        return total_price

# 음료 객체 생성
Coffee = Beverage("커피", 3000)
GreenTea = Beverage("녹차", 2500)
IceTea = Beverage("아이스티", 3000)

# 음료 메뉴 설정
menu = {"커피": Coffee, "녹차": GreenTea, "아이스티": IceTea}

# 각 음료에 대한 주문 수량 입력
coffee_quantity = int(input("커피 몇 잔을 주문하시겠습니까?: "))
green_tea_quantity = int(input("녹차 몇 잔을 주문하시겠습니까?: "))
ice_tea_quantity = int(input("아이스티 몇 잔을 주문하시겠습니까?: "))

# 첫 번째 사용자 입력 받기
order = input("주문할 음료를 선택하세요 (종료하려면 '종료' 입력): ")

# 입력값에 따라 객체 선택하여 calculate() 함수 호출
if order in menu:
    selected_beverage = menu[order]
    quantity = int(input("수량을 입력하세요: "))

    # 두 번째 사용자 입력을 calculate() 함수의 매개변수로 사용
    subtotal = selected_beverage.calculate(quantity)
    print(f"{selected_beverage.name} {quantity}잔 - 가격: {subtotal}원")

elif order == '종료':
    print("주문을 종료합니다.")

else:
    print("잘못된 음료입니다.")