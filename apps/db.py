from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/blog?charset=utf8')
Session = sessionmaker(bind=engine)
dbsession = scoped_session(Session)