# print(len("python")) 

# a="python"
# print(a,type(a))
# print(a[54])

# print("python"[0]) 
# print("python"[1]) 
# print("python"[2]) 
# print("python"[3]) 
# print("python"[4]) 
# print("python"[5]) 
# print("python"[6]) 

""" concatenation:=
Used only for strings. Will combine more than one string together.
we use + to represent concatentation in the strings concept.
string is immutable, modifications cannot be made"""

# v="department"
# print(v[3]+v[2]+v[3]+v[4]+v[5]+v[6]+v[7]+v[8]+v[9])
# print(v[3]+v[2:])

# print("python"[-1]) 
# print("python"[-2]) 
# print("python"[-3]) 
# print("python"[-4]) 
# print("python"[-5]) 
# print("python"[-6]) 
# print("python"[-7]) 

# w="python"
# print(w[:]) 
# print(w[0:]) 
# print(w[0:6]) 
# print(w[-6:6])
# print(w[0:0]) 
# print(w[0:1]) 
# print(w[0:2]) 
# print(w[0:3]) 
# print(w[0:4]) 
# print(w[0:5]) 
# print(w[0:6]) 
# print(w[0:7]) 
# print(w[0:99]) 
# print(w[0:0]) 
# print(w[3:2]) 
# print(w[5:3]) 
# print(w[0:-1]) 
# print(w[0:-2]) 
# print(w[0:-3]) 
# print(w[0:-4]) 
# print(w[0:-5]) 
# print(w[0:-6]) 
# print(w[0:-7]) 

# r="python"
# print(r[2:5]) 
# print(r[3:4]) 
# print(r[5:2]) 
# print(r[5:5]) 

# y="python"
# print(y[-1:-6])
# print(y[2:-5])
# print(y[-6:])

c="python"
# print(c[ : : ]) 
# print(c[0 : : 1]) 
# print(c[ : :2]) 
# print(c[ : :3]) 
# print(c[ : :4]) 
# print(c[ : :5]) 
# print(c[ : :6]) 
# print(c[: : -1]) 
# print(c[:  :-2]) 
# print(c[ : :-3]) 
# print(c[ : :-4]) 
# print(c[ : :-5]) 
# print(c[ : :-6]) 
# print(c[1: : ]) 
# print(c[2: : ]) 
# print(c[3: : ]) 
# print(c[4: : ]) 
# print(c[5: : ]) 
# print(c[6: : ]) 
# print(c[1: 6: ]) 
# print(c[2: 5: ]) 
# print(c[3: 4: ]) 
# print(c[4: 3: ]) 
# print(c[5: 2: ]) 
# print(c[6: 1: ]) 

"""Strings:
string is immutable, modifications cannot be made"""

# a="python"
# print(a,type(a))
# print(a[0])
# a[0]='P'

# print(dir(str))

# print(len(['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']))

# name="hEllo PyThon"
# print(name.capitalize())

# name="hEllopyThon"
# print(name.capitalize())

# name="hEllo pyThon"
# print(name.casefold())
# print(name.lower())

# name="hEllopyThon"
# print(name.casefold())
# print(name.lower())

# name="hEllo pyThony"
# print(len(name)) # 13
# print(name.center) 
# print(name.center()) 
# print(name.center(50,'*'))
# print(name.center(100))

# name="hEllo pyThon"
# print(type(name))
# n=name.encode()
# print(n) 
# print(n.decode()) 
# print(type(b'hello'))


# name='hEllo pyThon'
# print(name.upper())
# print(name.lower())
# print(name.isupper())
# print(name.islower())
# b="CRICKET"
# print(b.isupper())
# m='worldcup t20'
# print(m.islower())

# t='hEllo pyThon'
# print(t.title())
# print(t.capitalize())
# print(t.istitle())
# c='Hello Python'
# print(c.istitle())

# n='hEllo pyThon'
# print(n.endswith()) # TypeError: endswith() takes at least 1 arguent, (0 given)
# print(n.endswith(''))
# print(n.endswith(' '))
# print(n.endswith('n'))

# n='hEllo pyThon'
# print(n.startswith(''))
# print(n.startswith(' '))
# print(n.startswith('h'))

# z=' hEllo pyThon'
# print(z.startswith(''))
# print(z.startswith(' '))
# print(z.startswith('h'))


# v=''
# g='    '
# print(v.isspace())
# print(g.isspace())

# q="hEllo pyoTholno"
# print(q.index('l'))
# print(q.index("p"))
# print(q.index('l',4))
# print(q.index('o'))
# print(q.index('o',5))
# print(q.rindex('o'))
# print(q.index(1))

# r="hEllo pyThon programming"
# print(r.index('b')) # ValueError
# print(r.index('n'))
# print(len(r))
# print(r.rindex('g'))

# r="hEllo pyThon programming"
# print(len(r))
# print(len('josh innovations'))

# print(dir(str))

# n=['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
# 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
# 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 
# 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 
# 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
# 'removesuffix', 'replace','rfind', 'rindex', 'rjust', 'rpartition', 
# 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 
# 'swapcase', 'title','translate', 'upper', 'zfill']
# print(len(n))

# w="_3hello"
# print(w.isidentifier())

# b="python programming"
# print(b.find('p')) 
# print(b.find('e')) 
# print(len(b))
# print(b.rfind('m')) 

# v="python programming"
# print(v.count('p')) 
# print(v.count('m')) 
# print(v.count('i')) 
# print(v.count('e')) 

# h="python course"
# print(h.replace('course','programming'))
# g="core python programing core"
# print(g.replace('core',2))
# print(g.replace('core',str(2)))
# print(g.replace('core','2'))
# print(g.replace('o','k',1))
# print(g.replace('o','k',2))
# print(g.replace('o','k',3))
# print(g.replace('o','k',4))
# print(g.replace('o','k',5))
# print(g.replace('o','k',(2)))

# d="       python programming  .      "
# print(d.strip())
# print(d.lstrip())
# print(d.rstrip())

# e="  hello python      ".strip()
# print(len(e))

# a="hello","Python",'pro'
# print(a , type(a))
# b=' World '.join(a)
# print(b)
# print("Hello", "Python" ,"pro",sep=" World ")


# c="hey"
# d="*".join(c)
# print(d)
# e="hey",
# f="*".join(e)
# print(f)
# g="hey",""
# h="*".join(g)
# print(h)

# c="Python Programming"
# print(c.removeprefix('p'))
# print(c.removeprefix('P'))
# print(c.removeprefix('Py'))
# print(c.removesuffix('g'))
# print(c.removesuffix('ng'))
# print(c.removesuffix('ming'))

"""isalnum: 
will return True , only if the string contains
only alphabets and numeric , even alphabets and
numeric can be kept inside the string , but
space/spaces and special symbols are not allowed.
if kept spaces or special symbols then it will return False
i.e. no spaces and no special symbols allowed"""


# a="hello python"
# print(a.isalnum()) # space not allowed in isalnum

# a="hellopython"
# print(a.isalnum())  # returns True bcz no space

# a="hello.python"
# print(a.isalnum())  # returns False bcz .(point) or special symbols are not allowed

# a="hellopython39"
# print(a.isalnum()) # returns True because contains only alphabets and numeric


# b="core python"
# print(b.isalpha())

# b="corepython"
# print(b.isalpha())

# b="corepython39"
# print(b.isalpha())

# b="6"
# print(b.isalpha())

# b="H"
# print(b.isalpha())

# b=""
# print(b.isalpha())

# b=" "
# print(b.isalpha())

# v="august python"
# print(v.isascii())

# b=chr(0)
# c=chr(32)
# print(b.isspace())
# print(c.isspace())
# print("hello"+chr(32)+"Python")
# print("hello"+' '+"Python")
# print("hello","Python",sep=' ')
# print("hello","Python")

# print(chr(32)+"Hey")
# print(chr(0)+"Hey")

# print(ord('a')) 
# print(ord('z')) 
# print(ord('A'))
# print(ord('Z'))
# print(ord('0'))
# print(ord('9'))
# print(ord(' '))
# print(ord('!'))

"""To find the ascii value"""
# print(chr('0')) # TypeError: an integer is requried (got type str)
# print(chr(97)) # a
# print(chr(65)) # A
# print(chr(30)) # ▲
# print(chr(31)) # ▼ 
# print(chr(32)) # 
# print(chr(32).isspace()) # True

# print(ord("a"))
# print(ord("z"))
# print(ord("A"))
# print(ord("Z"))
# print(ord("_"))
# print(ord(" "))
# print(ord("\t"))
# print(ord("0"))
# print(ord("9"))
# print(ord('')) # TypeError: ord() expexted a character, but string of length 0 found

# v=bin(5)
# print(v,type(v))
# h=0b101
# print(h,type(h)) 
# j=0B101
# print(j,type(j))

# print(bin(23))
# print(0b10111)
# print(0B10111)

# f=oct(11)
# print(f,type(f))
# print(0o13)
# print(0O13)

# w=hex(18)
# print(w,type(w))
# print(0x12)
# print(0X12)
# print(0xA)
# print(0xD)
# print(0xF)


# a=65
# print(a,type(a))
# print(ord('1'))
# print(chr(0o142))
# print(chr(0o41)) # !
# print(ord('A')) # 65
# print(chr(0X61))  # a
# print(chr(65)) # A

# p="pythON proGRAMming"
# print(p.swapcase()) 

# a=4  ; b=66
# print(a)
# del a,b
# print(a,b)

'''Format'''
# print("Buy this for Rs.{ed} or for Rs.{d}".format(d=11,ed=50))

'''expandtabs  , by default=8'''
# a='R\tS\tV'
# print(a.expandtabs(0))
# print(a.expandtabs(1))
# print(a.expandtabs(2))
# print(a.expandtabs(3))
# print(a.expandtabs(4))
# print(a.expandtabs(5))
# print(a.expandtabs(6))
# print(a.expandtabs(7))
# print(a.expandtabs(8))
# print(a.expandtabs())
# print(a.expandtabs(-1))

""" join """
# v='hello','python','core'
# n='python'
# print('-'.join(v))
# print('*'.join(n))
# print('*'.join("Hello"))

""" maketrans and translate"""
# r="helly hello"
# a=r.maketrans("l",'u')
# print(a,type(a))
# print(r.translate(a))

# r={}
# print(r,type(r))
# v={1:'hello', 2:'python'}
# print(type(v))
# print(v[1])

# a="hello\nCore Python\nProgramming"
# print(a.index('C'))
# print(a.index('n'))
# print(a[6:17])
# print(a)
# g=a.splitlines()
# print(g)
# print(g,type(g))
# print(g[0])
# print(g[1])
# print(g[2])
# h="HelloWelcome to JoshInnovations"
# w=h.split()
# print(w,type(w))
# print(w[0][:5])
# print(h.split(" "))
# print(h.split(""))

# a=5.6,7
# print(a,type(a))

# a=[int(x) for x in input().split()]
# print(a,type(a))
# print(sum(a))
# print("The sum is"+' '+str(sum(a)))
# print("The sum is",sum(a))

# v="Hello Welcome to JoshInnovations"
# print(v.split())

# b="Hello:Welcome: To:Josh:Innovations"
# print(b.split(":"))

# n="Python#C#Java#R#Dart"
# print(n.split("#"))
# print(n.split("#",0))
# print(n.split("#",1))
# print(n.split("#",2))
# print(n.split("#",3))
# print(n.split("#",4))

# v=r"hello\bprogramming"
# print(v,type(v))


# k="Hello!\nWelcome to \nJoshInnovations"
# print(k.splitlines())

# y="Hello!\nWelcome to \nJoshInnovations"
# print(y.splitlines(True))
# print(y.splitlines(False))
# print(y.splitlines())

# f="hello"
# print(f.zfill(10))

# j="Hey! How are you Doing?"
# print(j.partition("are"))

# t="Hey! How are you Doing?"
# r=t.partition("you")
# print(r)
# print(r[2])

# m="We are Learning Python Programming , Python is Basic need \
#  for ML,DS,AI,DL,BigData..etc"
# print(m.partition("Python"))
# print(m.rpartition("Python"))

# c="Python"
# print(c.ljust(8),"Programming Basics")

# x="Python"
# print(x.rjust(8),"Programming Basics")

# z="Python"
# print(z.rjust(10),'R')
# print(z.rjust(10,'R'))

# s="Python"
# print(s.ljust(10,'R'))



""" Optional """
# w= "Python, C, Java"
# d=w.rsplit(",", 1)
# t=w.rsplit(", ", 1)
# r=w.split(' ', 1)
# print(d)
# print(t)
# print(r)


# a='_ello'
# print(a.isidentifier())
# b='hello'
# print(b.isidentifier())
# c='Hello'
# print(c.isidentifier())
# d='_'
# print(d.isidentifier())
# e='_32'
# print(e.isidentifier())
# f='1abc'
# print(f.isidentifier())
# g='.1abc'
# print(g.isidentifier())
# h='1a bc'
# print(h.isidentifier())


# print(dir(str))


