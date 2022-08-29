import pymysql


# def Returnshu():
#     return 1,2,3
mydb=pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='schema1',
    port=3306
)
mycursor=mydb.cursor()

sql1='select * from table1'
mycursor.execute(sql1)

myresult=mycursor.fetchall()
for i in myresult:
    print(i)
mydb.commit()
with open("1.png",'rb') as file:
    erjinzhi=file.read()
# b=(3,"tomp",erjinzhi)
# sql2='update table1 set img=%s where id =3'
# mycursor.execute(sql2,erjinzhi)
sql3='insert into table1 (id,name,img) values(5,"tom",%s)'
mycursor.execute(sql3,erjinzhi)
# a,b,c= myresult[0]
# a,b,c=Returnshu()
# print(a,b,c)
# fout=open("img.png",'wb')  #创建一个图片载体
# fout.write(myresult[2][2]) #二进制图片数据写入图片文件
# print(myresult[0][0])
print("------------------------")
mycursor.execute(sql1)

myresult=mycursor.fetchall()
for i in myresult:
    print(i)
mydb.commit()
mydb.commit()