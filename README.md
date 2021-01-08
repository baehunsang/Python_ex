# Python_ex
## 기본
---
* `control` + `/` =>문장 전체 주석처리
* `10//3` => 10을 3으로 나눈 몫
* ```abs``` =>절댓값

* ```from math import*```
* ```sqrt``` 루트, ```floor```내림, ```ceil```올림
* ```from random import*```의  ```random()``` =>0.0~10.0미만 의 난수

* ```int(random()*10)``` => 0~ 10 미만 (0 1 2 3 4 5 6 7 8 9)
* ```randrange(1, 46)``` => 1~45까지의 숫자
* ```str()```, ```int()``` 타입캐스팅
 ```str1 = 001006-0000000 print('생일'+ str1[0:6])```<br/> => 001006 => 오른쪽끝 index는 포함 안됨,
왼쪽끝 index포함<br/> 
* `[-7:]` 뒤에서 7번째(-7)부터 끝까지(맨끝 글자는 -1 index를 가짐)
* ```str.lower()``` 소문자로
* ```str.replace("str1", "str2")``` 문자열 치환
* `str.index('a')` `a`의 index반환 없으면 오류
* `str.find("substring")` 해당 substring의 index 반환 없으면 -1
* `str.count("a")` `a`개수 반환
* `print("%d %d %d" % (1, 2, 3))` 포멧 스트링
* `print("{0}색 {1}색".format(빨강, 파랑))` =>`빨강색 파랑색` => 중괄호
* ```print(f"{외부 변수} {외부 변수}")```
---
## 리스트
---
빈 자료구조는   `False`값을 가진다
* 선언 <br/>`list = [10, 20, 30]`
### 함수
---
* 맨 뒤에 삽입`list.append()`
* index위치에 삽입 `list.insert(1, 40)`
* 맨 뒤에서 삭제 `list.pop()`
* 원소의 수 `list.count()`
* 정렬 `list.sort()`
* 역순 저장 `list.reverse()`
* 합치기 `list.extend(list2)`
* 자료형 통일 불필요
---
## 딕셔너리
---
* 선언 
```ts
dic = {3:'유재석', 100: '김태호'} // 3, 100 => key
```
---
### 함수, 표현
* key 값으로 원소 참조<br/>`dic.get(3, "Not exist")`없으면 두번째 인자 출력

* `3 in dic` `in`표현 사용 key값이 있으면 `True`아니면 `False`

* `dic[4] = '조세호'` 새 key, 원소 덮어쓰기/ 추가

* `del dic["key"]` 해당 key값 삭제

|출력 포멧|dict_XXX([],[], ...)|
|--|--|
|dic.keys()|key만|
|dic.values()|값들만|
|dic.items()|쌍으로|
`items`는 key와 값을 쌍으로 튜플로 내보낸다

---
## 튜플
원소의 변경(삭제, 삽입) X
리스트보다 더 빠르다

---
* 선언 `menu = ('돈까스', '짜장면')`

* 일괄적으로 대입
```ts
(var1, var2, var3) = (1, 2, 3)
```

---

## 집합
순서X, 중복 X

---
* 선언 `set ={1, 2, 3, 3}` 
* 선언 과정에서 중복이 있으면 자동으로 지운다`{1, 2, 3}`

---
### 연산자, 함수
* `&`, `|`, `-` 합, 곱, 차집합

|함수||
|--|--|
|set.add("element")|삽입|
|set.delet("element")|삭제|

---

## 타입캐스팅(자료구조)
---
|함수||
|--|--|
|list()||
|tuple()||
|set()||

---
## 한줄 for

```ts
//Ex)문자열 길이 리스트 재생성
list = ['Iron man', 'Thor', 'Groot']
list2 = [len(i) for i in list]
```
---
## 2개 이상의 return

```ts
def foo():
    return a, b
    // 튜플 형식으로 2개 이상의 값 반환
```

---
## 가변인자
```ts
//Ex
def foo(*language):
    return
foo("C")
foo("C", "java")

// language 카테고리에 해당되는 값을 가변적으로 삽입 가능
```

---
## 표준입출력 포멧

|함수||
|--|--|
|ljust(num)|num 만큼의 빈칸을 확보후 왼쪽정렬|
|rjust(num)| 오른쪽 정렬|
|str.zfill(num)|num 칸만큼 공간을 두고 str이외 부분은 0으로 채운다|

|출력 포멧||
|--|--|
|"{}"|기본|
|"{0: >+10}"|빈칸은 " "로 채우고 오른쪽 정렬(>), 부호 삽입(+), 10칸의 공간 확보(10)|
|"{0:,}"|3칸마다 ',' 삽입|
|"{0: 2f}"|소수점 둘째자리까지 반올림해서 출력|

---

## 파일 입출력
`print`의 `file`인자, `open`함수

|||
|--|--|
|read()|전부 출력|
|readline()|탈출문자를 포함해서 한줄씩 읽고 커서는 줄바꿈|
|readlines()|모든 라인을 `리스트`로 저장|

### [pikle](https://docs.python.org/ko/3/library/pickle.html)

`import pickle`로 선언
`.pickle`파일은 `"wb"`, `"rb"`모드로 `open`한다.
신뢰할 수 있는 데이터만 피클링(open)해야 한다.
`dump(변수, 파일)` 변수에 저장된 걸 파일에 저장
`load(파일)` 파일에 저장된 값을 그대로 불러온다(자료구조, 타입 등이 유지된다.)


### with
일시적으로 파일을 열고닫고 할 때
```ts
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
```

`with as`문을 탈출하면서 파일이 자동으로 닫힌다. 








