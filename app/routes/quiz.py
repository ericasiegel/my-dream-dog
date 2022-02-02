from flask import Blueprint, render_template, request, session, redirect, jsonify
from app.db import get_db
from app.models import Breed
from .temp_list import temperament_list as tl
import random
from .api_requests import get_size
from .api_requests import dog_sizes
from .api_requests import breed_stats
from app.utils.auth import login_required

# Blueprint
bp = Blueprint('quiz', __name__, url_prefix='/quiz')



    
def get_temperament(*args):
    """
    function to return the list of dog breeds and ids from dog api
    """
    
    temperament_ids = []
    new_temp_ids = []
    top_temps = []
    # print(args)
    
    # get the list of dog ids that match the temperament args
    for c in args:
        for t in dog_sizes:
            # print(t['breed_group'])
            if c in t["temperament"]:
                temperament_ids.append(t['id'])
    # print(sorted(temperament_ids))
    st = sorted(temperament_ids)
    
    # find all of the ids if they occur more than 3 times
    for r in range(265):
        if r in st:
            x = st.count(r)
            if x >= 3:
                new_temp_ids.append(r)
                
    # if the main list is less than 5 ids
    # find all of the ids if they occur 2 times
    if len(top_temps) < 5:
        for r in range(265):
            if r in st:
                x = st.count(r)
                if x == 2:
                    new_temp_ids.append(r)

    # if the main list is still less than 5 ids
    # randomy shuffle the remaining ids and add to final list
    if len(top_temps) < 5:
        rest = []
        for r in range(265):
            if r in st:
                x = st.count(r)
                if x == 1:
                    rest.append(r)
        # print(rest)
        random.shuffle(rest)
        # print(rest)
        top_temps = new_temp_ids + rest

    # print(top_temps)
    # print(top_temps[:5])
    return top_temps[:5] #return the first 5 in list

@bp.route('/', methods=['GET', 'POST'])
@login_required
def quiz():
        
    return render_template('quiz.html',
                            tl = tl,
                            loggedIn = session.get('loggedIn')
                            )
top_five = []
@bp.route('/results', methods=['GET', 'POST'])
@login_required
def results():
    # top_five = []
    if request.method == 'POST':
        results = request.form
        
        breed_size = results['size']
        # print(breed_size)
        
        get_size(float(breed_size))
        results_ids = get_temperament(results['temp1'],results['temp2'],results['temp3'],results['temp4'],results['temp5'])
        # print(results_ids)
        
        
        for i in results_ids:
            # print(i)
            stats = breed_stats(i)
            # print(stats)
            top_five.append(stats)
        # print(top_five)
        
        
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
        
    return render_template('results.html',
                            top_five = top_five,
                            ids=ids,
                            loggedIn = session.get('loggedIn')
                            )  

