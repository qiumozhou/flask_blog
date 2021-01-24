
from flask import Blueprint, request, session, jsonify

from apps.model import Article, User, Credit, Favorite
from common.code import Code
from common.mail import Mail


favorite = Blueprint("favorite",__name__)


@favorite.route("/favorite/<int:id>",methods=["GET","POST"])
def setFavorite(id):
    if request.method == "POST":
        userid = session.get("userid")
        if not userid:
            result = {"code": 10004, "msg": "ok"}
            return jsonify(result)
        articleid = id
        fa = Favorite().resetCollect(userid,articleid)
        result = {"code": 10001, "data": fa, "msg": "ok"}
        return jsonify(result)

    if request.method == "GET":
        userid = request.form.get("userId")
        articleid = request.form.get("articleId")
        fa = Favorite.getCollect(userid, articleid)
        result = {"code": 10001, "data": fa, "msg": "ok"}
        return jsonify(result)
