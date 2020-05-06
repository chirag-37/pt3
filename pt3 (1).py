#!/usr/bin/env python
# coding: utf-8

# # 1. What is the syntax to call a constructor of a base class from child class 
# 
# ans: class parentclassname:
#         def _init_(self,var):
#             self.var=var
#             print(self.var)    
#      class childclassname(parentclassname):
#              pass        
#      x=10
#      obj = childclassname(x) 
#      class A:
#     def __init__(self,x):
#         self.x=x
#         print(self.x)
# class B(A):
#     pass 
# x=10
# d1 = B(x)

# # 2. How is a class made as inherited class (syntax of child class)
# 
# ans: class childclassname(parentclassname):
#           pass
#      obj = childclassname()
#      obj.methodofparentclass()
# class A:
#     def find(self):
#         print('good')
# class B(A):
#     pass
# d1 = B()
# d1.find()

# # 3. Print an element of a nested dictionary 
# ANS : d1={1:'A',2:'B',3:('C','D'),4:['E','F','G','H'],5:{'A':1,'B':2,'C':3}}
# d1
# d1[4][0]
# 

# In[11]:


#1. Write a program that calculates and prints the value according to the formula given below. Take three values from user. Q= square root (( 2*value1*value2)/value3) 
import math
v1=int(input("enter any number : "))
v2=int(input("enter any number : "))
v3=int(input ("enter any number: "))
m=((2*v1*v2)/(v3))
print(math.sqrt(m))


# In[14]:


# write a program which accepts a string from console and print the characters that have even indexes. 
a= input('enter the string: ')
b=a[::2]
print(b)


# In[ ]:




