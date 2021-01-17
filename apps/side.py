from flask import Blueprint, jsonify


from apps.model import Article


side = Blueprint("side",__name__)

@side.route("/side")
def getSide():
    article = Article()
    readMent =article.getReadList()
    newPub = article.getNewList()
    popRead = article.getPopList()
    return jsonify(readMent,newPub,popRead)