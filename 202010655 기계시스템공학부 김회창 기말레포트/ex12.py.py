#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면
#"정답 입니다를" 아닐 경우 "오답입니다" 출력하라

#출제 의도 if문과 딕셔너리 사용을 할 줄 아는가? 를 알기위한 문제
fruit={"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은?")  #사용자(user)가 좋아하는 과일은? 이라고 물을때
if user in fruit.values():  # 만약 fruit 딕셔너리 안에 values 값이 있다면
    print("정답입니다.") # "정답입니다" 출력해라
else:   #fruit 딕셔너리 안에 values 값이 없다면
    print("오답입니다.") # "오답입니다" 출력해라

