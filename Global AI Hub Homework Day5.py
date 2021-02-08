#!/usr/bin/env python
# coding: utf-8

# #  Homework Day 5

# ![image.png](attachment:deda7eba-67b3-4009-b74c-52634d84cfed.png)!

# In[88]:


class animals:
    def __init__(self, coat_color, weight, height, age):  #self.name = name
        self.coat_color = coat_color
        self.weight = weight
        self.height = height
        self.age = age
             
    def add_coat_color(self):
        self.coat_color(self.coat_color)
        
    def add_weight(self):
        self.weight(self.weight)
        
    def add_height(self):
        self.height(self.height)
        
    def add_age(self):
        self.age(self.age)
        
    def animalinfo(self):      # print("pet name is {} ".format(self.name))
        print("it's other info is : ")
        for i in (self.coat_color, self.weight, self.height, self.age):
              print(i)
        


# In[89]:


#Animal = animals('Gray')
Animal.add_coat_color('black')
Animal.add_weight(50)
Animal.add_height(30)
Animal.add_age(5)


# In[90]:



Animal.animalinfo()


# In[91]:


class dogs(animals):
    def __init__(self, breed_type, owner, bmi):
        self.breed_type = breed_type
        self.owner = owner
        self.bmi = bmi
        
    def print_breed(self):
        print (self.breed_type)
        
    def pet_owner(self):
        print (self.ower)
        
    def print_bmi(self):
        self.weight + self.height + self.age
        return (self.bmi)
    
dog = dogs('Pitbull', 'Jeremy', '')


dog = animals('black', 45, 37, 7)


# In[92]:


dog.print_breed()
dog.pet_owner()
dog.print_bmi()

dog.animalinfo()


# In[ ]:


class cats(animals):
    def __init__(self, owner, bmi):
        self.breed_type = breed_type
        self.owner = owner
        self.bmi = bmi
    
        
    def print_breed(self):
        print (self.breed_type)
        
    def pet_owner(self):
        print (self.ower)
        
    def print_bmi(self):
        self.bmi = self.weight + self.height + self.age
        print(self.bmi)
        
cat = cat('Bob cat', 'Ella', '')


# In[ ]:


cats.print_breed()

