from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db
class User(db.model):
    password_hash = db.Column(db.String(128))
    @property
    def password(self):
        raise AttributeError('passowrd is not a readable attribute')
    @password.setter
    def passowrd(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    