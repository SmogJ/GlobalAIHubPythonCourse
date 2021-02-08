#!/usr/bin/env python
# coding: utf-8

# # Homework Day 4

# ![image.png](attachment:image.png)

# In[11]:


# prime numbers  - number divisble by it self and one without a remender

n = int(input( "Enter an integer between 0 and 100 : " ))


def prime_n (n):
    for num in range (0, n):
        if num > 1:
            for i in range(2,num):
                if (num  % i) == 0:
                    #p = 0
                    num *=1 
                    return prime_n
                    
            
print (n)
prime_n(n)


# In[ ]:




