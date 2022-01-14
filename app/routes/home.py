from flask import Blueprint, render_template
from .api_requests import breed_info as stats

# Blueprint() lets us consolidate routes into a single bp object
bp = Blueprint('home', __name__, url_prefix='/')

# route to index.html
@bp.route('/')
def index():
    breed = stats['name']
    use = stats['use']
    height = stats['height']
    weight = stats['weight']
    temp = stats['temp']
    lifespan = stats['lifespan']
    group = stats['group']
    img = stats['image']
    return render_template('homepage.html', 
                           breed=breed, 
                           use=use, 
                           height=height,
                           weight=weight,
                           temp=temp,
                           lifespan=lifespan,
                           group=group,
                           img=img
                           )
# login page route
@bp.route('/login')
def login():
    return render_template('login.html')
# signup page route
@bp.route('/signup')
def signup():
    return render_template('signup.html')