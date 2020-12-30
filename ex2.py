from random import * 

# 한명은 치킨, 3명은 커피, 20명 집단에서 추출
#lst = []
# for i in range(0, 20):
#     lst.append(i+1)
lst = list(range(1, 21)) # 1~20이 들어간 range 객체를 선언 후 타입캐스팅
shuffle(lst)
print("-- 당첨자 발표 --")
print("치킨 당첨자 :"+str(lst[0]))
print("커피 당첨자 :"+ str(sample(lst, 3)))
print("-- 축하합니다 --")