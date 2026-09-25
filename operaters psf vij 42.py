Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arithmatic
a=3
b=8
print(a+b)
11
print(a_b)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(a_b)
NameError: name 'a_b' is not defined
print(a-b)
-5
print(a*b)
24
print(a//b)
0
print(a/b)]
SyntaxError: unmatched ']'
print(a/b)
0.375
print(a**b)
6561
print(a%b)
3
#assignment
a=5
b=4
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
9
a-=b
a
5
a-=5
a
0
a*=4
a
0
a//=4
a
0
a/=b
a
0.0
a**=4
a
0.0
a%=4

a
0.0
a=4
b=5
a+=b
b
5
b-=4
b
1
#comparision
a=4
b=9
a<b
True
a>b
False
a<=b
True
a>=b
False
#logical
a=9
b=8
a<b and b>a
False
a>b and b>a
False
a>b and b<a
True
a<b or a>b
True
a==b or a!=b
True
not False
True
not True
False
#identity
a=4
type
<class 'type'>
type(a) is float
False
type(a) is not int
False
type(a) is not float
True
type(a)is int
True
#membership
a= 2,3,4,5,6,7,7
7 in a
True
18 in a
False
19 is not in a
SyntaxError: invalid syntax
19 not in a
True
#bitwise
a=3
b=5
a&b
1
bin(2)
'0b10'
bin(3)
'0b11'
bin(6)
'0b110'
bin(11)
'0b1011'
#or
a=8
b=4
a|b
12
a&b
0
a=4
=(-a+2)
SyntaxError: invalid syntax
a=9
-(a+2)
-11
-a(-a+2)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    -a(-a+2)
TypeError: 'int' object is not callable
~a
-10
-(a+1)
-10
a^b
13
a=4
>>> a=11
>>> a^a
0
>>> a=4
>>> b
4
>>> a=4
>>> b=11
>>> a^b
15
>>> #left push
>>> a=4
>>> a<<2
16
>>> a=6
>>> a<<12
24576
>>> #right shift
>>> a=3
>>> b=7
>>> a>>4
0
>>> a>>2
0
>>> a>>1
1
