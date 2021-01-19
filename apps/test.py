from faker import Factory
from faker.generator import random

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from apps.db import engine
from apps.model import User, Tag, Article, Credit

Base = declarative_base()

faker = Factory.create()
Session = sessionmaker(bind=engine)
session = Session()

faker_users = [User(
    username=faker.name(),
    password=faker.word(),
    email=faker.email(),
) for i in range(10)]
session.add_all(faker_users)


faker_tags= [Tag(name=faker.word()) for i in range(20)]
session.add_all(faker_tags)


for i in range(100):
        article = Article(
            titile=faker.sentence(),
            content=' '.join(faker.sentences(nb=random.randint(70, 100))),
            author=random.choice(faker_users),
            pubdate = faker.date_time(),
            type = faker.random_int(min=1,max=6),
            reading_volume = faker.random_int(min=100,max=900),
            cost_integral = faker.random_int(min=1,max=10)
        )
        for tag in random.sample(faker_tags, random.randint(2, 5)):
            article.tags.append(tag)
        session.add(article)


credit_category =[[1,"用户登录"],[50,"用户注册"],[2,"评论文章"],[-5,"阅读文章"],[200,"用户投稿"]]
faker_credit = [Credit(
    category=credit_category[random.randint(0,4)][1],
    credit=credit_category[random.randint(0,4)][0],
    user=random.choice(faker_users),
    createtime=faker.date_time(),
    updatetime=faker.date_time()

) for i in range(10)]
session.add_all(faker_users)

session.commit()
