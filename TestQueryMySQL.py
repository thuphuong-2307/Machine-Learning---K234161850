import mysql.connector

server = 'localhost'
port = 3306
database = 'studentmanagement'
username = 'root'
password = 'carot'

conn = mysql.connector.connect(
    host=server,
    port=port,
    database=database,
    user=username,
    password=password
)

"""
# Toan bo sinh vien va sap xep theo tuoi tang dan

# cursor = conn.cursor()
# 
# sql = 'select * from student'
# cursor.execute(sql)
# 
# dataset = cursor.fetchall()
# align = '{0:<3} {1:<6} {2:<15} {3:<10}'
# print(align.format('ID','Code','Name','Age'))
# for item in dataset:
#     id=item[0]
#     code=item[1]
#     name=item[2]
#     age = item [3]
#     avatar=item[4]
#     intro=item[5]
#     print(align.format(id,code,name,age))
# 
# cursor.close()
"""
"""
# Toan bo sinh vien, tuoi tang dan
cursor=conn.cursor()
sql='select * from student ' \
    'order by Age asc'
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID','Code','Name','Age'))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()
"""

# Sinh vien tu 22-26 tuoi, tuoi tang dan
"""
cursor = conn.cursor()
sql = 'select * from student ' \
    'where Age>=22 and Age<=26 ' \
    'order by Age asc'
cursor.execute(sql)

dataset = cursor.fetchall()
align = '{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID','Code','Name','Age'))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()
"""

# Truy van sinh vien khi biet ID
"""
cursor = conn.cursor()
sql = 'select * from student where ID = 1'

cursor.execute(sql)

dataset = cursor.fetchone()
if dataset != None:
    id, code, name, age, avatar, intro=dataset
    print("ID = ",id)
    print("Code = ",code)
    print("Name = ",name)
    print("Age = ",age)
cursor.close()
"""

# Truy van phan trang Student
"""
cursor = conn.cursor()
sql = "select * from student limit 3 offset 0"
# LIMIT: số phần tử muốn truy vấn
# OFFSET: số phần tử bắt dầu truy vấn

cursor.execute(sql)

dataset = cursor.fetchall()
align = '{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID','Code','Name','Age'))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))
cursor.close()
"""


# Truy van phan trang Student
"""
print("PAGING!!!!!")
cursor = conn.cursor()
sql="SELECT count(*) FROM student"
cursor.execute(sql)
dataset=cursor.fetchone()
rowcount=dataset[0]

limit=2
step=1
for offset in range(0,rowcount,step):
    sql=f"SELECT * FROM student LIMIT {limit} OFFSET {offset}"
    cursor.execute(sql)

    dataset=cursor.fetchall()
    align='{0:<3} {1:<6} {2:<15} {3:<10}'
    print(align.format('ID', 'Code','Name',"Age"))
    for item in dataset:
        id=item[0]
        code=item[1]
        name=item[2]
        age=item[3]
        avatar=item[4]
        intro=item[5]
        print(align.format(id,code,name,age))

cursor.close()
"""

# Thêm mới 1 Student
"""
cursor = conn.cursor()
sql='insert into student(code,name,age) values(%s,%s,%s)'
val=("sv07", "Tran Duy Thanh", 45)
cursor.execute(sql,val) #cursor.execute(sql,val) thì chương trình sẽ tự động mapping giá trị trong tuple cho các %s
conn.commit() #xác thực là sẽ lưu mới dữ liệu
print(cursor.rowcount,'read inserted') #có bao nhiêu dòng dữ liệu được thay đổi trong cơ sở dữ liệu.
cursor.close()
"""

# Them moi nhieu Student
"""
cursor = conn.cursor()
sql='insert into student(code,name,age) values (%s,%s,%s)'

val=[
    ("sv08","Tran Quyet Chien",19),
    ("sv09","Ho Thang",22),
    ("sv10","Hoang Ha", 25)]
cursor.executemany(sql,val)
conn.commit()
print(cursor.rowcount,'record inserted')
cursor.close()
"""

# Update ten sv code sv09 thanh Hoang Lao Ha
"""
cursor = conn.cursor()
sql="update student set name ='Hoang Lao Ta' where Code='sv09'"
cursor.execute(sql)
conn.commit()
print(cursor.rowcount,'record(s) affected')
"""

# Xoa Student cos ID=11
"""
cursor=conn.cursor()
sql=('delete from student where ID =11')
cursor.execute(sql)
conn.commit()
print(cursor.rowcount,'record(s) affected')
"""

# Xoa Student co ID = 1
"""
cursor=conn.cursor()
sql='delete from student where ID =%s'
val=(1,)
cursor.execute(sql,val)
conn.commit()
print(cursor.rowcount,'record(s) affected')
"""


