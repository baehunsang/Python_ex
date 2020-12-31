def std_weight(height, gender): 
    if(gender == '남자'):
        std_weight = pow((height / 100) , 2) * 22 # 공식에서 키 단위는 미터[m]
    else:
        std_weight = pow((height / 100) , 2) * 21
    print("키 %d cm %s의 표준 체중은 %.2f kg 입니다." % (height, gender, std_weight))
    return std_weight

height = 175
gender = '남자'
weight = std_weight(height, gender)
print("%.2f" % weight)