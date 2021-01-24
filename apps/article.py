from flask import Blueprint, render_template, jsonify, session

from apps.model import Article, Favorite, Comment

article = Blueprint("article",__name__)


@article.route("/article/<id>",methods=["GET"])
def getArticle(id):
    article = Article()
    articleData = article.getOneArticle(id)
    comList = Comment().getCommentsList(id,1,10)
    articleStatu = Favorite().getStatu(session.get("userid"),id)
    return render_template("article.html",article=articleData,statu = articleStatu,comments=comList)


@article.route("/content/<id>",methods=["GET"])
def getContent(id):
    article = Article()
    flag = article.isBuy(id)
    if flag:
        result ={"code":10001,"data": article.getAllContent(id),"flag":flag}
        return jsonify(result)
    else:
        result = {"code":10001,"data": article.getHalfContent(id), "flag": flag}
        return jsonify(result)

@article.route("/articlebuy/<id>",methods=["GET"])
def buyArticle(id):
    if not session.get("username"):
        result = {"code": 10004, "msg": "please login!"}
        return jsonify(result)
    else:
        article = Article()
        result = article.buyArticle(session.get("username"),id)
        return jsonify(result)
