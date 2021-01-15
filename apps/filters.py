from flask import Blueprint





filters = Blueprint("filters",__name__)

#
# @filters.template_filter('mylen')
# def mylen(arg):#实现一个可以求长度的函数
#     return arg[0:10]