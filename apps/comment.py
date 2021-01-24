
from flask import Blueprint, request, session, jsonify

from apps.model import Article, User, Credit, Favorite, Comment
from common.code import Code
from common.mail import Mail


comment = Blueprint("comment",__name__)

@comment.route('/comment',methods=['POST'])
def addComment():
    userid = session.get("userid")
    articleid = request.form.get("articleId")
    content = request.form.get("content")
    replyid = request.form.get("replyId",None)
    Comment().addComment(userid, articleid, replyid, content)
    result = {"code": 10001,"msg": "ok"}
    return jsonify(result)