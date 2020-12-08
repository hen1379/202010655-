#!/usr/bin/env python
# coding: utf-8

# In[5]:


#1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.
#출제 의도 = 곱셈을 위해서 초기값을 1로 설정 할 수 있는가? for문을 사용할 수 있나?
result = 1  #곱셈을 위해서 초기값을 1로 설정

for i in range (1,11): #(1,2,3,4,5,6,7,8,9,10)
    result=result*i    #조금더 세련되게 만들려면 result*=i 로도 가능하다
print(result)
#답 3628800


# In[ ]:




