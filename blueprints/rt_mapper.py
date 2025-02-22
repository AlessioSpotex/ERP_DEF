from flask import Blueprint, render_template

mapper_bp = Blueprint('mapper', __name__, url_prefix='/mapper')

@mapper_bp.route('/jajaja')
def sasa():
    return "fdvwsv"

@mapper_bp.route('/sasa')
def dadaosaoda():
    return "sajdska."