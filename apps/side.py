from flask import Blueprint, render_template


from apps.model import Article


side = Blueprint("side",__name__)


@side.route("/side/<int:type>-<int:page>",methods=["GET"])
def getSide(type,page):
    article = Article()
    articleData = article.getSideArticle(type,page)
    pageNumber = article.getTypeNumber(type)
    currentPageNumber = page
    return render_template("side.html",articles=articleData,pageNumber=pageNumber,currentPage=currentPageNumber,type=type)




