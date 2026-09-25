Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
b=8.3
type(b)
<class 'float'>
a="Teja"
type(a)
<class 'str'>
f=5+3f
SyntaxError: invalid decimal literal
f=3+7j
type(f)
<class 'complex'>
f=7j
type(f)
<class 'complex'>
g=j
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    g=j
NameError: name 'j' is not defined
g="j"
print(g)
j
type(g)
<class 'str'>
a="True"
type(a)
<class 'str'>
b="true"
type(b)
<class 'str'>
a="False"
type(a)
<class 'str'>
b="false"
type(b)
<class 'str'>
#datatype conversions
#int
int(5)
5
int(9.8)
9
int("ji")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int("ji")
ValueError: invalid literal for int() with base 10: 'ji'
int(3+7j)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int(3+7j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(2)
2.0
float(9.8)
9.8
float"teja")
SyntaxError: unmatched ')'
float("teja")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    float("teja")
ValueError: could not convert string to float: 'teja'
flot(3+6j)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    flot(3+6j)
NameError: name 'flot' is not defined. Did you mean: 'float'?
float(True)
1.0
float(Falsr)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    float(Falsr)
NameError: name 'Falsr' is not defined. Did you mean: 'False'?
float(False)
0.0
#str
str(9)
'9'
str(8.3)
'8.3'
str(teja)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    str(teja)
NameError: name 'teja' is not defined
str("teja")
'teja'
str(3+6j)
'(3+6j)'
str(True)
'True'
str(False)
'False'
>>> #complex
>>> complex(3)
(3+0j)
>>> complex(3.8)
(3.8+0j)
>>> complex(t"teja")
SyntaxError: invalid syntax
>>> complex("teja")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    complex("teja")
ValueError: complex() arg is a malformed string
>>> complex(3+9j)
(3+9j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #boolean
>>> a=True
>>> type(a)
<class 'bool'>
>>> bool(4)
True
>>> bool(4,8
...      )
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    bool(4,8
TypeError: bool expected at most 1 argument, got 2
>>> bool(3.8)
...          
True
>>> bool("teja")
...          
True
>>> bool(3+5j)
...          
True
>>> bool(True)
...          
True
>>> bool(False)
...          
False
