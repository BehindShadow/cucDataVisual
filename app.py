from flask import Flask,jsonify,render_template
import json
from datetime import timedelta
import pymysql

# 实例化产生一个Flask对象
# 自动重载模板文件
app = Flask(__name__)

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
# 设置静态文件缓存过期时间
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

#flask的路由是基于装饰器的
@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/d3art0')
def d3art0():
    return render_template('d3art0.html')

@app.route('/d3art1')
def d3art1():
    return render_template('d3art1.html')

@app.route('/d3art2')
def d3art2():
    return render_template('d3art2.html')

@app.route('/d3art3')
def d3art3():
    return render_template('d3art3.html')
    
@app.route('/d3art4')
def d3art4():
    return render_template('d3art4.html')

@app.route('/d3art5')
def d3art5():
    return render_template('d3art5.html')


@app.route('/d3art6')
def d3art6():
    dbhost = "localhost"
    dbuser = "root"
    dbpass = "G884414g#_" # 修改
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
        # ans = ""
        # for i in results:
        #     ans +="<p>"+str(i[1])+str(i[2])+str(i[3])+"</p>"
        #     print("<p>"+str(i[1])+str(i[2])+str(i[3])+"</p>")
        # return """<html ><head>
   	    # <meta charset = 'utf-8'>
        # </head>
        # <body >""" +ans +"""</body></html>"""
        seq = []
        for i in results:
            temp = str(i[1])+str(i[2])+str(i[3])
            seq.append(temp)
            # print(temp)
        return render_template('d3art6.html',seq=seq)
    except:
        print ("Error: unable to fetch data")
    
    db.close()
    return "hello"
# # 关闭数据库连接
    

if __name__ == '__main__':
    app.run()      