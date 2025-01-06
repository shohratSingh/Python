#in python print is used as output statement which is used to display the output
#print accept 3 argumnents i.e. print(veriable/valus,seperator='',end='') and seperator and end is optional to pass and veriable/value is mandatory

#examples:-
a = 10
b = 20
c = 30

#this will print in 3 diffrent lines one by one 
print(a)
print(b)
print(c)

#this will print in one line including space between them
print(a,b,c)

print(a)

#here space will be replaced as @ and output will be in same line
print(a,b,c, sep="!")

#here from a to vale c will be printed without any space and in same line because value of end is empty here s cursor will remail in the same line
print(a,end='')
print(b,end='')
print(c)

#vale of a will be printed
print(a)

#here a empty line will be printed
print() 

#here there is a @ between value of a and b and in the next line value of c will be printed includeing n alphabet
print(a,b,sep='@')
print(c,end='n')
