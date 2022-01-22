from flask import Blueprint, render_template

from .api_requests import breed_stats
from .api_requests import breed_info as stats

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
    breed_stats(165)
    return render_template('dashboard.html', 
                            # card info
                           stats=stats
                           )