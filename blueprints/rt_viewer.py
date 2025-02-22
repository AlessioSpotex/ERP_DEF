from flask import Blueprint, render_template

viewer_bp = Blueprint('viewer', __name__, url_prefix='/viewer')

@viewer_bp.route('/jdkajsdjkajdskja1')
def jdkajsdjkajdskja2():
    return "jdkajsdjkajdskja3"

@viewer_bp.route('/jdkajsdjkajdskja4')
def jdkajsdjkajdskja5():
    return "jdkajsdjkajdskja6."