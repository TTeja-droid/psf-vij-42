Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[[]
a=[3,4.5,"python",6+9j,True,False]
print(a)
[3, 4.5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=9.8
type(b)
<class 'float'>
c=[9.8]
type(c)
<class 'list'>
#append
a=["python","java","c"]
a.append(c++)
SyntaxError: invalid syntax
a.append("c+")
a
['python', 'java', 'c', 'c+']
b=["ds","ai"]
b.append(["c","c++"])

b
['ds', 'ai', ['c', 'c++']]
#insert
a=["python","java","c"]
a.insert(1,"ds")
b
['ds', 'ai', ['c', 'c++']]
a
['python', 'ds', 'java', 'c']


a=["python","java","c"]
a.insert(1,"ds")
SyntaxError: multiple statements found while compiling a single statement
a
['python', 'ds', 'java', 'c']
#index
#index
a=["hyd","vij","vizag"]
a.index(vizag)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.index(vizag)
NameError: name 'vizag' is not defined
a.index("vizag")
2
a.copy()
['hyd', 'vij', 'vizag']
#sort()
a=["mango","apple","grapes","banana"]
a.sort()
a
['apple', 'banana', 'grapes', 'mango']
b=[7,5,9,3,0,1,2,20,30,25]
b.sort()
b
[0, 1, 2, 3, 5, 7, 9, 20, 25, 30]
#reverse
a=["black","white","red","blue"]
a.reverse
<built-in method reverse of list object at 0x00000228BF9CFE40>
a.reverse()
a
['blue', 'red', 'white', 'black']
b=[1,2,3,4,5,6,7,8,9]
b.reverse()
b
[9, 8, 7, 6, 5, 4, 3, 2, 1]
#pop()
a=["java","ds","ai"]
a.pop()
'ai'
a
['java', 'ds']
a.pop(0)
'java'
a
['ds']
a.remove("ds")
a
[]
b=("chair","table")
b.clear()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    b.clear()
AttributeError: 'tuple' object has no attribute 'clear'
b
('chair', 'table')
b.clear()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    b.clear()
AttributeError: 'tuple' object has no attribute 'clear'
b
('chair', 'table')
c=[]
c.append("praveen")
c
['praveen']
a=["hi","hello"]

len(a)
2
b="hello"
len(b)
5
c["hello"]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    c["hello"]
TypeError: list indices must be integers or slices, not str
c=["hello"]
len(c)
1
#tuple()
a=(4,6.7,"praveen",8+9j,True,false)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a=(4,6.7,"praveen",8+9j,True,false)
NameError: name 'false' is not defined. Did you mean: 'False'?
print(a)
['hi', 'hello']

a=(4,6.7,"praveen",8+9j,True,False)
print(a)
(4, 6.7, 'praveen', (8+9j), True, False)
type(b)
<class 'str'>
type(a)
<class 'tuple'>
#sets{}
a={3.6.7,"python",8+9j,True,False}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a={3,6.7,"python",8+9j,True,False}
print(a)
{False, True, 3, (8+9j), 6.7, 'python'}
type(a)
<class 'set'>
a={4,5,6,7,8,9}
a.add(10)
a
{4, 5, 6, 7, 8, 9, 10}
a={1,2,3,4,5,6}
b={5,6,7,8,9,10}
a.issubset(b)
False
b.issubset(a)
False
a=
SyntaxError: invalid syntax
a={2,3,4,6,7,8}
b={5,6,7,8,}
b.issubset(a)
False
a.issubset(b)
False
a={4,5,6,7,8,9}
b={7,8,9}
a.issuperset(b)
True
b.issuperset(a)
False
#union()
a={10,11,12,13,14,15}
b={14,15,16,17,18,19}
a.union(b)
{10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
a
{10, 11, 12, 13, 14, 15}
#intersection()
a={4,5,6,7,8,9,10}
b={8,9,10,11,12,13}
a.intersection(b)
{8, 9, 10}
#update()
a={3,4,5,6,7,}
b={6,7,8,9,10}
a.update(b)
a
{3, 4, 5, 6, 7, 8, 9, 10}
a
{3, 4, 5, 6, 7, 8, 9, 10}
b
{6, 7, 8, 9, 10}

b.update(a)
b
{3, 4, 5, 6, 7, 8, 9, 10}
#difference()
a={5,6,7,8,9,10,11}
b={9,10,11,12,13,14}
a.difference(b)
{8, 5, 6, 7}
b.difference(a)
{12, 13, 14}
#symmetric_difference
#difference_update()
a={4,5,6,7,8,9}
b={6,7,8,9,10,11}
a.difference_update(a)
a
set()
b
{6, 7, 8, 9, 10, 11}
a
set()
#intersection_update()
a={5,6,7,8,9,10,11}
b={9,10,11,12,13,14}
a.intersection_update(b)
a
{9, 10, 11}
>>> b.intersection_update(a)
>>> b
{9, 10, 11}
>>> #symmetric_difference_update()
>>> a={10,20,30,40,50}
>>> b={30,40,50,60,70}
>>> a.symmetric_difference_update(b)
>>> a
{20, 70, 10, 60}
>>> b.symmetric_difference_update(a)
>>> b
{50, 20, 40, 10, 30}
>>> #pop()
>>> a={2,3,4,5,6,7}
>>> a.pop()
2
>>> a
{3, 4, 5, 6, 7}
>>> a.remove(5)
>>> a
{3, 4, 6, 7}
>>> a={5,6,7,8,9,10}
>>> a.copy()
{5, 6, 7, 8, 9, 10}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(60)
>>> 
>>> b
{60}
>>> #disjoint()
>>> a={4,5,6,7,8}
>>> b={9,10,11,12}
>>> a.isdisjoint(b)
True
