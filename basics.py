a = 10
ananyo = 1
type(a)
type(ananyo)
7 + 8
a + ananyo 
type(a + ananyo )
b = 2.09
type(b)
c = 23.20
type(c)
d = "ananyo"
type(d)
e = 'this is my 1st tech class .'
type(e)
#  example :  int = 10 , float = 23.45 , str = 'ananyo '
n = True 
m = False 
type(n)
type(m)
# ex 2 : boolean variables , True , False 
# True = 1 , False = 0 
n + m
type(n +m)
True * False
False / True
# True / False, in numpy module it will give you infinity but here it will show you error 
# complex number 
v = 5 + 8j 
type(v)
v.imag
v.real
a = 7 + 8j
a.real
a.imag
type(v)
a
print('my name is Ananyo')
print(a)
s = 'pwskills' # stored in the system as a combination of characters .
type(s)
s[0]
s[1]
s[-8]
s[-7]
s[-1]
s[0::]
s[9::]
s[-6]
s[4]
s[5]
s 
s[-8]
s[2]
s[0:2]
s[0:3]
# slicing (upper bound -1) 
s[0:4]
s[0:8]
s[0:8:2]
s[::2]
s[2::2]
s[2::6]
s[::-1]
s[2:7:-1]
# it will give you a blank beacuse youre going to positive direction and jumping into a negetive direction
s[2:7:-1]
# conflict arises and blank is given  by the interpreter 
s[8:0]
# it will give you blank beacuse by default the jump is +1
s[8:0:-1]
s[::-1]
s[::1]
s[-2:-8:1]
s[-2:-8:-1]
s[0:3]
s[8:0:1]
s[8:0:-1]
s[0:8]
s[::8]
s[::-1]
s[::1]
# s[90] # string index out of range 
s[::-90]
s[:-90 :]
s[:-9000:-1]
c = 200
# c[0] int object is not subscriptable its a whole object 
d = '200'
d[1]
s1 = 'this is my string class'
# string manipulation 
len(s1)
s1.find('s')
s1.find('i')
# find( finds the lower index of sub string )
s1.find('iS')
s1.find('is')
s1.count('s')
s1.count('st')
s1
s1.upper()
s1 
s2 ='CEWF CEWIVEUHECUEC CI'
s2.lower()
s1.title()
s1.capitalize()
s1+'sudh'
s1 + '1'
s1 + str(1)
s*3
# "sudh"/4 , str dont support division operation 
"don't do copy and pest in my class ."
# this is my 1st class for programming 
"""lol I care about comments , its necessary for coders to understand the thing another one written ."""

# List 

# premitive data type , the basic data type we learned before 

l1 = [1,345,45,True , 5+7j,'ananyo']
type(l1)
# list is created under square [] bracket 
l1[0]
l1[1]
l1[3]
l1[5]
type(l1[4])
# you can put anything in list[] 
l1[0:3]
# (upper bound -1 ) 
l1[-1]
# in terms of slicing same concept is applicable 
l1[::2]
s = 'pwskills'
list(s)
l1
l1[-1][0:2] #,again using slicing concept 
l1[3]
str(l1[3])[0:2] # typecasting , 1st converting the data type from 1 data type to another data type 
# l1 + 5 , you cant concatenate list and integers 

l2 = [3,4,5]
l1+l2
l1*3
len(l1)
len(l1+l2)

l1
l1.append(5)
l1
l1.append(s)
l1
l1.append(l2)
l1
l1[-1][1]

l1
# l1.extend(4)
l1.extend('ananyo')
l1.extend(l2)
l1
l1.insert(1,'subho')
l1
l1.insert(0,[2,3,4])
l1
l1.insert(-1,45)
l1
l1.remove(5)
l1.insert(27,51)
l1
l1.pop(27)
l1
# pop removes data from indexes , if you dont put indexes it will remove data from -1 index

l1.pop(2)
l1.pop(2)
l1.pop(3)

l1
l1.pop(6)
l3 = [1,2,3,4,'subho']

l3.insert(1,'sudh')
l3
l1
l1.insert(0,45)
l1
l1.insert(-1 ,45)
l1.pop()
l1.pop()
l1.pop(2)
l3
l3.pop(3)
l3.remove(1)
l3
l1
l1.remove([2,3,4])
l8=[2,3,4]
# string is a immutable object 
l1[::-1]
l1.reverse()
l1
l1.reverse()
# l1.sort() ,only integers 
l0=[2 ,7 ,5,6,4,3,1,0]
l0.sort()
l0
# l3.sort 
# l3 
l4 =['pw', 'skill' ,'kota' ]
l4.sort()
l4
l5 = [1,2,3,6, 9,8]
l5.sort(reverse=True)
l5

l5.index(2)
l5.count('9')
l5.count(9)
s = 'ananyo'
l6=[3,4,5,6]
s[0]
# s[0] = 'a' 
l5[0]= 30
l5
# str object doesnt support mutability 
l7 =[3,4,5,6]
s.replace('a','s')

# TUPLE

t=(2,3,4,5,5.6,7+8j,False,True,[3,4,5])
type(t)
len(t)
t[0]
t[-1]
t[::-1]
# t[0]=2323
# tupples are immutable , lists are mutable 
# for making password tupples are used 
t.count(4)
t.index(False)
# SET 

# s1 = {} , dictionary
type(s1)
s2= {2,4,5,6,7}
type(s2)
s3 = {23.87,23 ,6+7j,9,0,'ananyo', (2,3,4)}
# only takes immutable objects 
s6= {2,2,2,3,33,4,4,5,6,7,8,'sudh','Sudh'}
s4
# to remove duplicate data we use set 
m6=list(set(m6))
# m6
s6
# set build unordered collection of unique elements 
# set never arrange data in order 
# indexing , slicing not going to work in case of set 
s6.add(34)
s6
s6.remove('sudh')
s6
# set removes all the duplicates .
# python is a case scencitive language 


# dictionary 
# key and value pair 
d1 = {} #blank dict
type(d1)
d2 = {'key':"ananyo"} #key should always be unique 
d2
d3 = {'name' : "sudhangsu",'email':"ss@gmail.com","number" :8679}
d3
d4 = {234 : 'ananyo'} # special case characters cant be added as a key under dict
d5 = {True :2345 } # bool is alowed as a key
d6 = {'ananyo': "lol", True : 9870}
d6['ananyo']
d6[True]
d6[1]
d3['email']
d7 = {'name':'ananyo' ,'mail_id':'ananya@gmail.com',"name": 'ananya'}
d7['name']
# if  key is not unique it will overwrite it 
d8 = {'company':"pwskills",'course':["webdev" ,"data science", "android dev"]}
d8
d8['course'][1]
d9 = {'number':[2,34,4,3,4] , 'assignment':(1,2,3,4,5,6) , 'launch_date':{28,12,23}}
d9
d9["launch_date"]
d9['mentor'] =['sudhangsu','krish','anurag']
d9
del d9['number']
d9
list(d9.keys())
d9.items()
d9.pop('assignment')


# Control flow 

# control statement = decision making statement 



