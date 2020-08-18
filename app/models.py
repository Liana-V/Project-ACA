from __init__ import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'USERS'

    def __repr__(self):
        return self.DISTRICT


class Level(db.Model):
    __tablename__ = 'LEVEL'

class Category(db.Model):
    __tablename__ = 'CATEGORY'


class Post(db.Model):

    __tablename__ = 'JOBS'

    def __repr__(self):
        return self.DISTRICT

class Users_skills(db.Model):

    __tablename__ = 'USER_SKILLS'
class Jobs_skills(db.Model):

    __tablename__ = 'JOBS_SKILLS'
class Skills(db.Model):

    __tablename__ = 'SKILLS'