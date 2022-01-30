import requests
import json

breed_info = {}
breed_list = []
# breed_single = {}

def breed_names():
    """
    function to return the list of dog breeds and ids from dog api
    """
    breeds_url = 'https://api.thedogapi.com/v1/breeds?48dbab43-41dd-4351-9528-5f3aa2a1bd39'
    breeds = requests.get(breeds_url)
    db_list = json.loads(breeds.text)
    
    for n in db_list:
        name_id ={}
        name_id['id']=n['id']
        name_id['breed']=n['name']
        breed_list.append(name_id)
        
  
def breed_stats(id):
    """
    function to return the json data for a single dog breed. After getting the json data
    we can get the specific stats for the breed
    Parameter: (id) is the id of the selected dog breed
    """
    breed_url = 'https://api.thedogapi.com/v1/images/search?48dbab43-41dd-4351-9528-5f3aa2a1bd39&include_breed=1'
    param = {'breed_id': str(id)}
    response = requests.get(breed_url, params=param)
    data = json.loads(response.text)[0]
    
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
        
        
        
breed_names()
# print(breed_info) 
# print(breed_list) 
    

