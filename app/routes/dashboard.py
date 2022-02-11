from flask import Blueprint, render_template, session, request
from app.models import Breed, User
from app.db import get_db
from .api_requests import breed_stats
from app.utils.auth import login_required
import random

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/', methods=['GET', 'POST'])
@login_required
def dash():
    # query the Breed database to display the dog names and ids
    db = get_db()
    single_id = (
        db.query(Breed)
        .filter(Breed.user_id == session.get('user_id'))
        .all()
    )
    
    ids = []
    # print(single_id.__list__)
    for s in single_id:
        bid = s.__dict__['breed_id']
        ids.append(bid)
        # print(s.__dict__)
    # print(ids)

    attribute = ''
    message = ''
    stats = {}
    if request.method == 'POST':
            data = request.form
            # print(data)
            stats = breed_stats(data['id'])

            
            attribute = ''
            message = 'hidden'
            
    else:
        stats = breed_stats(1)
        attribute = 'hidden'
        message = ''
    # print(stats)
    
    # query the DB to get user's username
    user_name = (
        db.query(User)
        .filter(User.id == session.get('user_id'))
        .one()
    )
    
    username = user_name.__dict__['username']
    # print(user_name.__dict__['username'])
        
    return render_template('dashboard.html', 
                            # card info
                           stats=stats,
                           # saved breed names
                           saved=single_id,
                            attribute=attribute,
                            message=message,
                            username = username,
                           #log session info
                           ids=ids,
                            loggedIn=session.get('loggedIn')
                           )