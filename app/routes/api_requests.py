from flask import g
import requests
import json

# global variables
breed_list = []
dog_sizes = []


def breed_names():
    """
    appends all dog breed names and ids, from dog api, to the global variable breed_list
    
    """
    # make the call to the api and return the data
    breeds_url = 'https://api.thedogapi.com/v1/breeds?48dbab43-41dd-4351-9528-5f3aa2a1bd39'
    breeds = requests.get(breeds_url)
    db_list = json.loads(breeds.text)
    
    # iterate through the json data to create the list of ids and names for dropdown menu
    for n in db_list:
        name_id ={}
        name_id['id']=n['id']
        name_id['breed']=n['name']
        breed_list.append(name_id)
        
  
def breed_stats(id):
    """
    Returns a new object from the json data for a single dog breed. 
    
    After getting the json data we can get the specific stats for the breed and create
    a new object with those details.
    
    Parameter (id): is an id for the dog breed
    Precondition: id is an integer
    
    """
    # make the call to the api and return the data
    breed_url = 'https://api.thedogapi.com/v1/images/search?48dbab43-41dd-4351-9528-5f3aa2a1bd39&include_breed=1'
    param = {'breed_id': str(id)}
    response = requests.get(breed_url, params=param)
    data = json.loads(response.text)[0]
    
    breed_info = {}
    
    # get data from api and add to breed_info{} dictionary
    try:
        breed_info['id'] = data['breeds'][0]['id']
        breed_info['name'] = data['breeds'][0]['name']
        breed_info['weight'] = data['breeds'][0]['weight']['imperial']
        breed_info['height'] = data['breeds'][0]['height']['imperial']
        breed_info['use'] = data['breeds'][0]['bred_for']
        breed_info['group'] = data['breeds'][0]['breed_group']
        breed_info['temp'] = data['breeds'][0]['temperament'] 
        breed_info['lifespan'] = data['breeds'][0]['life_span']
        breed_info['image'] = data['url']
    except:
        breed_info['id'] = data['breeds'][0]['id']
        breed_info['name'] = data['breeds'][0]['name']
        breed_info['weight'] = data['breeds'][0]['weight']['imperial']
        breed_info['height'] = data['breeds'][0]['height']['imperial']
        # breed_info['use'] = data['breeds'][0]['bred_for']
        # breed_info['group'] = data['breeds'][0]['breed_group']
        breed_info['temp'] = data['breeds'][0]['temperament'] 
        breed_info['lifespan'] = data['breeds'][0]['life_span']
        breed_info['image'] = data['url']
        
    return breed_info
    
def get_size(lbs):
    """
    Appends an object containing an id and temperament string to global dictionary dog_sizes
    
    After getting the json data we determine what dogs are in the specified size range. 
    Then create a new object with the dog id and temperament that gets appended to a new global
    dictionary. 
    
    Parameter (lbs): is an number specifying the dog size in weight
    Precondition: id is a float
    
    """
    # make the call to the api and return the data
    breeds_url = 'https://api.thedogapi.com/v1/breeds?48dbab43-41dd-4351-9528-5f3aa2a1bd39'
    breeds = requests.get(breeds_url)
    db_list = json.loads(breeds.text)
    
    # iterate through the json data to compare the sizes
    for n in db_list:
        if 'temperament' in n:
            s = {}
            # get the max weight from api
            size = n['weight']['imperial']
            size = float(size.split(' ')[-1])
            
            if size <= 22 and lbs <= 22:
                s['id'] = n['id']
                s['temperament'] = n['temperament']
                dog_sizes.append(s)
                # print('small')
            elif (size >= 23 and size <= 55) and (lbs >= 23 and lbs <= 55):
                s['id'] = n['id']
                s['temperament'] = n['temperament']
                dog_sizes.append(s)
                # print('medium')
            elif lbs >= 56 and size >=56:
                s['id'] = n['id']
                s['temperament'] = n['temperament']
                dog_sizes.append(s)
                # print('large')
    # print(len(dog_sizes))  
    
        
breed_names()

    

