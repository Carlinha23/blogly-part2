#"""Seed file to make sample data for pets db."""

from models import User, Post, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

Post.query.delete()

# Add User
whiskey = User(first_name='Whiskey', last_name="dog")
bowser = User(first_name='Bowser', last_name="dog")
spike = User(first_name='Spike', last_name="porcupine")

#Add Post
bola = Post(title='Whiskey', content="dog")
carro = Post(title='Bowser', content="dog")
casa = Post(title='Spike', content="porcupine")

# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(bowser)
db.session.add(spike)

db.session.add(bola)
db.session.add(carro)
db.session.add(casa)
# Commit--otherwise, this never gets saved!
db.session.commit()
