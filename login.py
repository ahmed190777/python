#!/usr/bin/env python
# coding: utf-8

# In[50]:





# In[108]:


x=["ahmed",1234,"mohamed",4567,"ali",8910]
name=input("please enter your name:")

password=int(input("please enter your bassword :"))
    


# In[109]:


y=1
for i in range(0,len(x),2) :
    if name==x[i]:
        if password==x[i+1]:
            y=0
            print("valid login")
  
if y==1:
	print ("invalid login")


# In[ ]:





# In[ ]:




