from .rt_public import public_bp
from .rt_admin import admin_bp
from .rt_pages import pages_bp
from .rt_function import function_bp
from .rt_api import api_bp
from .rt_viewer import viewer_bp
from .rt_mapper import mapper_bp
from .rt_modular import modular_bp

blueprints_register = [
    public_bp,
    admin_bp,
    pages_bp,
    function_bp,
    api_bp,
    viewer_bp,
    mapper_bp,
    modular_bp
]