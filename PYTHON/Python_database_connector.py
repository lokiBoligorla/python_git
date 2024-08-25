# import mysql.connector
# mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="demo")
# mycursor=mydb.cursor()
# sql="insert into stu (id,name,price,total,total2)values(%d,%s,%d,%d,%d)"
# val=(1012,"loki",90,76,34)
# mycursor.execute(sql,val)

# mycursor.execute("select * from stu")
# result=mycursor.fetchall()
# for i in result:
#     print(i)






import mysql.connector
md=mysql.connector.connect(host="localhost",user="root",password="1234",database="data")
mycursor=md.cursor()
# mycursor.execute("show databases") #Show all databases in the system
# for i in mycursor:
#     print(i)

# mycursor.execute("show tables") #Show the all the tables in the databases
# for i in mycursor:
#     print(i)

# mycursor.execute("select * from demo") # It will show the all data in table
# for i in mycursor:
#     print(i)

# mycursor.execute("create table new_table(id int(10),name varchar(20))") # This will create the new table in the database 
# mycursor.execute("show tables")
# for i in mycursor:
#     print(i)

sql="insert into demo(SNO,Name,Profession,Experience))VALUES(%d,%s,%s,%s)"
values=("1","joy","coder","tester")
mycursor.execute(sql,values)
md.commit()