#!/usr/bin/env python
# coding: utf-8

# In[1]:


#아래 코드의 출력 결과를 예상하라

# 출제 의도 : 블록 구분을 할 줄 아는가? 를 알기위한 문제
if True:     #if True 부터 else:
                            #  print("4") 까지가 한블록 나머지 print("5") 가 두번쨰 블록이다.
    if False:   #거짓이여서 바로 지워짐
        print("1")
        print("2")
    else:         #거짓이 아니기에 사실이기에 3 출력됨
        print("3")
else :
    print("4")
print("5")  #블록 끝났고 이제 남은 print("5") 실행하여 5 출력됨

# 블록 구분만 하면 쉬운문제


# In[ ]:




