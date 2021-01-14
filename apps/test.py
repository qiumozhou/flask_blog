from faker import Factory
from faker.generator import random

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from apps.db import engine
from apps.model import User, Tag, Article


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
            pubdate = faker.date_time()
        )
        for tag in random.sample(faker_tags, random.randint(2, 5)):
            article.tags.append(tag)
        session.add(article)
session.commit()
