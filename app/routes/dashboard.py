from flask import Blueprint, render_template, session
from app.models import Breed
from app.db import get_db
from .api_requests import breed_stats
from .api_requests import breed_info as stats

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
    # query the Breed database to display the dog names and ids
    db = get_db()
    single_id = (
        db.query(Breed)
        .filter(Breed.user_id == session.get('user_id'))
        .all()
    )
    breed_stats(165)
    return render_template('dashboard.html', 
                            # card info
                           stats=stats,
                           # saved breed names
                           saved=single_id,
                           #log session info
                            loggedIn=session.get('loggedIn')
                           )