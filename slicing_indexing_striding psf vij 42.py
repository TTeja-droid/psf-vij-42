Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
 #indexing
a="i am in class"
a[2]
'a'
a[4]
' '
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[1]+a[4]+a[7]
'   '
a="vijayawada is a loyal city"
a[11]+a[12]+a[16]+a[17]+a[18]+a[19]+a[20]+a[22]+a[23]+a[24]+a[25]
'isloyalcity'
a[16]+a[17]+a[18]+a[19]+a[20]
'loyal'
a="vizag is a city of destiny"
a[-15]+a[14]+a[13]+a[12]
'cyti'
a[-15]+a[-14]+a[-13]+a[-12]
'city'
a[-26]+a[-25]+a[-24]+a[-23]+a[-22]
'vizag'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'destiny'
a="simple is better than complex"
a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
a[-28]+a[-27]+a[-26]+a[-25]+a[-24]+a[-23]
'imple '
a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]+a[-23]
'simple '
#slicing
a="codegnan"
a=[0:4]
SyntaxError: invalid syntax
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a"work hard until you succed"
SyntaxError: invalid syntax
a="work hard until you succed"
a[11:16]
'ntil '
a[10:16]
'until '
a[6:10]
'ard '
a[5:10]
'hard '
a[0:3]
'wor'
a[0:4]
'work'
a[20:26]
'succed'
a[10:15]
'until'
a="tims is very precious"
a="time is very precious"
a[13:21]
'precious'
a="i love python"
a[-8:-12]
''
a[-12:-8]
' lov'
a[-11:-9]
'lo'
a[-11:-7]
'love'
a[-6:-1]
'pytho'
a[-6;0]
SyntaxError: invalid syntax
a[-6:0]
''
a[-6:]
'python'
#striding
a="data science"
a[::]
'data science'
a[::1]
'data science'
a[::2]
'dt cec'
a[1::2]
'aasine'
a="machine learning"
a[::4]
'miln'
a[::6]
'men'
a[::2]
'mcielann'
a[5:]
'ne learning'
a[:9]
'machine l'
a[::7]
'm n'
a="cloud computing"
a[1:11:2]
'lu op'
a[2:14:4]
'ocu'
a[5:13:3]
' mt'
>>> a=[4:12:2]
SyntaxError: invalid syntax
>>> a[4:12:2]
'dcmu'
>>> a[4:11:2]
'dcmu'
>>> a[4:10:2]
'dcm'
>>> a="python course"
>>> a[-1:-11:2]
''
>>> a[-1:-11:-2]
'ero o'
>>> a[-2:-12:-3]
'sont'
>>> a[1::7]
'yo'
>>> a[0::2]
'pto ore'
>>> a[::2]
'pto ore'
>>> a="python course"
>>> a[::1]
'python course'
>>> a[::-1]
'esruoc nohtyp'
