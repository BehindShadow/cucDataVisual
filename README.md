# cucDbVis

## Brief instruction of deploying Mysql over Web server

### The environment

if you try to achieve this project, you should have  
- Ubuntu 20.04 
- Mysql-server
- python3.8 
- flask
- PyMysql
- vscode 
- you can get it easily by using the following commands
```
apt-get update
apt install Mysql-server
apt install python
pip install PyMsql 
pip install flask
```
**You will need to remember your root password when installing mysql**

### Steps

#### 1. create the database and table

open the termianl and type the command:
```
mysql -u root -p
```

and type the root password
then using the following command to create a database 
```sql
CREATE DATABASE dict
```
and then, open your vscode, **it is strong recommand you use the plug

- MySQL
- MySQL Syntax

You can add connection in resource manager, like this:
![1](./img/1.png)

type :localhost, username, password


and **Add query**
![2](./img/1.png)


Copy the contents of the SQL code file given by the teacher into this file

Right click on the **run MySQL Query**
and the you create the database successfully

#### 2. Writing Python Code

The core code in app.py
```py
@app.route('/dbfirst')
def dbfirst():
    dbhost = "localhost"
    dbuser = "root"
    dbpass = "**********"# 密码要写自己的这里就不展示了
    dbname = "dict"
    db=pymysql.connect(host=dbhost,user=dbuser,password=dbpass,database=dbname)
    sql = "SELECT * FROM `dict`.`map_enword` LIMIT 100;"
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        # print(results)
        ans = ""
        for i in results:
            ans +="<p>"+str(i[1])+str(i[2])+str(i[3])+"</p>"
            print("<p>"+str(i[1])+str(i[2])+str(i[3])+"</p>")
        return """<html ><head>
   	    <meta charset = 'utf-8'>
        </head>
        <body >""" +ans +"""</body></html>"""

    except:
        print ("Error: unable to fetch data")
    
    db.close()
    return "hello"
# # 关闭数据库连接
```

### 
#### 1. Svae the project

you can save the project to local by using **git clone**
#### 2. Run
cd to the corresponding folder
using this command
``` 
python ./app.py
```

#### 3. Open your Web browser

Enter 127.0.0.1:5000/dbfirst in the address box

You can see this in your browser window
![3](./img/1.png)  


