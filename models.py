"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, 
                    primary_key=True, 
                    autoincrement=True)

    first_name = db.Column(db.String(50), 
                            nullable=False)

    last_name = db.Column(db.String(30), nullable=False)

    image_url = db.Column(db.String, nullable=False, default=DEFAULT_IMAGE_URL)  # You can provide a default image URL or set it to None

    def greet(self):
        #"""Greet using name."""

        return f"I'm {self.first_name}, {self.last_name or 'thing'}"

    def __repr__(self):
       # """Show info about user."""

        p = self
        return f"<User {p.id} {p.first_name} {p.last_name} {p.image_url}>"

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    title = db.Column(db.String(100), nullable=False)

    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"<Post {self.id} {self.title} {self.user_id}>"
