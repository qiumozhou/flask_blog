from flask import Flask, render_template
# from flask.ext.sqlalchemy import SQLAlchemy
# from apps import article
from apps.article import article
from apps.db import dbsession
from apps.model import Article

app = Flask(__name__,static_folder="static",template_folder="template",static_url_path='/')

# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://jianshu:jianshu@127.0.0.1:3306/jianshu'
# #设置这一项是每次请求结束后都会自动提交数据库中的变动
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
# #实例化
# db = SQLAlchemy(app)

@app.route('/')
def index():
    row = dbsession.query(Article)[0:5]
    return render_template("index.html", artiles=row)

# @app.route('/article')
# def article():
#     return render_template("article.html")

if __name__ == "__main__":

    app.register_blueprint(article)
    app.run(debug=True)