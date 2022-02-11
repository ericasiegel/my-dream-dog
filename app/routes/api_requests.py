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
    Returns the json data for a single dog breed. 
    
    Parameter (id): is an id for the dog breed
    Precondition: id is an integer
    
    """
    # make the call to the api and return the data
    breed_url = 'https://api.thedogapi.com/v1/images/search?48dbab43-41dd-4351-9528-5f3aa2a1bd39&include_breed=1'
    param = {'breed_id': str(id)}
    response = requests.get(breed_url, params=param)
    data = json.loads(response.text)[0]
    # print(data['breeds'])
    breed_info = data
    # print(breed_info)
        
    return breed_info
    
def get_size(lbs):
    """
    Appends an object containing an id and temperament string to global dictionary dog_sizes
    
    After getting the json data we determine what dogs are in the specified size range. 
    Then create a new object with the dog id and temperament that gets appended to a new global
    dictionary. 
    
    Parameter (lbs): is a string
    Precondition: id is a float
    
    """
    # make the call to the api and return the data
    breeds_url = 'https://api.thedogapi.com/v1/breeds?48dbab43-41dd-4351-9528-5f3aa2a1bd39'
    breeds = requests.get(breeds_url)
    db_list = json.loads(breeds.text)
    
    dog_sizes = []
    
    # iterate through the json data to compare the sizes
    for n in db_list:
        if 'temperament' in n:
            s = {}
            # get the max weight from api
            size = n['weight']['imperial']
            size = float(size.split(' ')[-1])
            # print(size)
            # print(lbs)
            
            if lbs == 'small':
                if size < 23.0:
                    s['id'] = n['id']
                    s['temperament'] = n['temperament']
                    dog_sizes.append(s)
                    print(size)
            elif lbs == 'medium':
                if size >= 23 and size <= 55:
                    s['id'] = n['id']
                    s['temperament'] = n['temperament']
                    dog_sizes.append(s)
                    print(size)
            elif lbs == 'large':
                if size >=56:
                    s['id'] = n['id']
                    s['temperament'] = n['temperament']
                    dog_sizes.append(s)
                    print(size)
                    
            # print(s)
    return dog_sizes
    
        
breed_names()

    

