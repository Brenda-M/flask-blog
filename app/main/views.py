
from flask import render_template, redirect, url_for, request, flash, abort
from . import main
from app import db, bcrypt

@main.route('/')
def index():



  return render_template('index.html', title = 'Welcome to TechBlog')