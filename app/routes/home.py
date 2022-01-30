from flask import Blueprint, render_template, request, session, redirect, jsonify
import random
import json

# import files
# from .api_requests import breed_stats
from .api_requests import top_stats
# from .api_requests import breed_info as stats
from .api_requests import breed_list as breeds
from app.models import Breed
from app.db import get_db

# Blueprint() lets us consolidate routes into a single bp object
bp = Blueprint('home', __name__, url_prefix='/')

# route to index.html
@bp.route('/', methods=['GET', 'POST'])
def index():
    stats = {}
    # dispay the breed list for dropdown and breed card
    if request.method == 'POST':
        # breed_id = data.value
        breed_id = list(request.form.listvalues())[0][0]
        # print(breed_id)
        stats = top_stats(breed_id)
    else:
        try:
            random_num = random.randint(1, 264)
            stats = top_stats(random_num)
        except:
            stats = top_stats(165)
            
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

    return render_template('homepage.html', 
                        # card info
                           stats=stats,
                        # dropdown info
                           breeds=breeds,
                        # saved breed names
                           saved=single_id,
                           ids=ids,
                        #log session info
                        loggedIn=session.get('loggedIn')
                           )
# login page route
@bp.route('/login')
def login():
    # not yet logged in
    if session.get('loggedIn') is None:
        return render_template('login.html')
    
    return redirect('/dashboard')
# signup page route
@bp.route('/signup')
def signup():
    return render_template('signup.html')