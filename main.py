from flask import Flask, render_template

from apps.article import article
from apps.filters import filters
from apps.model import Article
from apps.page import page
from apps.search import search
from apps.side import side
from apps.type import type

app = Flask(__name__,static_folder="static",template_folder="template",static_url_path='/')

# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://jianshu:jianshu@127.0.0.1:3306/jianshu'
# #设置这一项是每次请求结束后都会自动提交数据库中的变动
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
# #实例化
# db = SQLAlchemy(app)


@app.context_processor
def getType():
    type = {
        1:"math",
        2: "chinese",
        3: "english",
        4: "life",
        5: "sports",
        6: "earth",
    }
    return dict(articleType=type)


@app.route('/')
def index():
    article = Article()
    articleList = article.getPageArticle(0,10)
    pageNumber = article.getPageNumber()
    return render_template("index.html", articles=articleList,pageNumber=pageNumber)



if __name__ == "__main__":

    app.register_blueprint(article)
    app.register_blueprint(filters)
    app.register_blueprint(page)
    app.register_blueprint(type)
    app.register_blueprint(search)
    app.register_blueprint(side)

    app.run(debug=True)