# d={'a':1,'b':2,'c':3,'d':4,'e':5}

#  for i in d:
#      print(i)

#  for i in d.items():
#      print(i)

#  for i in d.keys():
#      print(i)

#  for i in d.items():
#      print(i[1])

#  for i in d.items():
#      print(i[0])

#  for i in d.items():
#      print(i[0],i[1])


#  l=[10,10,20,20,30,40,50]
#  out=[]
#  for i in l:
#      if i not in out:
#          out.append(i)

#  print(out)

#  #Q1
#  for i in range(10):
#      print(i)

#  #Q2
#  for i in range(1,11):
#      print(i)

#  #Q3
#  for i in range(20):
#      if i%2==0:
#          print(i)

#  #Q4
#  for i in range(20):
#      if i%2==1:
#          print(i)

#  #Q5
#  s='hello'
#  for i in range(len(s)):
#      print(f"index number of {s[i]} is {i}")

#  #Q6
#  for i in range(20,-1,-1):
#      print(i)

#  Q7
#  l=['apple','banana','orange','pine','grapes']
#  for i in range(len(l)):
#      if l[i][0] in 'aeiouAEIOU':
#          print(l[i][::-1])
#      else:
#          print(l[i])

#  Q8
#  t=(10,20,'hello',True,'world',(10,20,30))
#  for i in range(len(t)):
#      if type(t[i]) in (int,float, bool,complex):
#          print(t[i])

#  Q9
#  # string
#  a='hello'
#  out=''
#  for i in range(len(a)):
#      out=a[i]+out
#  print(out)

#  list
#  l=[10,20,'hi',40]
#  l2=[]
#  for i in l:
#      l2=[i]+l2
#  print(l2)

#  tuple
#  t=(10,20,30,'hello',40)
#  t2=()
#  for i in t:
#      t2=(i,)+t2
#  print(t2)

#  dictionary
#  d={'a':1,'b':2,'c':3}


#  Q10
#  s='hello'
#  count=0
#  for i in s:
#      count+=1
#  print(count)


#  Q11
#  l=[10,10,20,20,30,30,'hello',40,50]
#  l2=[]
#  for i in l:
#      if i not in l2:
#          l2=l2+[i]
#  print(l2)

#  Q12

#  #-----intermediate termination in loop-----

#  for i in range(1,11):
#      if i==5:
#          print("okok")
#          break
#      else:
#          print(i)

#  for i in range(1,6):
#      if i==3:
#          continue
#      else:
#          print(i)


#  choice=int(input())
#  if choice==1:
#      pass
#  elif choice==2:
#      pass
#  else:
#      print("invalid")


#  for i in range(1,4):
#      for j in range(1,4):
#          print(i,j)


#  s='hai hello priya'
#  d={}
#  a=s.split()
#  for i in a:
#  count=0
#  for j in i:
#  if j in 'aeiouAEIOU':
#  count+=1
#  d[i]=count
#  print(d)


#  s='Python is very easy'
#  d={}
#  for i in s.split():
#      count=0
#  for j in i:
#      if j in 'aeiouAEIOU':
#          count+=1
#  d[i]=[i,count,i[::-1]]
#  print(d)

#  s = 'aaaabbbacccbca'
#  t = ''
#  for i in s:
#     count = 0
#     if i not in t:
#         for j in s:
#             if i == j:
#                 count += 1
#         t += i+str(count)
#  print(t)

#  s = "aaaabbbacccbca"
#  t = ""
#  for i in s:
#      if i not in t:
#          count = s.count(i)
#          t += i + str(count)

#  print(t)


#  for i in range(1,6):
#     for j in range(1,6):
#         if i==j:
#             print("$", end=' ')
#         else:
#             print(' ',end=" ")
#     print()


#  for i in range(1,6):
#     for j in range(1,6):
#         if i+j==6:
#             print("$", end=' ')
#         else:
#             print(' ',end=" ")
#     print()


#  for i in range(1,6):
#     for j in range(1,6):
#         if i==j or i+j==6:
#             print("$", end=' ')
#         else:
#             print(' ',end=" ")
#     print()


#  for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or j==3:
#             print("$", end=' ')
#         else:
#             print(' ',end=" ")
#     print()


#  for i in range(1,6):
#     for j in range(1,6):
#         if i==5 or j==1:
#             print("$", end=' ')
#         else:
#             print(' ',end=" ")
#     print()


#  for i in range(1,6):
#     for j in range(1,6):
#         if i==5 or j==5:
#             print("$", end=' ')
#         else:
#             print(' ',end=" ")
#     print()

#  for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or j==1:
#             print("$", end=' ')
#         else:
#             print(' ',end=" ")
#     print()

#  for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or j==5:
#             print("$", end=' ')
#         else:
#             print(' ',end=" ")
#     print()


#  for i in range(1,6):
#     for j in range(1,6):
#         if (i==1 or j==5) or (i==5 or j==1):
#             print("$", end=' ')
#         else:
#             print(' ',end=" ")
#     print()


#  for i in range(1,6):
#      for j in range(1,6):
#          if j<=i:
#              print('$',end=' ')
#      print()

#  for i in range(1,6):
#      for j in range(1,6):
#          if j>=i:
#              print('$',end=' ')
#      print()

#  for i in range(1,6):
#      for j in range(5,0,-1):
#          if i>=j:
#              print('$',end=' ')
#          else:
#              print(' ',end=' ')
#      print()

#  for i in range(5,0,-1):
#      for j in range(5,0,-1):
#          if i>=j:
#              print('$',end=' ')
#          else:
#              print(' ',end=' ')
#      print()


#  for i in range(15,0,-1):
#      for j in range(15,0,-1):
#          if i>=j:
#              print('s',end=' ')

#      print()


#  -----------while loop-----------------

#  i=5
#  while i>=1:
#      print(i)
#      i-=1

#  i=1
#  while i<=5:
#      print(i)
#      i+=1

#  s='python'
#  i=0
#  while i<len(s):
#      print(s[i])
#      i+=1


#  start = int(input("Enter number: "))
#  i = 0
#  while i < 10:
#     print(start + i)
#     i += 1


#  s=int(input("enter number:" ))
#  i=1
#  while i<=s:
#     print(i)
#     i+=2

#  s=int(input("enter number: "))
#  i=0
#  while i<=s:
#  print(i)
#  i+=2

#  i=1
#  while i<30:
#     if i%3==0:
#         print(i)
#     i+=1

#  s=(input("enter any word: " ))
#  i=0
#  while i<len(s):
#      if i%2==0:
#          print(s[i])
#      i+=1

#  s = 'kabab is love'
#  d = {}
#  for i in s.split():
#      count = 0
#      nonVowel = ' '
#      for j in i:
#          if j in 'aeiouAEIOU':
#              count += 1
#          else:
#              nonVowel+=j
#      d[i] = [i[::-1], count,nonVowel]
#  print(d)

#  l=[100,200,35,40,60]
#  l2=[]
#  for i in l:
#          l2.append(sum(l)-i)
#  print(l2)
 

#  s={10:'star',20:'bye',30:'moon',40:'apple'}
#  d={}
#  for i in s.items():
#      a=' '
#      for j in i[1]:
#          if j in 'aeiouAEIOU':
#              a+=j
#      d[i[0]]=a
#  print(d) 

# s='kabab is love'
# d={}
# for i in s.split():
#      a=' '
#      count=0
#      for j in i:
#          if j not in 'aeiouAEIOU':
#              a+=j
#              count+=1
# key={a[0]+a[-1]}
# d[key]=(a,count,a[::-1])
# print(d)

# s = 'kabab is love'
# d = {}
# for i in s.split():
#     a = ''
#     count = 0
#     for j in i:
#         if j not in 'aeiouAEIOU':
#             a += j
#             count += 1
#     key = str(i[0])+str(i[-1])
#     if key not in d:
#         d[key] = (a, count, a[::-1])
# print(d)                                                                                                                  

# data=[10,True,'100',700,800,'mango',[10,20,30]]
# data2=[]
# for i in data:
#     if type(i) in (str,tuple,list,set,dict):
#         data2.append(len(i))
#     else:
#         data2.append("1")
# print(data2)



