# #some questions using for loop

# #q1
# for i in range(0,11):
#     print(i)

# #q2
# for i in range(1,11):
#     print(i)


# #q3
# for i in range (0,20):
#     if i%2==0:
#         print(i)

# #q4
# for i in range(0,20):
#     if i%2==1:
#         print(i)

# #q5
# s='hello'
# for i in range(len(s)):
#     print(i,s[i])

# #q6
# for i in range(20,0,-1):
#     print(i)

# #q7
# l=['apple','banana','orange','pine','grapes']
# for i in l:
#     if i[0] in 'aeiouAEIOU':
#         print(i[::-1])
#     else:
#         print(i)

# #q8
# t=(10,20,'hello',True,'world',(10,20,30))
# for i in t:
#     if type(i) in (int,bool,float,complex):
#         print(i)

# q9


# # q10
# s = 'hello'
# count = 0
# for i in s:
#     count += 1
# print(count)

# #q11
# l=[10,10,20,20,30,'hello']
# l2=[]
# for i in l:
#     if i not in l2:
#         l2+=[i]
# print(l2)

# #q12
# l=['hello','ten']
# d={}
# for i in l:
#     d[i]=len(i)
# print(d)

# #q13
# s='hello'
# s2={}
# for i in s:
#     if i in s2:
#         s2[i]+=1
#     else:
#         s2[i]=1
# print(s2)

# #q14
# l=['hello','guy','hey']
# l2=[]
# for i in l:
#     l2+=i[-1]
# print(l2)

# #q15
# s='apple hello'
# s2=''
# for i in s.split():
#     if i[0] in 'aeiouAEIOU':
#         s2+=i[::2]
#     else:
#         s2+=i[-1::-1]
# print(s2)

# #q16
# s='hello world welcome to python programming language'
# d={}
# for i in s.split():
#     if i[-1] in 'aeiouAEIOU':
#         d[i]=len(i)
# print(d)

# #q17
# l=['welcome','python','java','programming','spring','django']
# d={}
# for i in l:
#     if len(i)>=5:
#         d[i]=len(i)
# print(d)

# #q18
# l=['joi.com','fb.py','qspy.in']
# l2=[]
# for i in l:
#     extension=i.split(".")[-1]
#     l2.append(extension)
# print(l2)


# #q19
# l=[10,20,30,40,50]
# for i in l:
#     print(i,end=' ')

# #q20
# l='just looking like a wow'
# l2=''
# for i in l.split():
#     if len(i)%2==0:
#         l2+=i[-1].upper()
#     else:
#         l2+=i.upper()
# print(l2,end=' ')


# l = 'just looking like a wow'
# words = l.split()
# result = []
# for word in words:
#     length = 0
#     for char in word:  # Count the number of characters
#         length += 1
#     if length % 2 == 0:  # Even number of characters
#         transformed_word = ''
#         for i in range(length):
#             if i == length - 1:  # Check for the last character
#                 transformed_word += chr(ord(word[i]) - 32)  # Convert to uppercase
#             else:
#                 transformed_word += word[i]
#         result.append(transformed_word)
#     else:  # Odd number of characters
#         transformed_word = ''
#         for char in word:
#             if 'a' <= char <= 'z':  # Only convert lowercase letters
#                 transformed_word += chr(ord(char) - 32)
#             else:
#                 transformed_word += char
#         result.append(transformed_word)

# # Join the transformed words back into a string
# output = ' '.join(result)
# print(output)


# same questions using while loop

# #q1
# i=0
# while i<=10:
#     print(i)
#     i+=1

# #q2
# i=1
# while i<=10:
#     print(i)
#     i+=1

# #q3
# i=0
# while i<20:
#     if i%2==0:
#         print(i)
#     i+=1

# #q4
# i=1
# while i<20:
#     if i%2==1:
#         print(i)
#     i+=1

# #q5
# s='hello'
# index=0
# while index<len(s):
#     print(index,s[index])
#     index+=1

# #q6
# i=20
# while i>-1:
#     print(i)
#     i-=1

# #q7
# l=['apple','banana','ornage','pine','grapes']
# i=0
# while i<len(l):
#     word=l[i]
#     if word[0] in 'aeiouAEIOU':
#         print(word[::-1])
#     else:
#         print(word)
#     i+=1

# # q8
# t = (10, 20, 'hello', True, 'world', (10, 20, 30))
# i = 0
# while i<len(t):
#     word = t[i]
#     if type(word) in (float, bool, complex, int):
#         print(word)
#     i+=1

#q9


# #q10
# s='string'
# count=0
# i=0
# while i<len(s):
#     count+=1
#     i+=1
# print(count)

# #q11
# l=[10,10,20,20,'hello',10,40,50]
# l2=[]
# i=0
# while i<len(l):
#     j=l[i]
#     if j not in l2:
#         l2.append(j)
#     i+=1
# print(l2)

# #q12
# l=['hello','ten']
# d={}
# i=0
# while i<len(l):
#     j=l[i]
#     d[j]=len(j)
#     i+=1
# print(d)

# #q13
# s='hello'
# s2={}
# i=0
# while i<len(s):
#     if s[i] in s2:
#         s2[s[i]]+=1
#     else:
#         s2[s[i]]=1
#     i+=1
# print(s2)

#q14



