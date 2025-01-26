#q1
age=int(input("enter age to know group: "))
if age<13:
    print('child')
elif 13<age<19:
    print('teenager')
elif 20<age<59:
    print('adult')
else:
    print('senior')


#q2
day=input('enter day: ').lower().split()
age=int(input('enter age: '))
if day=='wednesday':
    if age>18:
        print('$10')
    else:
        print('$6')
else:
    if age>18:
        print('$12')
    else:
        print('$8')

#alternative
day=input('enter day: ').lower().split()
age=int(input('enter age: '))
if day == 'wednesday':
    price = '$10' if age>18 else '$6'
else:
    price = '$12' if age>18 else '$8'
print(price)

#q3
marks=int(input("enter number got: "))
if marks>100:
    print("Please verify you marks")
    exit()
if marks>=90:
    grade='A'
elif marks>=80:
    grade='B'
elif marks>=70:
    grade='C'
elif marks>=60:
    grade='D'
else:
    grade='E'
print('Grade:',grade)

#alternative
marks = int(input("Enter marks obtained: "))
if marks > 100:
    print("Please verify your marks.")
else:
    grade = (
        'A' if marks >= 90 else
        'B' if marks >= 80 else
        'C' if marks >= 70 else
        'D' if marks >= 60 else
        'E'
    )
    print('Grade:', grade)

#q4
color=input("enter color of fruit i.e. green,yellow or brown: ")
condition=(
    'unripe' if color=='green' else
    'ripe' if color=='yellow' else 'overripe'
)
print(condition)

#q5
weather=input("provide the condition of the weather: ").lower()
activity =(
    'go for a walk' if weather=='sunny' else
    'read a book' if weather=='rainy' else
    'build a snowman' if weather=='snowy' else 'provide valid input'
)
print(activity)

#q6
distance=int(input('enter distance: '))
mode_of_transport=(
    ' walk' if distance<3 else
    'bike' if 3<=distance<15 else
    'car' if distance>15 else 'provide valid input'
)
print(mode_of_transport)

#q7
size=input('enter coffe size: ')
extra=input('want extra or not(y/n): ')
coffee=(
    (size + ' with extra') if extra=='y' else size 
)
print(coffee)

#8
password=input('enter password: ')
strength=(
    'week' if len(password)<6 else
    'medium' if 6<=len(password)<10 else 'strong'
)
print(strength)


#q9
year=int(input('enter year to check: '))
leap_year=(
    'yes' if (year%4==0 and year%100!=0) or (year%400==0 ) else 'no' 
)
print(leap_year)

# #q10
pet = input('Select pet (cat/dog): ').strip().lower()
if pet not in ['cat', 'dog']:
    print("Invalid pet selected. Please choose either 'cat' or 'dog'.")
    exit()
age = int(input('Enter age: '))
food = (
        'puppy food' if pet == 'dog' and age <= 2 else
        'normal dog food' if pet == 'dog' and age > 2 else
        'senior cat food' if pet == 'cat' and age > 5 else
        'junior cat food'
    )
print(food)