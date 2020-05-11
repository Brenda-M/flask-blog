import markdown2
from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import current_user, login_required
from app.models import BlogPost, User
from .forms import NewPost
from .utils import save_blog_picture
from . import main
from app import db
from app.email import subscription_email


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
      picture_file =  save_blog_picture(form.image_file.data).decode('utf-8')
    post = BlogPost(title=form.title.data, content=form.content.data, category=form.category.data, author=current_user, image_file=picture_file)
    db.session.add(post)
    db.session.commit()

    users = User.query.all()
    for user in users:
      if user.email != current_user.email:
        subscription_email("New Post Alert", "email/new_post_subscription", user.email, user=user)

    flash('Your post has been created!', 'success')
    return redirect(url_for('.index'))
  return render_template('create_post.html', title='New Post Blog', form=form, legend='New Post')

@main.route('/post/<int:blogpost_id>/update', methods=['GET', 'POST'])
@login_required
def update_post( blogpost_id):

  post = BlogPost.query.get_or_404( blogpost_id)

  if post.author != current_user:
    abort(403)
  form = NewPost()
  if form.validate_on_submit():
    post.title = form.title.data
    post.content = form.content.data
    db.session.commit()
    flash('Your blog post has been updated', 'success')
    return redirect(url_for('.index', blogpost_id= blogpost_id))
  elif request.method == 'GET':
    form.title.data = post.title
    form.content.data = post.content
  return render_template('create_post.html', title='Update Blog Post', form=form, legend='Update Post',  blogpost_id= blogpost_id)

@main.route('/post/<int:blogpost_id>/delete', methods=['POST'])
@login_required
def delete_post(blogpost_id):
  post = BlogPost.query.get_or_404(blogpost_id)
  if post.author != current_user:
    abort(403)
  db.session.delete(post)
  db.session.commit()
  flash('Your post has been deleted', 'success')
  return redirect(url_for('.index'))
