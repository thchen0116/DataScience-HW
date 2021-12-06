#!/usr/bin/env python
# coding: utf-8

# In[2]:


f=open("C:\\Users\\vivia\\Desktop\\Vivian\\datascience\\IMDB-Movie-Data.csv","r")
lines=f.readlines()
f.close()
data=[]
for t in range(len(lines)):
    if t !=0:       
        sp=lines[t].split(",")
        data.append(sp)


# open檔案之後，用for-loop刪掉第一列之後，再把其他列用","分開存在data中

# In[3]:


#problem1
rating,result=[],[]
a=[]
movie=[]
dict1={}
for i in range(len(data)):
    if "2016" in data[i][5]:
        movie.append(data[i][1])
    for j in range(len(movie)):
        if movie[j] in data[i][1]:
            rating.append(data[i][7])
dict1=dict(zip(movie,rating))
dict1=dict(sorted(dict1.items(), key=lambda item: item[1],reverse=True)) 
rating=list(set(rating))
rating.sort(reverse=True)    
print("Top-3 movies with the highest ratings in 2016:",end=' ')
for i in range(3):
    for j in range(len(dict1)):
        key1=list(dict1.keys())
        value1=list(dict1.values())
        if rating[i] == value1[j]:
            result.append(key1[j])
for i in range(len(result)):
    if i < len(result)-1:
        print(result[i],end=" , ")
    else:
        print(result[i])


# 先找2016年的電影名稱，存成一個list，再用電影名稱去找相對應的rating，並存成另一個list，
# 利用dictionary把movie跟rating的list包再一起，movie是key，rating是value，
# 用set把ratingt重複的數字去掉，再用sort由大到小排序，
# 最後用for-loop找到前三名並存在result裡。

# In[4]:


#problem2
actor,genere,num,generes=[],[],[],[]
dict1={}
actors,act,result=[],[],[]
for i in range(len(data)):
    sp=data[i][4].split('|')
    for j in range(len(sp)):
        act.append(sp[j].strip(" "))
actors=list(set(act))            #去掉重複的
for i in range(len(actors)):
    total = 0
    a = 0
    for j in range(len(data)):
        if actors[i] in data[j][4]:
            if data[j][9] == "":
                total += 0
                a += 1
            else:
                total += float(data[j][9])
                a += 1
    num.append(total/a)   
dict1=dict(zip(actors,num))
dict1=dict(sorted(dict1.items(), key=lambda item: item[1],reverse=True))
fin=max(num)             
print("The actor generating the highest average revenue:",end="")
for j in range(len(dict1)):
    key1=list(dict1.keys())
    value1=list(dict1.values())
    if fin == value1[j]:
        result.append(key1[j])
for i in range(len(result)):
    if i < len(result)-1:
        print(result[i],end=" , ")
    else:
        print(result[i])


# 先在data裡找所有演員的資料，並用split把"|"分開，
# 因為有些演員的名字前面會包含一個空格，所以用strip把空格去掉，
# 再利用set把重複的演員名字去掉，存成actors這個list，
# 從actors裡面找各個演員在data裡面所有對應到的revenue，
# 利用total去計算revenue總和，a則是計算總共的電影數量，然後再取平均(num)，
# 利用dictionary把actors跟num的list包在一起，actors是key，num是value，
# 用max取num裡的最大值，就可以找到最大的平均總收益，
# 最後用for-loop找到最大平均總收益對到的演員是誰並存在result裡。

# In[5]:


#problem3
actors=[]
num=0
total=0
for i in range(len(data)):
    actor=data[i][4].split("|")
    act=[]
    for j in range(len(actor)):
        act.append(actor[j].strip(' '))
    actors.append(act)
for j in range(len(actors)):
    if 'Emma Watson' in actors[j]:
        total += float(data[j][7])
        num+=1
print('The average rating of Emma Watson’s movies:',total/num)


# 先在data裡找演員的資料，並用split把"|"分開，
# 因為有些演員的名字前面會包含一個空格，所以用strip把空格去掉，
# 再利用set把重複的演員名字去掉，存成actors這個list，
# 從actors裡面找"Emma Watson"，如果再第j個項找到的話，
# 再用total去計算在data裡面所有對應到的rating總和，num則是計算總共的電影數量，
# 最後用print平均(total/num)。

# In[6]:


#problem4
director,actors,a,num,acts,result=[],[],[],[],[],[]
dict1={}
for i in range(len(data)):
    director.append(data[i][3])
director=list(set(director))            #去掉重複的
director.sort()
for i in director:
    b=[]
    for j in range(len(data)):
        if i == data[j][3]:
            a=data[j][4].split('|')
            for k in range(len(a)):
                a[k] = a[k].strip(' ')  #有些名字前面有" "
            b.extend(a)                 #b的迴圈結束，重新繼續
    actors.append(b)
for i in range(len(actors)):
    act=list(set(actors[i]))            #去掉重複的
    acts.append(act)
    num.append(len(acts[i]))
dict1=dict(zip(director,num))
dict1=dict(sorted(dict1.items(), key=lambda item: item[1],reverse=True))
print('Top-3 directors who collaborate with the most actors:',end=" ")
num=list(set(num))
num.sort(reverse=True)             
for i in range(3):                      #不確定會不會有名次並列的
    for j in range(len(dict1)):
        key1=list(dict1.keys())
        value1=list(dict1.values())
        if num[i]== value1[j]:
            result.append(key1[j])
for i in range(len(result)):
    if i < len(result)-1:
        print(result[i],end=" , ")
    else:
        print(result[i])


# 先在data裡找導演的資料，用set把重複的去掉，
# 用for-loop找每位導演對應到的電影有哪些，
# 然後在data裡那些電影中找演員的資料，並用split把"|"分開，
# 因為有些演員的名字前面會包含一個空格，所以用strip把空格去掉，
# 再存成actors這個list，用set把重複的演員名字去掉，避免重複計算，
# 用num去算每個導演對應到的演員人數有幾位，
# 利用dictionary把director跟num的list包在一起，director是key，num是value，
# 用set把num裡重複的數字刪掉，並由大到小排序，
# 最後用for-loop找到前三名並存在result裡。

# In[7]:


#problem5
genere,a,num,generes=[],[],[],[]
dict1={} 
actors,act,result=[],[],[]
for i in range(len(data)):
    sp=data[i][4].split('|')
    for j in range(len(sp)):
        act.append(sp[j].strip(' '))
actors=list(set(act))                  #去掉重複的
actors.sort()
for i in actors:
    b=[]
    for j in range(len(data)):
        if i in data[j][4]:
            a=data[j][2].split('|')
            b.extend(a)
    genere.append(b)
for i in range(len(genere)):
    gen=list(set(genere[i]))
    generes.append(gen)                  #去掉重複的
    num.append(len(generes[i]))
dict1=dict(zip(actors,num))
dict1=dict(sorted(dict1.items(), key=lambda item: item[1],reverse=True))
num=list(set(num))
num.sort(reverse=True)
print('Top-2 actors playing in the most genres of movies: ',end="")
for i in range(2):
    for j in range(len(dict1)):
        key1=list(dict1.keys())
        value1=list(dict1.values())
        if num[i]== value1[j]:
            result.append(key1[j])
for i in range(len(result)):
    if i != (len(result)-1):
        print(key1[i],end=" , ")
    else:
        print(key1[i])


# 先在data裡找所有演員的資料，並用split把"|"分開，
# 因為有些演員的名字前面會包含一個空格，所以用strip把空格去掉，
# 再利用set把重複的演員名字去掉，存成actors這個list，
# 從actors裡面找各個演員在data裡面所有對應到的genere，存成genere這個list，
# 在genere裡面的每項把重複的刪掉，存成generes這個list，
# 用num去算每個演員對應到的電影類型有幾個，
# 利用dictionary把actors跟num的list包在一起，actors是key，num是value，
# 用set把num裡重複的數字刪掉，並由大到小排序，
# 最後用for-loop找到前二名並存在result裡。

# In[8]:


#problem6
yeargap,a,num,actor=[],[],[],[]
dict1={}
actors,act,result=[],[],[]
for i in range(len(data)):
    sp=data[i][4].split('|')
    act1=[]
    for j in range(len(sp)):
        act.append(sp[j].strip(' '))
        act1.append(sp[j].strip(' '))
    actor.append(act1)
actors=list(set(act))       #去掉重複的
actors.sort()
for i in actors:
    b=[]
    for j in range(len(actor)):
        for k in range(len(actor[j])):
            if i == actor[j][k]:
                b.append(int(data[j][5]))
    a.append(b)
for i in a:
    gap=max(i)-min(i)
    num.append(gap)
dict1=dict(zip(actors,num))
dict1=dict(sorted(dict1.items(), key=lambda item: item[1],reverse=True))
num=list(set(num))
num.sort(reverse=True)
print('Top-3 actors whose movies lead to the largest maximum gap of years: ',end="")
for i in range(1):
    for j in range(len(dict1)):
        key1=list(dict1.keys())
        value1=list(dict1.values())
        if num[i]== value1[j]:
            result.append(key1[j])
for i in range(len(result)):
    if i != (len(result)-1):
        print(key1[i],end=" , ")
    else:
        print(key1[i])


# 先在data裡找所有演員的資料，並用split把"|"分開，
# 因為有些演員的名字前面會包含一個空格，所以用strip把空格去掉，
# 再利用set把重複的演員名字去掉，存成actors這個list
# 從actors裡面找各個演員在data裡面所有對應到的年分，把年份由str轉成int存在a，
# 在a裡的每一項，用最大值減去最小值就得到gap year，
# 把每位演員的gap year再存到num中，
# 利用dictionary把actors跟num的list包在一起，actors是key，num是value，
# 用set把num裡重複的數字刪掉，並由大到小排序，
# 最後用for-loop找到最大GAP YEAR的所有演員並存在result裡。

# In[9]:


#problem7
actors=[]
ans = []
for i in range(len(data)):
    actor=data[i][4].split("|")
    act=[]
    for j in range(len(actor)) :
        act.append(actor[j].strip(' '))
    actors.append(act)
def find(name):
    global ans
    rel = []
    for i in range(len(actors)):
        if name in actors[i]:
            actors[i].remove(name)
            for j in actors[i]:
                if j in ans:
                    continue
                rel.append(j)
                ans.append(j)
    rel = list(set(rel))
    for i in rel:
        find(i)

find("Johnny Depp")
ans.sort()
print('All actors who collaborate with Johnny Depp: ',end="")
for i in range(len(ans)):
    if i != (len(ans)-1):
        print(ans[i],end=" , ")
    else:
        print(ans[i])


# 先在data裡找所有演員的資料，並用split把"|"分開，
# 因為有些演員的名字前面會包含一個空格，所以用strip把空格去掉，
# 寫一個function重複找與Johnny Depp相關的演員存在rel及ans中，
# 再從rel中繼續找相關的演員，重覆到無新增演員為止。
