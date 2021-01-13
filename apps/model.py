from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship


engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/blog?charset=utf8')

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
    content = Column(Text)
    user_id = Column(Integer,ForeignKey("tb_user.id"))
    tags = relationship('Tag', backref='articles', secondary=article_tag)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.titile)




class Tag(Base):
    __tablename__ = "tb_tag"
    id = Column(Integer,primary_key=True)
    name = Column(String(64))

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)



Base.metadata.create_all(engine)