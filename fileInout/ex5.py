def printformat(FILE,week, depart, name):
    print("- {} 주차 주간보고 -".format(week), file= FILE)
    print("부서 : {}".format(depart), file=FILE)
    print("이름 : {}".format(name), file=FILE)
    print("업무 요약: ", file=FILE)
week = 1
name = "배훈상"
depart = "마케팅"

for week in range(1, 51):
    with open("fileInout/{}주차.txt".format(week), "w", encoding="utf-8") as FILE:
        printformat(FILE,week, depart, name)




