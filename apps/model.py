import math
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from apps.db import engine, dbsession

Base = declarative_base()

class User(Base):
    __tablename__ = "tb_user"
    id = Column(Integer,primary_key=True)
    username = Column(String(64),nullable=False,index=True)
    password = Column(String(64),nullable=False)
    email = Column(String(64),nullable=False,index=True)
    articles = relationship("Article",backref="author")

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)


article_tag = Table(
    "article_tag",Base.metadata,
    Column("article_id",Integer,ForeignKey("tb_article.id")),
    Column("tag_id",Integer, ForeignKey("tb_tag.id"))
)

class Article(Base):
    __tablename__ = "tb_article"
    id = Column(Integer,primary_key = True)
    titile = Column(String(255),nullable=False,index=True)
    pubdate = Column(DateTime,nullable=False)
    type = Column(Integer,nullable=False)
    reading_volume = Column(Integer)
    cost_integral = Column(Integer)
    content = Column(Text)
    user_id = Column(Integer,ForeignKey("tb_user.id"))
    tags = relationship('Tag', backref='articles', secondary=article_tag)

    def getOneArticle(self,id):
        row = dbsession.query(Article).filter(Article.id==id).first()
        return row

    def getPageNumber(self):
        articleTotal = len(dbsession.query(Article).all())
        number = math.ceil(articleTotal / 10)
        return number

    def getPageArticle(self,start,end):
        row = dbsession.query(Article)[start:end]
        return row

    def getSideArticle(self,type,page):
        row = dbsession.query(Article).filter(Article.type == type)[page*10-10:page*10]
        return row

    def getTypeNumber(self,type):
        number = math.ceil(dbsession.query(Article).filter(Article.type == type).count()/10)
        return number

    def getSearchArticle(self,keyword,page):
        row = dbsession.query(Article).filter(Article.titile.like('%'+keyword+'%'))[page*10-10:page*10]
        return row

    def getSearchNumber(self, keyword):
        number = math.ceil(dbsession.query(Article).filter(Article.titile.like('%'+keyword+'%')).count()/10)
        return number

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.titile)




class Tag(Base):
    __tablename__ = "tb_tag"
    id = Column(Integer,primary_key=True)
    name = Column(String(64))

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)



Base.metadata.create_all(engine)