from flask import Blueprint, render_template

public_bp = Blueprint('public', __name__, url_prefix='/')

@public_bp.route('/')
def homepage():
    return render_template('home.html')
