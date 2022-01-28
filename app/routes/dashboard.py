from flask import Blueprint, render_template, session, request
from app.models import Breed, User
from app.db import get_db
from .api_requests import breed_stats
from .api_requests import breed_info as stats

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/', methods=['GET', 'POST'])
def dash():
    # query the Breed database to display the dog names and ids
    db = get_db()
    single_id = (
        db.query(Breed)
        .filter(Breed.user_id == session.get('user_id'))
        .all()
    )
    if request.method == 'POST':
        data = request.form
        breed_stats(data['id'])
        
    return render_template('dashboard.html', 
                            # card info
                           stats=stats,
                           # saved breed names
                           saved=single_id,
                           #log session info
                            loggedIn=session.get('loggedIn')
                           )