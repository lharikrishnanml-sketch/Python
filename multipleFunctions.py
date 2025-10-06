#!/usr/bin/env python
# coding: utf-8

# In[3]:


class multipleFunctions:
    def subfields(self):
        print("Machine Learning\n"
              "Neural Networks\n"
              "Robotics\n"
              "Vision\n"
              "Speech processing\n"
              "Natural Language Processing\n")
    def OddEven(self):
        oddeven=int(input("Enter the number"))
        if (oddeven%2==0):
             print("Even number")
             message = "Even number"
        else:
             print("Odd number")
             message=("Odd number")
        return message
        
    def Eligible(self):
        Gender=input("Enter your Gender")
        age=int(input("Enter your Age"))
        if Gender =="Male" and age==21:
            print("Eligible for Male Marriage")
            message="Eligible for Male Marriage"
        elif Gender=="Female" and age==18:
            print("Eligible for Female Marriage")
            message="Eligible for Female Marriage"
        else:
            print("Not eligible for marriage")
            message="Not eligible for marriage"
        return message
    def percentage(self):
        Subject1= 98
        Subject2= 87
        Subject3= 95
        Subject4= 95
        Subject5= 93
        marks=[Subject1,Subject2,Subject3,Subject4,Subject5]
        Total = sum(marks)
        average=sum(marks)/len(marks)
        print(f"Percentage of 10th mark is: {average}")
    def Areatriangle(self):
        Height=32
        Breadth=34
        Areaformula= (Height*Breadth)/2
        print(Areaformula)
    def perm_triangle(self):
        Height1=2
        Height2=4
        Breadth=4
        Perimeterformula= Height1+Height2+Breadth
        print(Perimeterformula)


# In[ ]:




