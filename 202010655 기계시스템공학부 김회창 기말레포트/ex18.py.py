#!/usr/bin/env python
# coding: utf-8

# In[3]:


#리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때
#  low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.
#출제 의도 : 리스트에 어떤값을 추가 하는 방법을 아는가? 변동폭을 리스트에 저장할 수 있는가? 를 알기위해서
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility=[]
for i in range(5):   #0,1,2,3,4
    diff=high_prices[i]-low_prices[i]
    #변동폭을 리스트에 저장해야하기에 for문 바깥쪽에 비어있는 리스트를 만들고 계산값을 리스트에 넣어주면 된다.
    volatility.append(diff) #  리스트에 어떤값을 추가할때는 리스트 이름적고 .찍고 append 하고 (추가하고싶은값) 하면 된다   
print(volatility)
    


# In[ ]:




