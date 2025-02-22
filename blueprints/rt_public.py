from flask import Blueprint, render_template, url_for

public_bp = Blueprint('public', __name__, url_prefix='/')

@public_bp.route('/')
def homepage():
    return render_template('home.html')

@public_bp.route('/login')
def login():
    return render_template('login.html')