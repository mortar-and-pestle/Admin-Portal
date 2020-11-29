from admin import db, login_manager
from flask_login import UserMixin
from sqlalchemy.orm import backref


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(70), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    type = db.Column(db.String(15), unique = True, nullable = True)

    # def __repr__(self):
    #     return f"User('{self.username}', '{self.email}', '{self.password}', '{self.type}')"
