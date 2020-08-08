from new_version.__init__ import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model,UserMixin):
    __tablename__ = 'USERS'

    def __repr__(self):
        return self.DISTRICT


class Post(db.Model):
    __tablename__ = 'JOBS'

    def __repr__(self):
        return self.DISTRICT

