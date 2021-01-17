from flask import Blueprint, render_template


from apps.model import Article


search = Blueprint("search",__name__)

@search.route("/search/<keyword>-<int:page>",methods=["GET"])
def getSearch(keyword,page):
    article = Article()
    articleData = article.getSearchArticle(keyword,page)
    pageNumber = article.getSearchNumber(keyword)
    currentPageNumber = page
    return render_template("search.html",articles=articleData,pageNumber=pageNumber,currentPage=currentPageNumber,keyword=keyword)