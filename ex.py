# 비밀번호 만들기
# http://naver.com
# 규칙1 http부분 제외 => replace
# 규칙2 처음 점 제외
# 규칙3 비밀번호 :처음 세자리 + 글자개수 + 글자내 e개수 + !
str1 = 'http://naver.com'
str2=str1.replace("http://", "")
str2 = str2[:str2.index(".")] #처음부터 '.' index앞까지
numOfE = str2.count('e')
print(str2[:3]+str(len(str2))+str(numOfE)+'!')


