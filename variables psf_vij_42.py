Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
print(4+8)
12
a=10
print
<built-in function print>
print(a)
10
x=50
print(x)
50
print(X)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
z=100
print(z)
100
3=90
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a3=90
print(a3)
90
5x=9
SyntaxError: invalid decimal literal
name="Teja"
print(name)
Teja
print("name")
name
city="vja"
print(city)
vja
country="India"
print(country)
India
a=3
b=8
print(a+b)
11
fname="Kanteti"
lname+"Teja"
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    lname+"Teja"
NameError: name 'lname' is not defined. Did you mean: 'name'?
print(fname+lname)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(fname+lname)
NameError: name 'lname' is not defined. Did you mean: 'name'?
fname="Kanteti"
lname="Teja"
print(fname+lname)
KantetiTeja
print(fname+""+lname)
KantetiTeja
print(fname+" "+lname)
Kanteti Teja
a=3,b=7
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=8;b=9
print
<built-in function print>
print(a+b)
17
a=8
b=7
print(a+b)
15
@=5
SyntaxError: invalid syntax
$=9
SyntaxError: invalid syntax
_=4
print(_)
4
>>> _a=40
>>> print(_a)
40
>>> if=29
SyntaxError: invalid syntax
>>> while=32
SyntaxError: invalid syntax
>>> a=2,3,4,5,5
>>> print(a)
(2, 3, 4, 5, 5)
>>> a,v,c=2,3,4
>>> print(a,v,c)
2 3 4
>>> first name="pooja"
SyntaxError: invalid syntax
>>> first_name="pooja"
>>> print(first_name)
pooja
>>> fristname="pooja"
>>> print(firstname)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    print(firstname)
NameError: name 'firstname' is not defined. Did you mean: 'first_name'?
>>> print(fristname)
pooja
>>> a=4
>>> print(a)
4
>>> a=(1,2,3)
>>> print
<built-in function print>
>>> print(a)
(1, 2, 3)
>>> a,b,c=(1,2,3)
>>> print(a,b,c)
1 2 3
>>> a=9
>>> print(a)
9
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a3'?
