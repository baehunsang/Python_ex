from random import *
# https://www.youtube.com/watch?v=kWiCuklohdY&t=11867s
# 객체지향 연습용 코드
# 기본 뼈대 
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{} 유닛 생성됨".format(self.name))

    def move(self, location):
        if self.speed != 0:
            print("[지상유닛] {} : {} 방향 이동[속도: {}]".format(self.name, location, self.speed))
        else:
            print("{}: [경고] 이동 불가".format(self.name))

    def damaged(self, damage):
        print("{} : {}데미지 받음!".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력 {}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 처치당함!".format(self.name))

# 공격 기능 추가
class AttackUnit(Unit):
    def __init__(self, name, hp,speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{} : {} 방향으로 공격. [공격력 : {}]".format(self.name, location, self.damage))
    

#공격 유닛이면서 날아다니는 유닛일 경우
class FlyableAttack(AttackUnit):
    def __init__(self, name, hp, damage, speed):
        AttackUnit.__init__(self, name, hp, speed, damage)

    def move(self, location): # 부모클래스의 move  오버라이딩
        if self.speed != 0:
            print("[공중 유닛] {} : {} 방향으로 날아감[속도: {}]".format(self.name, location, self.speed))
        else:
            print("{}: [경고] 이동 불가".format(self.name))

#마린 
#마린은 체력 10을 대가로 `steampack`을 사용할수 있다.
class Marin(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    
    def steampack(self):
        if(self.hp > 10):
            print("{}: 스팀팩 사용함".format(self.name))
        else:
            print("{}: [경고] 체력 부족".format(self.name))


#탱크
#시즈모드 시에는 이동속도 0, 공격력 상슴

class Tank(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.IsSeize = False
    def setSeize(self):
        if self.IsSeize == True:
            self.IsSeize = False
            self.speed = 1
            self.damage = 35
            print("{}: 시즈모드 해제".format(self.name))
        else:
            self.IsSeize = True
            self.speed = 0
            self.damage *= 2
            print("{}: 시즈모드".format(self.name))

#레이스
#클로킹모드 기능이 있음, 날아다님

class Wraith(FlyableAttack):
    def __init__(self):
        FlyableAttack.__init__(self, "레이스", 80, 20, 5)
        self.IsClocked = False
    def clocking(self):
        if self.IsClocked == False:
            print("{}: 클로킹 모드".format(self.name))
            self.IsClocked = True
        else:
            print("{}: 클로킹모드 해제".format(self.name))
            self.IsClocked = False


# 동작
# 마린 세마리를 만든다.
# 탱크 둘을 만든다.
# 레이스 하나를 만든다.
# 유닛 모두를 '1시'방향으로 이동한다.

# 레이스는 클로킹모드, 탱크는 시즈모드, 마린은 스팀팩을 먹는다
# 모든 유닛 공격'1시'방향

# 모든 유닛은 5 ~ 150 사이의 데미지를 받는다
# 다 죽으면 게임오버 출력

units = []

for i in range(0, 3):
    units.append(Marin())
for i in range(0, 2):
    units.append(Tank())
units.append(Wraith())

for unit in units:
    unit.move("1시")

for unit in units:
    if isinstance(unit, Marin):
        unit.steampack()
    if isinstance(unit, Tank):
        unit.setSeize()
    if isinstance(unit, Wraith):
        unit.clocking()

for unit in units:
    unit.attack("1시")
    unit.damaged(randint(5, 151))

if not units:
    print("Game Over")
 



