# #craeting class and object

# class A3:
#     pass

# obj1=A3()
# obj2=A3()

# print(A3)  #o/p => <class '__main__.A3'>
# print(obj1) 
# print(obj2) 

# class Demo:
#     a,b=10,20

# a1=Demo()
# a2=Demo()

# print(Demo.a)
# print(a1.a)
# print(a2.a)

# #modification
# Demo.a=1000
# a1.a=100
# Demo.a2=200

# print(Demo.a)
# print(a1.a)
# print(a2.a)


#types of states/properties
#1. Generic/static/class Members
#2. Specific/object Members

# class Company:
#     c_name='Antrica'
#     c_address='Nodia'
#     c_contactDetail=9939338373
#     c_mail='antrica23.gmail.com'
#     c_domain='tech'

#     def add_details(obj,id,ename,deptno,salary,comm,job,hiredate):
#         print(id,ename,deptno,salary,comm,job,hiredate)
    
# emp1=Company()
# emp2=Company()
# emp3=Company()
# emp4=Company()
# emp5=Company()

# emp1.id=101
# emp1.ename='Smith'
# emp1.deptno=10
# emp1.salary=6000
# emp1.comm=1000
# emp1.job='Manager'
# emp1.hiredate='01-JAN-90'

# emp1.add_details(101,'Smith',10,6000,1000,'Manager','01-JAN-90')

# emp2.id=102
# emp2.ename='Adams'
# emp2.deptno=20
# emp2.salary=600
# emp2.comm=100
# emp2.job='Salesman'
# emp2.hiredate='01-FEB-95'

# emp3.id=103
# emp3.ename='Blake'
# emp3.deptno=10
# emp3.salary=500
# emp3.comm=10
# emp3.job='Guard'
# emp3.hiredate='01-MAY-90'

# emp4.id=104
# emp4.ename='Devid'
# emp4.deptno=10
# emp4.salary=1000
# emp4.comm=None
# emp4.job='Analyst'
# emp4.hiredate='23-JAN-95'

# emp5.id=105
# emp5.ename='Dejahu'
# emp5.deptno=20
# emp5.salary=1500
# emp5.comm=None
# emp5.job='Analyst'
# emp5.hiredate='01-JULY-97'


# print(emp1.id)
# print(emp1.ename)
# print(emp1.deptno)
# print(emp1.salary)
# print(emp1.comm)
# print(emp1.job)
# print(emp1.hiredate)

# print(emp2.id)
# print(emp2.ename)
# print(emp2.deptno)
# print(emp2.salary)
# print(emp2.comm)
# print(emp2.job)
# print(emp2.hiredate)

# print(emp3.id)
# print(emp3.ename)
# print(emp3.deptno)
# print(emp3.salary)
# print(emp3.comm)
# print(emp3.job)
# print(emp3.hiredate)

# print(emp4.id)
# print(emp4.ename)
# print(emp4.deptno)
# print(emp4.salary)
# print(emp4.comm)
# print(emp4.job)
# print(emp4.hiredate)


# print(emp5.id)
# print(emp5.ename)
# print(emp5.deptno)
# print(emp5.salary)
# print(emp5.comm)
# print(emp5.job)
# print(emp5.hiredate)



# class Mall:
#     m_name='V2'
#     m_address='Padrauna'
#     m_mail='v2padrauna@yahoo.com'
#     m_phno=2842989201
#     m_branch=None

#     def customer(obj,name,gender,phn_no,mail,address):
#         obj.name=name
#         obj.gender=gender
#         obj.phn_no=phn_no
#         obj.mail=mail
#         obj.address=address
    
#     def info(obj):
#         print(obj.name,obj.gender,obj.phn_no,obj.mail,obj.address)



# ob=Mall()
# ob.customer('Shohrat','Male',7878787878,'ssr06@com','Gurugram')
# ob.info()


#Constructor
"""to call method implicitly we use constructor"""

# class Company:
#     c_name='TCS'
#     c_address='Gurugram'
#     C_email='tcs123@yahoo.com'

#     def __init__(self,id,name,age,address):
#         self.id=id
#         self.name=name
#         self.age=age
#         self.address=address
    
#     def display(self):
#         print(self.id,self.name,self.age,self.address)
#     def rename(self,new_address):
#         self.address=new_address

# person1=Company(101,'Rio',24,'Gurugram')
# person2=Company(102,'Vishal',21,'Gurugram')
# person3=Company(103,'Shohrat',23,'Gurugram')
#
# person1.rename('Kolkata')
# person2.rename('Bihar')
# person3.rename('Uttar Pradesh')
#
# person1.display()
# person2.display()
# person3.display()



#abstraction
import abc

class Whatsapp(abc.ABC):
    @abc.abstractmethod
    def chat(self):
        ... 

    @abc.abstractmethod
    def group(self):
        ...

    @abc.abstractmethod
    def call(self):
        ...
    
class Dev1(Whatsapp):
    def chat(self):
        print("chat is loading")
class Dev2(Dev1):
    def group(self):
        print("group is in process")
class Dev3(Dev2):
    def call(self):
        print("call is loaded")

s=Dev3()
print(s.chat(),s.group(),s.call())
