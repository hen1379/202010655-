#!/usr/bin/env python
# coding: utf-8

# In[3]:


#문자열의 좌우의 공백이 있을때 이를 제거해보세요.
#출제 의도 : strip의 뜻과 사용 방법을 아는가?

data=  " 삼성전자 "#공백 한 칸씩 생성

data1= data.strip() #data1은 data의 공백을 지운거라는 뜻

print(data1)
print(data)
#결과값 : #삼성전자
           #삼성전자 
    #data1은 공백이 없어서 data 보다 한칸 앞에 있다.


# In[ ]:




