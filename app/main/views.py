from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import current_user
from app.models import BlogPost
from .forms import NewPost
from .utils import save_blog_picture
from . import main
from app import db


@main.route('/')
@main.route('/home')
def index():

  blogpost = BlogPost.query.filter().order_by(BlogPost.created_at.desc())

  return render_template('index.html', title = 'Welcome to TechBlog', blogposts=blogpost)

@main.route('/new_post', methods=['GET', 'POST'])
def new_post():

  form = NewPost()

  if form.validate_on_submit():
    picture_file = ''
    if form.image_file.data:
      picture_file =  save_blog_picture(form.image_file.data)
    post = BlogPost(title=form.title.data, content=form.content.data, category=form.category.data, author=current_user, image_file=picture_file)
    db.session.add(post)
    db.session.commit()

    users = User.query.all()
    for user in users:
      if user.email != current_user.email:
        subscription_email(user.email)

    flash('Your post has been created!', 'success')
    return redirect(url_for('.index'))
  return render_template('create_post.html', title='New Post Blog', form=form, legend='New Post')
