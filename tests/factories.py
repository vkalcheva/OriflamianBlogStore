from random import randint

import factory

from db import db
from models import UserRole, BloggerModel, AdminModel


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)
        db.session.add(object)
        db.session.flush()
        return object


class BloggerFactory(BaseFactory):
    class Meta:
        model = BloggerModel

    id = factory.Sequence(lambda n: n)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
    phone = str(randint(100000, 200000))
    role = UserRole.blogger

class AdminFactory(BaseFactory):
    class Meta:
        model = AdminModel

    id = factory.Sequence(lambda n: n)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
    phone = str(randint(100000, 200000))
    role = UserRole.admin


