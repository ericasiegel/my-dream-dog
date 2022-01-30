from flask import Blueprint, render_template, request, session, redirect, jsonify
# from app.db import get_db
# from .temp_list import temperament_list as tl
import requests
import json
# from .api_requests import

# Blueprint
bp = Blueprint('quiz', __name__, url_prefix='/quiz')

def get_temperament(*args):
    """
    function to return the list of dog breeds and ids from dog api
    """
    breeds_url = 'https://api.thedogapi.com/v1/breeds?48dbab43-41dd-4351-9528-5f3aa2a1bd39'
    breeds = requests.get(breeds_url)
    db_list = json.loads(breeds.text)
    
    temperament_ids = []
    top_temps = []
    print(args)
    for c in args:
        for t in db_list:
            if 'temperament' in t:
                # print(t['breed_group'])
                if c in t["temperament"]:
                    temperament_ids.append(t['id'])
    
    print(sorted(temperament_ids))
    st = sorted(temperament_ids)
    for r in range(265):
        if r in st:
            x = st.count(r)
            if x >= 3:
                top_temps.append(r)
    if len(top_temps) < 5:
        for r in range(265):
            if r in st:
                x = st.count(r)
                if x == 2:
                    top_temps.append(r)
    print(top_temps)
    # print(top_temps[:5])
    # return temperament_ids

@bp.route('/', methods=['GET', 'POST'])
def quiz():
    pass

get_temperament('Friendly', 'Confident', 'Loving', 'Independent', 'Active')