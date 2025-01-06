#datatypes:- type of data that we can store in a veriable or in a perticular memory loctaion

#to check the datatype of a veriable "type()" is used & it is a built-in function
#example:-
a,b=10,'hello'
print(type(a),type(b))

#to ceck the memory address of a veriable "id()" is used & it is a built-in function
#example:-
a,b=10,'hello'
print(id(a),id(b))

#there are two types of datatypes i.e.  
# 1.single valued datatype/individual datatypes    2.multi valued datatype/collection datatypes


#Single valued datatype:- it can store only one value
#there are 4 types of single valued datatype, mentioned below:-

#(i) integer
#standard representaion = int()
#default value = 0
a = 1
b = -1
print(a,b)
print(type(a),type(b))
print(id(a),id(b))

#(ii) float
#standard representaion = float
#default value = 0.0
p = 10.1
q = -10.1
print(p,q)
print(type(p),type(q))
print(id(p),id(q))

#(iii) complex
#standard representaion = complex
#default value = 0j
s = 10+20j
print(s)
print(10+20j)
print(type(s))
print(id(s))

#(iv) boolean
#standard representaion = bool
#default value = false
a =10
b = 20
print(a>b)
print(a<b)
print(True+False)
print(True*False)


#Single valued datatype:- it can store multiple value
#there are 5 types of single valued datatype, mentioned below:-
#1. string
#2. tuple
#3. list
#4. set
#5. dictionary


#----------string----------
#string is a collection/set of charecters enclosed between single,douple or tripal quotes
# example:-
a='hello'
b="hello"
c='''hello'''
#the tripal quote is also used as   1.documents string    2.multiline of values    3.comment lines

#------some string methods------

#1. len()
a='hello'
print(len(a))

#2. dir()
a='hello'
print(dir(a))

#3. upper()
a="hello"
print(a.upper())

#4. lower()
a='HELLO'
print(a.lower())

#5. capitalise()
a='hello world'
print(a.capitalize())

#6. title()
a='hello world'
print(a.title())

#7. swapcase()
a='Hello World'
print(a.swapcase())

#8. is upper()
a='HELLO'
b='hello'
print(a.isupper(),b.isupper())

#9. islower
a='HELLO'
b='hello'
print(a.isupper(),b.isupper())

#10. isalpha()
a='hello'
b='10'
print(a.isalpha(), b.isalpha())

#11. isdigit()
a='12'
b='hello world'
print(a.isdigit(),b.isdigit())

#12. replace
a='hello worlf'
print(a.replace('f','d'))

#13. count()
a='hello globe'
print(a.count('o'))

#14. startswith()
a='hello'
b='world'
print(a.startswith("h"),b.startswith('h'))

#15. endswith()
a='hello'
b='world'
print(a.endswith("o"),b.endswith('h'))

#16. split()
a='hello guys welocme to the world of python'
print(a.split())

#17. find()
a='hello boss'
print(a.find('o'))

#18. rfind()
s='hello worlds'
print(s.rfind('o'))

#19. 'strip'
a='---hello world---'
print(a.strip('-'))

#20. lstrip()
a='---hello---'
print(a.lstrip('-'))

#21. rstrip()
a='---hello---'
print(a.rstrip('-'))

#22. join()
a='hello hello'
print('-'.join(a))

#indixing in string
''' syntex = var[+/- index_no]'''

#slicing in string
'''syntex = var[start:end:step] '''


#----------tuple----------
#tuple is a collection of homogenous and hetrogenous type of data which are enclosed in paranthisis i.e.( )

#example:-
a=(10,20,30,'Hello',True,40.5)
print(type(a))

#------some tuple methods------

#1. count()
a=(10,10,10,20,20,30,30,'hello',4.5)
print(a.count(10))

#2. index()
a=(10,10,20,20,30,'hello',40)
print(a.index(40))


#----------list----------

#1. 
