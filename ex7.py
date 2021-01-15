class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

chicken = 10
waiting = 1
while(True):
    try:
        print("[남은 치킨 : {}]".format(chicken))
        order = int(input("치킨을 얼마나 주문하나요? "))
        if order < 1 :
            raise ValueError
        if chicken == 0:
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        if order > chicken:
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {}] {}마리 주문이 완료되었습니다".format(waiting, order))
            waiting += 1
        chicken -= order
    except ValueError:
        print("잘못된 값을 입력하였습니다")
    except SoldOutError as err:
        print(err)
        break