

from flask import Blueprint, request, session, jsonify

from apps.model import Article, User, Credit
from common.code import Code
from common.mail import Mail


register = Blueprint("register",__name__)
@register.route('/register',methods=["POST"])
def register_user():
    if request.method == "POST":
        userName = request.form.get("userName")
        passWord = request.form.get("passWord")
        code =  request.form.get("code")
        if code != session.get('code'):
            result={'code':"10004",'msg':"code is error!"}
            return jsonify(result)

        if User().getUserByName(userName):
            result = {'code': "10004", 'msg': "user existed!"}
            return jsonify(result)

        if not userName or not passWord:
            result = {'code': "10004", 'msg': "username or password cant'n be bull"}
            return jsonify(result)

        user = User().registerUser(userName,passWord)
        session['userid'] = user.id
        user.updateCredit(50)
        credit = Credit()
        credit.creaet(50,"注册帐号")
        result = {'code': "10001", 'msg': "register ok"}
        return jsonify(result)


@register.route('/code',methods=["POST"])
def getCode():
    if request.method == "POST":
        emailAddress = request.form.get("userName")
        code = Code().gen_code()
        session['code'] = code
        mail = Mail()
        msg = mail.send(emailAddress,code)
        return msg

