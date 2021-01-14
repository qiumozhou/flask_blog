from flask import Blueprint, render_template

from apps.db import dbsession
from apps.model import Article


article = Blueprint("article",__name__)


@article.route("/article/<id>",methods=["GET"])
def getArticle(id):
    row = dbsession.query(Article).filter(Article.id==id).first()
    return render_template("article.html",article=row)

