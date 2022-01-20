from crypt import methods
from tkinter.tix import Select
from flask import Blueprint, render_template, request
from django.shortcuts import render

# import files
from .api_requests import breed_stats
from .api_requests import breed_info as stats
from .api_requests import breed_list as breeds

# Blueprint() lets us consolidate routes into a single bp object
bp = Blueprint('home', __name__, url_prefix='/')

# route to index.html
@bp.route('/', methods=['GET', 'POST'])
def index():
    # try:
    #     random_num = random.randint(1, 264)
    #     breed_stats(random_num)
    # except:
    #     breed_stats(165)

    
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