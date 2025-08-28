import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0001",
    database="spidyPython",
    port=3306)

cursor = conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS student (
#                id INT PRIMARY KEY,
#                sname VARCHAR(20),
#                phn_no BIGINT CHECK (phn_no > 0 AND LENGTH(phn_no) = 10),
#                email VARCHAR(50),
#                address VARCHAR(100)
#                )""")

# def details():
#     id = int(input("Enter id: "))
#     sname = input("Enter name: ").strip()
#     phn_no = int(input("Enter phone number: "))
#     email = input("Enter email: ").strip()
#     address = input("Enter address: ").strip()
#     cursor.execute(f"insert into student values({id}, '{sname}',{phn_no}, '{email}', '{address}' )")
#     conn.commit()
#     print("Your data is inserted Sucessfully!")

# n = int(input("Enter number of data you want to insert: "))
# for i in range(n):
#     details()

# cursor.execute("delete from student where id = 1")
# conn.commit()

# cursor.execute("insert into student(id, address) values (103,'Gurugram')")
# conn.commit()


cursor.execute("update student set address = 'Delhi' where id = 104 ")
conn.commit()


    
