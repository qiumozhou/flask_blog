from flask import Blueprint, render_template


from apps.model import Article


page = Blueprint("page",__name__)


@page.route("/page/<int:number>",methods=["GET"])
def getPage(number):
    article = Article()
    articleData = article.getPageArticle(10*number-10,10*number)
    pageNumber = article.getPageNumber()
    currentPageNumber = number
    return render_template("page.html",articles=articleData,pageNumber=pageNumber,currentPage=currentPageNumber)




