#!/usr/bin/env python
# coding: utf-8

# In[11]:


#리스트에는 3일 간의 ohlc 데이터가 저장돼 있다. 시가에 매수해서 종가에 매도 했을 경우 총 수익금을 계산하라.  
# 출제 의도  : 4번에서 1번빼는 방법을 아는가? for문을 사용하여 뺀값들을 더할수가 있는가? 이다.
ohlc = [["open", "high", "low", "close"],
        [100,   110,     70,     100],
        [200,   210,    180,     190],
        [300,   310,    300,     310]]   #3일 간의 ohic 데이터

profit =0 #초기값 설정
for row in ohlc[1:]:
    profit += (row[3]-row[0])  #4번에서 1번 빼는거가 시가에서 매수해서 종가에 매도했을 경우니까 이렇게 설정
print(profit)   #for문 다돌아가고 profit 다 더해진 후 profit 값 산출
#값=0


# In[ ]:




