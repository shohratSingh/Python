import sqlite3
conn = sqlite3.connect('a3.db')
cursor = conn.cursor()

#Syntex
#cursor.execute(query)
# cursor.execute('create table student(id number(3) primary key ,name varchar(20),phn_no number(10) check(phn_no>0 and length(phn_no=10)))')
# cursor.execute("insert into student values(101,'Shohrat',9876543210)")
# cursor.execute("insert into student values(102,'Shatadru',01876543210)")
# cursor.execute("insert into student values(103,'Vishal',3445443210)")
# cursor.execute("insert into student values(104,'Smith',9826543210)")
# cursor.execute("insert into student values(105,'Allen',5674383210)")
# cursor.execute("delete from student where id = 107")
# conn.commit()

# #taking multiple data from user
# def details():
#     id=int(input("Enter id: "))
#     name=input("Enter name: ")
#     phn_no=int(input("Enter phone number: " ))
#     cursor.execute(f"insert into student values({id},'{name}',{phn_no})")
#     conn.commit()
#     print("Data is inseted Sucessfully!")

# for i in range(1,3):
#     details()




