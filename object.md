# 객체지향
## 선언
```ts
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

unit1 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
```
생성자 `__init__`을 통해서 클래스를 생성/ 초기화. `self`를 기본으로 받고 인자로 받은 멤버 변수 초기화. 만든 객체 에서 새로운 멤버 변수를 할당 가능 -> 확장한 객체에서만 적용
자기 자신의 멤버 변수를 이용해 함수를 만들고 싶을 경우 `self`를 인자로 받음.

## 상속

```ts
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상유닛] {} : {} 방향 이동[속도: {}]".format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
    
    def attack(self, location):
        print("{} : {} 방향으로 공격. [공격력 : {}]".format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{} : {}데미지 받음!".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력 {}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 처치당함!".format(self.name))
```
클래스명 뒤에 괄호를 통해 부모 클래스를 명시, `__init__`에는 부모의 `__init__`을 불러서 초기화

```ts
class Building(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0)
        self.location = location
```
`super`를 사용할수도 있지만 다중상속의 경우 처리가 힘들다.
### 다중 상속 
```ts
// 나는 기능을 위한 클래스
class Flyable:
    def __init__(self, speed):
        self.speed = speed
    
    def fly(self, name, location):
        print("{} : {} 방향으로 날아감".format(name, location))
//공격 유닛에 나는 기능 추가
class FlyableAttack(Flyable, AttackUnit):
    def __init__(self, name, hp, damage, speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, speed)
```
두 부모 클래스의 `__init__`을 사용해 초기화
### 오버라이딩
```ts
//공격 유닛에 나는 기능 추가
class FlyableAttack(AttackUnit):
    def __init__(self, name, hp, damage, speed):
        AttackUnit.__init__(self, name, hp, speed, damage)

    def move(self, location): // 부모클래스의 move  오버라이딩
        print("[공중 유닛]{} : {} 방향으로 날아감[속도: {}]".format(self.name, location, self.speed))
```
부모 클래스의 `move`를 오버라이딩 해서 나는 기능을 구현

### pass
아무것도 하지 않고 함수 종료 => 미완성인 함수에 사용

### ininstance(객체, 클래스명)
객체의 클래스 종류가 맞는지 판단(True, False)
