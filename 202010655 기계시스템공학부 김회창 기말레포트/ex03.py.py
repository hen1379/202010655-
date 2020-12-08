#!/usr/bin/env python
# coding: utf-8

# In[4]:


#아래 코드의 실행 결과를 예상해보세요.
#출제 의도 : 문자열은 변경 가능한가? 를 아는지 모르는지 알기위해
string='abcd'
string.replace('b','B') #string.replace('b','B') string에서 b를 b로 바꿔라 라는 뜻이다. 그러나 문자열은 변경 불가능 하다.
#문자열이 변경가능 하다고 생각을 했다면 aBcd라고 생각을 하겠지만 그럴 수 없기에 그대로 abcd로 출력된다.
print(string) 
#값 abcd

#원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해 준다.


# In[ ]:




