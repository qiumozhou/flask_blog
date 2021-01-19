from flask import Blueprint, session, request, jsonify, redirect, url_for, make_response

from apps.model import  User
from common.code import  Checkcode


login = Blueprint("login",__name__)

@login.route('/verifycode',methods=["GET"])
def getVerifyCode():
    code = Checkcode(width=80, height=32)

    pic = code['picture']  # image对象
    code_str = code.codelist
    session["verifyCode"] = code_str
    print(code_str)
    import base64
    from io import BytesIO
    buffered = BytesIO()
    pic.save(buffered, format="png")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str


@login.route('/login',methods=["POST"])
def login_in():
    if request.method == "POST":
        username = request.form.get("userName")
        password = request.form.get("passWord")
        ver_code = request.form.get("code")

        if ver_code.lower()!= session.get("verifyCode").lower():
            result = {'code': "10004", 'msg': "code is error!"}
            return jsonify(result)

        user = User().getUserByAll(username,password)
        if not user:
            result = {'code': "10004", 'msg': "username or password is error!"}
            return jsonify(result)
        else:
            session['username'] = user.username
            result = {'code': "10001", 'msg': "success", "data": user.username}
            resp = make_response(jsonify(result))  # 设置响应体
            resp.set_cookie("username", user.username, max_age=3600)
            return resp


@login.route('/logout',methods=["get"])
def logout():
    resp = make_response("ok")
    # 删除cookie
    resp.delete_cookie("username")
    session.pop("username")
    return resp
