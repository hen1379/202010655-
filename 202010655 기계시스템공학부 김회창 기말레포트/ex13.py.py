#!/usr/bin/env python
# coding: utf-8

# In[2]:


#출제 의도 :  str를 float로 변경하고 if문을 사용할 수 있나? 를 알기 위한 문제
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

high = btc['max_price']   
low  =btc['min_price']
print(high, type(high))  # 20930000 <class 'str'> 우선 type을 알아보려고 실행했고 high 와 low 둘다 str이 나왔다 이제 이것을                         
print(low, type(low))    #20630000 <class 'str'> 더하기 빼기등을 하기위해 float로 변경을 한다.
#float로 변경한 후 변동폭 시가 최고가 를 구해준다.
변동폭 = float(btc['max_price']) - float(btc['min_price']) 
시가= float(btc['opening_price'])
최고가= float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")  # 시가 와 변동폭의 합이 최고가 보다 높으면 "상승장" 출력
else:
    print("하락장")  # 시가 와 변동폭의 합이 최고가 보다 낮으면 "하락장" 출력
    #답=상승장


# In[ ]:




