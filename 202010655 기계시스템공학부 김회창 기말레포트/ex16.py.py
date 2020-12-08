#!/usr/bin/env python
# coding: utf-8

# In[1]:


#파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    split = i.split(".")  #i 값을 .을 경계로 나누어라 
    if (split[1] =="h") or (split[1]=="c"):  #0부터시작하니까 1은 두번째 즉 'intra.h'로 예를 들자면 0은 intra 이고 1은 h이다.   이
        print(i)# 뒤에 있는 h나 c가 있는 파일을 출력해라.


# In[ ]:




