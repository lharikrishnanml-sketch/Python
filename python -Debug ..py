#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.Find the error in the following Python code:

 for i in range(5):
    print(i)
    


# In[ ]:


#2.What will be the output of this code?

a = 10
b = 5
print(a + b)
 


# In[6]:


#3.What is the issue in this Python snippet?

def add_numbers(a, b):
     return a+b


# In[ ]:


#4.Identify the bug in the following Python code:

 numbers = [1, 2, 3, 4]
print(numbers[4])
array index out bound excepting , index value not present in this list


# In[ ]:


#5.Find the error in the following Python code:
print "Hello, World!"
didn't include brackets


# In[ ]:


#6.Find the error in the following Python code:
x = 5 / 0
exception error 


# In[ ]:


#7.Find the error in the following Python code:name = "Alice"
age = 25
print("Name: " + name + ", Age: " + age)
name alice is not defined


# In[ ]:


#8.Find the error
for i in range(1, 10, -1):
    print(i)
ideally it should be 10,1,-1 to decrement


# In[7]:


#9. Find the error in the following Python code:
x = 10
if x = 5:
    print("x is 5")
= operator should be ==


# In[2]:


userinput=int(input("Enter age"))
if userinput<18:
    print("not eligible to vote")
else:
    print("eligible to vote")
    


# In[4]:


list=[1,2,3,4,5,6,7,8,9,10]
print(max(list))
    


# In[10]:


userinput=float(input("enter salary to determine bonus eligibility and to apply bonus to your salary"))
if (userinput>50,000):
    bonus=userinput*0.10
    updatedsalary=userinput+bonus
    print(updatedsalary)
else:
    print("not eligible for bonus")


# In[12]:


userinput=int(input("enter number"))
if userinput%2==0:
    print("even number")
else:
    print("oddd number")


# In[13]:


text="hello"
revrerse_text=text[::-1]
print(revrerse_text)


# In[15]:


userinput=int(input("enter marks"))
if userinput>=40:
    print("pass")
else:
    print("fail")


# In[19]:


userinput=float(input("enter your total"))
if userinput>100:
    bonus=userinput*0.10
    updatedtotal=bonus+userinput
    print(updatedtotal)
else:
    print("not eliible for discount")


# In[20]:


numbers=[1,2,3,4,5,6,7,8,9,10]
for even in numbers:
    if even %2==0:
        print(even)


# In[22]:


userinput=int(input("Enter year"))
if userinput%4==0:
    print("leap year")
else:
    print("not leap year")


# In[ ]:




