#!/usr/bin/env python
# coding: utf-8

# # Final Project

# ![image.png](attachment:3d95c736-2732-4e03-aef1-7bf90fd4ec35.png)

# In[1]:


Company_Management_System = {
    'Manager1': {
        'name': 'Jackie Muller',
        'age': 34,
        'lang': 'French'
    }, 
    'Manager2': {
        'name': 'Messy gin',
        'age': 26,
        'lang': 'English',
    },
    'Manager3':{
        'name': 'Lou Si',
        'age': 34,
        'lang':'Chinese'
    },
    'Employee1':{
        'name': 'Jackie Muller',
        'age': 34,
        'lang': 'French'
    },
    'Employee2':{
        'name': 'Mayer Jon',
        'age': 25,
        'lang': 'English'   
    },
    'Employee3':{
        'name': 'Kate Shaw',
        'age': 29,
        'lang': 'English'
    } 
} 


# In[2]:


print(Company_Management_System)


# In[3]:


class Managers:
    def __init__(self, Name, langauge, age):
        self.Name = Name
        self.language = langauge
        self.age = age
        


# In[6]:


class Employees(Managers):
    pass
        
    def print_lang(self):
        for i in Company_Management_System[3:]:
            if i == 'lang':
                print(i)


# In[ ]:




