class Product:

    serial_number = 0 # 일련 번호

    def __init__(self, name, quantity, price): # 상품명, 수량, 가격
        self.name = name
        self.quantity = quantity
        self.price = price
        Product.serial_number += 1
        self.serial_number = Product.serial_number

class Plain:

    def __init__(self, previous_payment): # 전월 이용 실적
        self.previous_payment = previous_payment
        self.reserve = 0 # 적립금

    def buy(self, name, quantity):
        if isinstance(name, Product):
            print(f'{name.price * quantity}원 입니다')
            name.quantity -= quantity # 산 만큼 수량 감소
            self.reserve += int((name.price * quantity) * 0.005) # 0.5적립
        else:
            print('바코드를 읽을 수 없습니다.')

class Friends(Plain):

    coupon_price = 6000

    def __init__(self, previous_payment, coupon=3):
        super().__init__(previous_payment)
        self.coupon = coupon # 쿠폰 수량

    def buy(self, name, quantity):
        if isinstance(name, Product):
            if (name.price * quantity < self.coupon_price) or (self.coupon < 1):
                print(f'{name.price * quantity}원 입니다')
                self.reserve += int((name.price * quantity) * 0.01)
            else:
                coupon_use = input("쿠폰을 사용하시겠습니까? YES/NO")
                if coupon_use.upper() == "YES":
                    print(f'쿠폰이 적용되었습니다! ')
                    total_price = name.price * quantity - self.coupon_price
                    self.coupon -= 1
                    print(f'{total_price}원 입니다')
                    self.reserve += (name.price * quantity) * 0.01
                else :
                    total_price = name.price * quantity
                    print(f'{total_price}원 입니다')
                    self.reserve += (name.price * quantity) * 0.01

            name.quantity -= quantity

        else:
            print('바코드를 읽을 수 없습니다.')

class Purple(Friends):

    coupon_price = 10000

    def __init__(self, previous_payment, coupon=4, reserve_sum= 0):
        super().__init__(previous_payment, coupon)
        self.reserve_sum = reserve_sum

    def buy(self, name, quantity):
        if isinstance(name, Product):
            if (name.price * quantity < self.coupon_price) or (self.coupon < 1):
                total_price = name.price * quantity

            else:
                coupon_use = input("쿠폰을 사용하시겠습니까? YES/NO : ")
                if coupon_use.upper() == "YES":

                    total_price = name.price * quantity - self.coupon_price
                    self.coupon -= 1
                else :
                    total_price = name.price * quantity

            print(f'{total_price}원 입니다')
            self.reserve += int(total_price * 0.07)
            name.quantity -= quantity

            # 후기 입력 여부를 묻는 while 루프
            while True:
                review = input("후기를 입력하시겠습니까? (YES/NO): ")
                if review.upper() == 'YES':
                    self.reserve *= 2  # 적립금을 두 배로 증가
                    print(f'후기 감사합니다! 적립금이 두 배가 되어 {self.reserve:.2f}원이 되었습니다.')
                    self.reserve_sum += int(self.reserve)
                    print("총 적립금은 " +str(int(self.reserve_sum)) + "입니다.")
                    break
                elif review.upper() == 'NO':
                    print('후기를 입력하지 않으셨습니다. 기본 적립금이 유지됩니다.')
                    print("총 적립금은 " + str(int(self.reserve_sum)) + "입니다.")
                    break
                else:
                    print("잘못된 입력입니다. YES 또는 NO로만 답해주세요.")
        else:
            print('바코드를 읽을 수 없습니다.')

새우깡 = Product('새우깡', 40, 2000)

# member = input("이름, 전월 실적, 보유 쿠폰 수량을 입력해주세요 : ").split()
# member[1] = int(member[1])
# member[2] = int(member[2])

# if member[1] >= 100:
#     new_person = 'member[0]'
#     new_person = Purple(member[1], member[2])
# elif member[1] >= 15:
#     new_person = 'member[0]'
#     new_person = Friends(member[1], member[2])
# else:
#     new_person = 'member[0]'
#     new_person = Plain(member[1])
# print(new_person)

kim = Purple(120, 3)
lee = Friends(70, 3)

kim.buy(새우깡, 30)
kim.reserve
