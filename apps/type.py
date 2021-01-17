from flask import Blueprint, render_template


from apps.model import Article


type = Blueprint("type",__name__)


@type.route("/type/<int:type>-<int:page>",methods=["GET"])
def getSide(type,page):
    article = Article()
    articleData = article.getSideArticle(type,page)
    pageNumber = article.getTypeNumber(type)
    currentPageNumber = page
    return render_template("type.html",articles=articleData,pageNumber=pageNumber,currentPage=currentPageNumber,type=type)




