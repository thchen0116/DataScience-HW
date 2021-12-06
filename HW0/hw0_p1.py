#!/usr/bin/env python
# coding: utf-8

# In[39]:


p=input("please enter the polynomial:")
p=p.split(')(')
a=[]
b=[]
c=[]
p[0]=p[0].strip("(")
p[-1]=p[-1].strip(")")
for i in range(len(p)):
    if "-" in p[i]: 
        p[i]=p[i].replace('-','+-')
    first=p[i].split("+")
    a.append(first)
for i in range(len(a)):
    b=[]
    for j in range(len(a[i])):
        if "*" not in a[i][j]:
            if "-" in a[i][j]:
                a[i][j]=a[i][j].strip("-")
                a[i][j]="-1*"+a[i][j]
            else:
                a[i][j]="1*"+a[i][j]
        mul=a[i][j].split("*")   
        b.append(mul)
    c.append(b)
print(c)
      
   


# 先把input的多項式用")("分開，再把頭尾的"("、")"去掉，在多項式裡面存成多個list，如果"-"在list裡面，就用"+-"取代"-"，再用"+"分開list存在a中，再判斷" * "是否再a的list裡面，如果沒有的話，就把a[i][j]前面多加上"1*"，存在c裡面。

# In[58]:


num=[]
var,var2,ans=[],[],str()
dict1={}
for i in range(len(c)):
    for j in range(len(c[i])):
        if i+1 >= len(c):
            continue
        for k in range(len(c[i+1])):
            n=int(c[i][j][0])*int(c[i+1][k][0])
            if n > 0 :
                n ="+" + str(n)
            num.append(n)
print(num)
for i in range(len(c)):
    for j in range(len(c[i])):
        if i+1 >= len(c):
            continue
        for k in range(len(c[i+1])):
            v=c[i][j][1] + c[i+1][k][1]
            var.append(v)
print(var)
for i in range(len(num)):
    a=str(num[i])+var[i]
    ans += a
print(ans.strip('+'))


# 進行相鄰兩項係數相乘及變數相乘(num/var)，係數相乘完如果大於0，則係數前面加上"+"，ans為係數結合變數

# In[ ]:




