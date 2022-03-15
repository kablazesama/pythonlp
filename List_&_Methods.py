'''List Data Type
List is represented by square brackets [ ]
list is mutable, modifications can be made.
list can contain several datatypes in it.
we can represent an empty list'''


# a=[]
# print(a,type(a))

# p=["Ameerpet",55]
# print(p,type(p))
# print(p[0],type(p[0]))
# print(p[1],type(p[1]))

# a=None
# print(type(a))

# b=[2,7.9,"hi",None,True]
# print(b[0],type(b[0]))
# print(b[1],type(b[1]))
# print(b[2],type(b[2]))
# print(b[3],type(b[3]))
# print(b[4],type(b[4]))
# print(b[5],type(b[5])) # IndexError: list index out of range


'''Note: modifications cannot be made inside the string data type'''
# s="hello"
# print(s[3])
# s[0]='H' # TypeError: 'str' object does not support item assignment

'''Note: List will allow the modifications'''
# r=[4,3.1,"python"]
# r[0]=89.23
# r[-1]='GT'
# print(r)

# n=[1,3.7,"hello",[10,11]]
# print(n,type(n)) 
# print(n[0],type(n[0]))
# print(n[1],type(n[1])) 
# print(n[2],type(n[2])) 
# print(n[3],type(n[3])) 
# print(n[3][0],type(n[3][0])) 
# print(n[3][1],type(n[3][1])) 

# n=[1,3.7,"hello",[10,11]]
# n[0]=24
# n[3][0]=50
# print(n,type(n))
# print(n[0],type(n[0]))
# print(n[1],type(n[1]))
# print(n[2],type(n[2]))
# print(n[3],type(n[3]))


""" Append method of list will add the elements at
the end of the list"""
# n=[1,3.7,"hello",[10,11]]
# n.append('josh','hyd')
# print(n) 

# n=[1,3.7,"hello",[10,11]]
# n.clear()
# print(n)

# n=[5,10,15,20]
# print(n)
# b=n.copy()
# print(b)

# n=[5,10,'hello',10,'']
# print(n.count(' '))
# print(n.count(6))
# print(n.count(10)) 
# print(n.count("hello")) 

# a=[5,10,15]
# b=[1,3,5,7]
# a.extend(b)  
# print(a) 
# b.extend(a) 
# print(b) 

# n=[2,4,6,8,'hello',4.5,[56]]
# print(n.index(14.5))
# print(n.index(4.5))
# print(n.index(8)) 
# print(n.index('hello'))
# print(n.index([56])) 
# print(n.rindex[2])

# n=[1,3,5,7,11,13,15] 
# n.insert(0,'hello')
# n.insert(2,4)
# n.insert(-1,8) 
# n.insert(-2,10) 
# print(n)

# n=[10,20,30,40]
# print(n.pop())
# n.pop()
# print(n)
# n.pop(0)
# n.pop(6)
# print(n)

# n=[10,20,'hello',30,40]
# n.remove('hello')
# print(n)

# n=[1,2,3,4,5]
# print(n[::-1])
# n.reverse()
# print(n)

# n=[1,5,4,3,2]
# n.sort()
# print(n)
# n.sort(reverse=False)
# print(n)
# n.sort(reverse=True)
# print(n)


# j=[2.8,3.5,6.8,1.4,2.6]
# j.sort()
# print(j)

# k=['HD','LK','SL','HH','5','HA','s','BA','PA','DA','WM','LH','PZ']
# k.sort()
# print(k) 

# print(dir(list))
# print(len(['append', 'clear', 'copy', 
# 'count', 'extend', 'index', 'insert', 
# 'pop', 'remove', 'reverse', 'sort']))