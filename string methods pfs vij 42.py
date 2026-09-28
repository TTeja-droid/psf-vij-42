Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
a="python"
len(a)
6
a="python course"
len(a)
13
a=""
len(a)
0
a=" "
len(a)
1
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("t")
5
a.count("")
28
a.count(" ")
3

#finding string
#find a string
a="python"
a.find("t")
2
a="hello"
a.find("l")
2
a[h]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a[h]
NameError: name 'h' is not defined
a[3]
'l'
#escape sequences
#\n=new line
#\t=tab space
a="name\nphn no\temail id"
print(a)
name
phn no	email id
a="name:Teja\nphn no:6300486121\temail id:tejakanteti2005@gmail.com\n branch:CSE"
print(a)
name:Teja
phn no:6300486121	email id:tejakanteti2005@gmail.com
 branch:CSE
a="name:Teja\nphn no:6300486121\temail id:tejakanteti2005@gmail.com\nbranch:CSE"
print(a)
name:Teja
phn no:6300486121	email id:tejakanteti2005@gmail.com
branch:CSE
#replace()
a="wait untill succecc"
a.replace("wait,work")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.replace("wait,work")
TypeError: replace() takes at least 2 positional arguments (1 given)
a.replace("wait","work")
'work untill succecc'
b="python full stack"
a.replace("full stack","dsa")
'wait untill succecc'
b.replace("full stack","dsa")
'python dsa'
a="wait untill succecc"
b=a.replace("wait","work")
SyntaxError: multiple statements found while compiling a single statement
b=a.replace()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    b=a.replace()
TypeError: replace() takes at least 2 positional arguments (0 given)
a="wait untill succecc"
b=a.replace("wait","work")
b
'work untill succecc'
#upper()
a="code"
a.upper()
'CODE'
a.upper("c")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.upper("c")
TypeError: str.upper() takes no arguments (1 given)
#lower case
a="Data"
a.upper()
'DATA'
a.lower()
'data'
#if staring letter wanted to be capital
a="data"
a.capitalise()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a.capitalise()
AttributeError: 'str' object has no attribute 'capitalise'. Did you mean: 'capitalize'?
a.capitalize()
'Data'
#if in a sentence the staring letter of a word should be in capiatal
a="i am teja"
a.title()
'I Am Teja'
a.capitalize()
'I am teja'
a="python"
a.isupper()
False
a.islower()
True
a="data structures"
a.alpha
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.alpha
AttributeError: 'str' object has no attribute 'alpha'. Did you mean: 'isalpha'?
a.alpha()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a.alpha()
AttributeError: 'str' object has no attribute 'alpha'. Did you mean: 'isalpha'?
a.startswith("d")
True
a.endswith("s")
True
a.isdigit()
False
a=1234
a.isdigit()
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
a="1234"
a.isdigit()
True
a="teja123"
a.isalnum()
True
a="teja@123"
a.isalnum()
False
#strip
#lstrip=left space
#rstrip=rightspace
a="    i am teja    "
a.strip()
'i am teja'
a.lstrip()
'i am teja    '
a.rstrip()
'    i am teja'
#concatination
a="Teja"
b="is lazy
SyntaxError: unterminated string literal (detected at line 1)
b="is lazy"
print(a+b)
Tejais lazy
print(a+" "+b)
Teja is lazy
fname="teja"
lname="kanteti"
print(fname+" "+lname)
teja kanteti
print(fname+" "+lname).title
teja kanteti
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    print(fname+" "+lname).title
AttributeError: 'NoneType' object has no attribute 'title'
print((fname+" "+lname).title)
<built-in method title of str object at 0x00000111250DB670>
print(fname+" "+lname).title)
SyntaxError: unmatched ')'
print((fname+" "+lname).title())
Teja Kanteti

#split
a="c c++ python"
a.split()
['c', 'c++', 'python']
a="i am learing pyton"
a.split()
['i', 'am', 'learing', 'pyton']
#join
a="apple","banana","grapes"
"".join()
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    "".join()
TypeError: str.join() takes exactly one argument (0 given)
"".join(a)
'applebananagrapes'
" ".join(a)
'apple banana grapes'
"l".join(a)
'applelbananalgrapes'
a="apple"
"l".join(a)
'alplpllle'
#formating
a=3
b=4
print(a+b)
7
print("the sum of",(a+b))
the sum of 7
city="vij"
print("the city",(city))
the city vij
#format method
#format()
a="motu"
b="pathulu"
print("hello {}{}".format(a,b))
hello motupathulu
print("hello {} {}".format(a,b))
hello motu pathulu
print("hello {} hello{}".format(a,b))
hello motu hellopathulu
print("hello {} hello {}".format(a,b))
hello motu hello pathulu
print(("hello {} hello {}".format(a,b)).title())
Hello Motu Hello Pathulu
print("hello {} hello {}".format(a,b).title())
Hello Motu Hello Pathulu
#fstring
a="teja
SyntaxError: unterminated string literal (detected at line 1)
>>> a="teja"
>>> b="kanteti"
>>> print(f"hello {a}{b}")
hello tejakanteti
>>> print(f"hello {a} {b}")
hello teja kanteti
>>> print(f"hello {a} {b}").title()
hello teja kanteti
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    print(f"hello {a} {b}").title()
AttributeError: 'NoneType' object has no attribute 'title'
>>> print((f"hello {a} {b}").title())
Hello Teja Kanteti
>>> a=3
>>> b=4
>>> print(f"{a}*{b}")
3*4
>>> a=3
>>> b=4
>>> print(f"{a*b}")
12
>>> a=5
>>> b=5
>>> c=a*b
>>> print(c)
25
print("the product of ".format(c))
the product of 
print("the product of {}".format(c))
the product of 25
print(f"the product is")
the product is
print(f"the product is {}")
SyntaxError: f-string: valid expression required before '}'
