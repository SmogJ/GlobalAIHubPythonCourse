#!/usr/bin/env python
# coding: utf-8

# # Homework Day 2

# ![image.png](attachment:image.png)

# ### Create a list and swap the second half of the list with the first half of the list and print the list on the screen

# In[37]:


lst = list(range(10))

lst2 =[]
lst3 = []
rvs = []
for i in lst:
    if i >= 5:
        lst2.append(i)
    if i < 5:
        lst3.append(i)

rvs = lst2 + lst3
print (rvs)


# # list comprehension

# In[58]:


rvs2 = [[i for i in lst if i >=5] + [i for i in lst if i < 5]]

print (rvs2)


# ### Ask the user to input a single digit integer to a variable 'n'. Then, print out all the even numbers from 0 to n (including n)  

# In[20]:


n = int(input('Please input any digit: '))

for i in range(n):
    if i%2 == 0:
        print (i)

