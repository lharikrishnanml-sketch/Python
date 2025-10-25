#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1. Square of Numbers from 1 to 5
#Output:
#1 4 9 16 25

for num in range(1,6):
    print (num*num, end=' ')



# In[4]:


#2.Swap Two Variables Without Using a Temporary Variable
#Question: Write a Python program to swap two variables a = 5 and b = 10 without using a temporary variable.

a=5
b=10
b=5
a=10
print(a,b)


# In[7]:


#3.Find Even and Odd Numbers in a List
#Question: Write a Python program to separate even and odd numbers from the list [12, 17, 19, 24, 35, 40, 56].

my_list=[12, 17, 19, 24, 35, 40, 56]
even_list=[]
odd_list=[]
for num in my_list:
   if num%2==0:
       even_list.append(num)
print("Even numbers are" ,even_list)
for num in my_list:
   if num%2!=0:
       odd_list.append(num)
print("odd numbers are", odd_list)


# In[9]:


#4. Reverse a Number
#Question: Write a Python program to reverse the number 12345.
my_list1=[1,2,3,4,5]
reverse_num=my_list1[::-1]
print(reverse_num)


# In[15]:


#5. Find the Second Largest Number in a List
#Question: Write a Python program to find the second largest number in the list [12, 45, 98, 34, 23].

list1=[12, 45, 98, 34, 23]
second_largest=0
for num in list1:
    if num>second_largest:
        second_largest=num
print(second_largest)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




