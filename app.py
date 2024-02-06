"""Blogly application."""

from flask import Flask, render_template, request, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)


@app.route('/')
def list_users():
    users = User.query.all()
    return render_template('list.html', users=users)


@app.route('/', methods=["POST"])
def create_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    return redirect(f'/{user.id}')

@app.route("/<int:user_id>")
def show_user(user_id):
    """Show info on a single pet."""

    user = User.query.get_or_404(user_id)
    return render_template("detail.html", user=user)

@app.route('/<int:user_id>/edit')
def users_edit(user_id):
    """Show a form to edit an existing user"""

    user = User.query.get_or_404(user_id)
    return render_template('/edit.html', user=user)


@app.route('/<int:user_id>/edit', methods=["POST"])
def users_update(user_id):
    """Handle form submission for updating an existing user"""

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/")


@app.route('/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):
    """Handle form submission for deleting an existing user"""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/")

@app.route('/<int:user_id>/post')
def users_post(user_id):
    """Show a form to edit an existing user"""

    user = User.query.get_or_404(user_id)
    return render_template('/post.html', user=user)

@app.route('/<int:pk>/post', methods=["POST"])
def users_post_update(pk):
    """Handle form submission for updating an existing user"""

    user = User.query.get_or_404(pk)
    user.title = request.form['title']
    user.content = request.form['content']

    post = Post(title=user.title, content=user.content, user_id=user.id)

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('users_post', user_id=pk))

@app.route('/<int:user_id>/post/<int:post_id>')
def post_detail(user_id, post_id):
    """Show post detail page."""

    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)

    return render_template('post_detail.html', user=user, post=post)
