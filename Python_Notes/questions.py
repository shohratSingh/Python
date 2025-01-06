# s = 'hello world'
# #wap to extract first characters
# print(s[0:3])
# #wap to extract last 3 characters
# print(s[-3:])
# #wap to extract alternative characters
# print(s[0::2])
# #wap to extract reverse a string
# print(s[::-1])
# #wap to extract odd characters
# print(s[::2])
# #wap to extract even characters
# print(s[1::2])
# #wap to extract middle characters
# print(s[5])
# #wap to reverse the first world
# print(s[-6::-1])
# #wap to print alternative characters from reverse
# print(s[-1::-2])
# #wap print odd characters from reverse
# print(s[::-2])
# #wap print even characters from reverse
# print(s[-2::-2])

# print(s.upper())

# data =[10,10.6,'Ruchi',True,[10,20,30]]
# if type(data[-1])==int:
#     print("integer")
# elif type(data[-1])==float:
#     print("Float")
# elif type(data[-1])==complex:
#     print('complex')
# elif type(data[-1])==bool:
#     print('bool')
# else:
#     print("collection")

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter third number: "))

# if a>b and a>c:
#     print("a is gretest")
# elif b>a and b>c:
#     print("b is gretest")
# else:
#     print(" c is greatest")


# char =input("Enter anything: ")

# if 'A'<= char <= 'Z':
#     print(ord(char))
# elif 'b'<= char <= 'z':
#     print(ord(char)-32)
# elif '0' <= char <= '9':
#     print(int(char)**2)
# else:
#     print(char)



# num=int(input("enter any numbr: "))
 
# if num % 3 == 0 and num % 5 == 0: 
#     print("FizzBuzz") 
# elif num % 3 == 0: 
#     print("Fizz") 
# elif num % 5 == 0: 
#     print("Buzz") 
# else: 
#     print(num)


# data=[10,5,50,3+3j,'hello']
# index=len(data)//2
# if type(data[index]) == int: 
#     print("digit")
# else:
#     print("not digit")


# num=int(input("enter any number: "))
# if -9<=num<=9:
#     print("single digit")
# elif -99<=num<=99:
#     print("double digit")
# elif -999<=num<=999:
#     print("tripal digit")
# else:
#     print("more then three digit")



# a=int(input("enter first number: "))
# b=int(input("enter second input: "))

# if a==b:
#     print("both the numbers are equal")
# elif a>b:
#     print(" first number is greater then second number")
# else:
#     print("first number is smaller then second number")



# a=int(input("Enter any digit: "))
# if len(str(a))==1:
#     print("one digit")
# elif len(str(a))==2:
#     print("double digits")
# elif len(str(a))==3:
#     print("tripal digits")
# else:
#     print("more then three digit")



# data=[10,10.5,True,'apple']

# # data = input("enter anything: ")

# if type(data[-1])==str:
#     if data[-1].isalpha():
#         last_char = data[-1][-1]
#         if last_char in ['a','e','i','o','u','A','E','I','O','U']:
#             print(ord(last_char))
#         else:
#             print("it is not vowel")
#     else:
#         print("it is not alphabet")
# else:
#     print("it is not string")


# data=[5,'Hi',10.5,'Hello']

# if len(data)%2==0:
#     if type(data[0])==int:
#         if (data[0])%2==1:
#             print(data[0]**2)
#         else:
#             print("it is not odd")
#     else:
#         print("it is not integer")
# else:
#     print("length of data is not even")


# data=(input("enter any alphabet: "))

# if type(data)==str:
#     if ord(data)%2==0:
#         print(ord(data)**2)
#     else:
#         print("ASCII code of input is not even")
# else:
#     print("input is not in alphabet")