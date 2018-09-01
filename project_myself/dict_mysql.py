import pymysql 
import re  

f = open('dict.txt')
db = pymysql.connect\
('localhost','root','123456','dict',charset="utf8")
cursor = db.cursor()

for line in f:
    l = line.split()
    # print(l)
    # l = re.split('[ ]+',line)
    word = l[0]
    interpret = ' '.join(l[1:])
    # print(word,interpret)
    sql = "insert into words (word,interpret) \
    values ('%s','%s');"%(word,interpret) 
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback() # 回滚:就是数据库里做修改后（update ,insert , delete）未commit之前使用rollback 可以恢复数据到修改之前

cursor.close()
db.close()       
f.close()








