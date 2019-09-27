from flask import Blueprint

bp = Blueprint('web', __name__)


@bp.route('/')
def index():
    """Return today's news"""
    return 'koowa2'
