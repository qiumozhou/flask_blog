import datetime
import os

from flask import Flask, render_template, request, session

from apps.article import article
from apps.login import login
from apps.filters import filters
from apps.model import Article
from apps.page import page
from apps.register import register
from apps.search import search
from apps.side import side
from apps.type import type

app = Flask(__name__,static_folder="static",template_folder="template",static_url_path='/')

app.config["SECRET_KEY"] = os.urandom(24)
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(minutes=5)

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



@app.before_request
def before_request():
    username = request.cookies.get("username")
    if username:
        session['username'] = username


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
    app.register_blueprint(register)
    app.register_blueprint(login)
    app.run(debug=True)