from flask import Blueprint, render_template

pages_bp = Blueprint('pages', __name__, url_prefix='/pages')

@pages_bp.route('/dashboard')
def homepage():
    return render_template('dashboard.html')

@pages_bp.route('/logout')
def login():
    return render_template('logout.html')
    