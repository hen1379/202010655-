#!/usr/bin/env python
# coding: utf-8

# In[1]:


#date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.
#출제 의도 : zip을 이용하고 딕셔너리로 생성하는 방법을 아는가? 를 알기위한 문제
date=['09/05', '09/06','09/07','09/08','09/09'] #data 값 지정
close_price=[10500,10300,10100,10800,11000] #close_price 값 지정
close_table= dict(zip(data,close_price))  #0번은 0번끼리 1번은 1번끼리 나오게 zip을 이용해준다.
#그리고 그것을 dict함수로 바꿔주기 위해 dict안에 넣어주면 된다.
print(close_table)
#답:{'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}


# In[ ]:




