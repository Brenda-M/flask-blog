from flask import render_template, redirect, url_for, request, flash, abort
from app.models import BlogPost, Category
from . import main


@main.route('/')
@main.route('/home')
def index():

  category = Category.get_categories()

  return render_template('index.html', title = 'Welcome to TechBlog', category=category)

@main.route('/create-post', methods=['GET', 'POST'])
@login_required
def new_post():
  form = PostForm()
  if form.validate_on_submit():
    picture_file = ''
    if form.image_file.data:
      picture_file =  save_blog_picture(form.image_file.data)
    post = BlogPost(title=form.title.data, content=form.content.data, category=form.category.data, author=current_user, image_file=picture_file)
    db.session.add(post)
    db.session.commit()
    
    flash('Your post has been created!', 'success')
    return redirect(url_for('.index'))
  return render_template('create_post.html', title='New Post Blog', form=form, legend='New Post')
