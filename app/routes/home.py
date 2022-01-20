from crypt import methods
from tkinter.tix import Select
from flask import Blueprint, render_template, request
import random

# import files
from .api_requests import breed_stats
from .api_requests import breed_info as stats
from .api_requests import breed_list as breeds

# Blueprint() lets us consolidate routes into a single bp object
bp = Blueprint('home', __name__, url_prefix='/')

# route to index.html
@bp.route('/', methods=['GET', 'POST'])
def index():
    # if 'Submit' != 'Submit':
    
    if request.method == 'POST':
        # breed_id = data.value
        breed_id = list(request.form.listvalues())[0][0]
        # print(breed_id)
        breed_stats(breed_id)
    else:
        try:
            random_num = random.randint(1, 264)
            breed_stats(random_num)
        except:
            breed_stats(165)
    
    return render_template('homepage.html', 
                        # card info
                           stats=stats,
                       
                        # dropdown info
                           breeds=breeds
                           )
# login page route
@bp.route('/login')
def login():
    return render_template('login.html')
# signup page route
@bp.route('/signup')
def signup():
    return render_template('signup.html')