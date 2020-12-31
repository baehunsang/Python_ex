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