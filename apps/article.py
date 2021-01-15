from flask import Blueprint, render_template


from apps.model import Article


article = Blueprint("article",__name__)


@article.route("/article/<id>",methods=["GET"])
def getArticle(id):
    article = Article()
    articleData = article.getOneArticle(id)
    return render_template("article.html",article=articleData)




