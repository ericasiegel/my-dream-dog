from flask import Blueprint, render_template, session, request
from app.models import Breed, User
from app.db import get_db
import random
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
    attribute = 'hidden'
    message = ''
    if request.method == 'POST':
            data = request.form
            breed_stats(data['id'])
            attribute = ''
            message = 'hidden'
            
    else:
        attribute = 'hidden'
        message = ''
        
    
    
    
    # if request.method == 'POST':
    #     data = request.form
    #     breed_stats(data['id'])
    # else:
    #     try:
    #         random_num = random.randint(1, 264)
    #         breed_stats(random_num)
    #     except:
    #         breed_stats(200)
 
        
    return render_template('dashboard.html', 
                            # card info
                           stats=stats,
                           # saved breed names
                           saved=single_id,
                            attribute=attribute,
                            message=message,
                           #log session info
                            loggedIn=session.get('loggedIn')
                           )