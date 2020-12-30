# 소요시간은 5 ~ 50까지의 난수
from random import *
passenger = []
Isride = ' '
rideCount = 0
for i in range(0, 51):
    #passenger.append(int(5 + random()*46))
    passenger.append(randrange(5, 51))
for i in range(0, 51):
    if((passenger[i] >= 5) and (passenger[i] <= 15)):
        Isride = 'O'
        rideCount = rideCount + 1
    print("[{}] {}번째 손님 (소요시간 : {}분)".format(Isride, i, passenger[i]))
    Isride = ' '
print("총 탑승 승객 : {} 분".format(rideCount))
