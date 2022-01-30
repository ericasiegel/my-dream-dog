from flask import Blueprint, render_template, request, session, redirect, jsonify
# from app.db import get_db
# from .temp_list import temperament_list as tl
import requests
import json
# from .api_requests import

# Blueprint
bp = Blueprint('quiz', __name__, url_prefix='/quiz')

dog_sizes = []

def get_size(lbs):
    breeds_url = 'https://api.thedogapi.com/v1/breeds?48dbab43-41dd-4351-9528-5f3aa2a1bd39'
    breeds = requests.get(breeds_url)
    db_list = json.loads(breeds.text)
    
    for n in db_list:
        if 'temperament' in n:
            s = {}
            size = n['weight']['imperial']
            # if '-' in size:
            #     size = size.split(' - ')[-1]
            size = float(size.split(' ')[-1])
            
            if size <= 22 and lbs <= 22:
                s['id'] = n['id']
                s['temperament'] = n['temperament']
                dog_sizes.append(s)
                print('small')
            elif (size >= 23 and size <= 55) and (lbs >= 23 and lbs <= 55):
                s['id'] = n['id']
                s['temperament'] = n['temperament']
                dog_sizes.append(s)
                print('medium')
            elif lbs >= 56 and size >=56:
                s['id'] = n['id']
                s['temperament'] = n['temperament']
                dog_sizes.append(s)
                print('large')
    # print(len(dog_sizes))
    
def get_temperament(*args):
    """
    function to return the list of dog breeds and ids from dog api
    """
    
    temperament_ids = []
    top_temps = []
    # print(args)
    for c in args:
        for t in dog_sizes:
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
                else:
                    top_temps.append(r)

    print(top_temps)
    print(top_temps[:5])
    # return top_temps[:5]

@bp.route('/', methods=['GET', 'POST'])
def quiz():
    pass

get_size(60)
get_temperament('Strong', 'Quiet', 'Loving', 'Independent', 'Playful')