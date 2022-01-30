from flask import Blueprint, render_template, request, session, redirect, jsonify
from app.db import get_db
from .temp_list import temperament_list as tl
import requests
import json
import random
from .api_requests import get_size
from .api_requests import dog_sizes

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
    print(top_temps[:5])
    return top_temps[:5] #return the first 5 in list

@bp.route('/', methods=['GET', 'POST'])
def quiz():
        
    return render_template('quiz.html',
                            tl = tl,
                            loggedIn = session.get('loggedIn')
                            )

@bp.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        results = request.form
        print(results)
        
    return render_template('results.html',
                            # tl = tl,
                            loggedIn = session.get('loggedIn')
                            )  

# get_size(17)
# get_temperament('Strong', 'Quiet', 'Loving', 'Independent', 'Playful')