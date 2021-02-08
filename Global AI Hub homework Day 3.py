#!/usr/bin/env python
# coding: utf-8

# # Homework Day3

# ![image.png](attachment:image.png)

# #### User Login app:
#     get username and password values from the user.
#     check the values in an if statement and tell the user if they were successful
# 

# In[16]:


print ('%%%%%%%%%%%%%%%%%%%%%% LOG IN %%%%%%%%%%%%%%%%%%%%%%%')

username = 'Mayers' 
password = 'Wholeeffort'

user = input('Enter a username: ')
pass1 = input('Enter a password: ')

if user == username and pass1 == password:
    print ('Welcome to Home  Page')

elif user != username or pass1 != password:
    print ('Username or Password is invalid')
else:
    if user == None or pass1 == None:
        print ('Enter your user details')


# #### Extra:
#     User login using dictionary 

# In[8]:


print('$$$$$$$$$$$$$$$$$$$$$$$ Log in $$$$$$$$$$$$$$$$$$$$$$')

login = {'username':'Mayers', 'password' : 'Wholeeffort'}

log_in = {'username':input ('Username: ' ), 'password':input ('Password: ' )} 

# print (log_in)

if log_in == login:
    print ('welcome to the Homepage')
    
elif log_in['username'] != login['username']:
    print('Invalid Username')
    
elif log_in['password'] != login['password']:
    print('Invalid Password')
    
else: 
    print ('Enter Ussername and Password')


# In[ ]:




