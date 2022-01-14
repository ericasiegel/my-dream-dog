import requests
import json

breed_info = {}
breed_list = []

def breed_names():
    """
    function to return the list of dog breeds and ids from dog api
    """
    breeds_url = 'https://api.thedogapi.com/v1/breeds?48dbab43-41dd-4351-9528-5f3aa2a1bd39'
    breeds = requests.get(breeds_url)
    db_list = json.loads(breeds.text)
    
    for n in db_list:
        name_id ={}
        # print(n['id'])
        # print(n['name'])
        name = n['name']
        dog_id = n['id']
        name_id['id']=dog_id
        name_id['breed']=name
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
    name = data['breeds'][0]['name']
    breed_info['name']=name
    weight = data['breeds'][0]['weight']['imperial']
    breed_info['weight']=weight
    height = data['breeds'][0]['height']['imperial']
    breed_info['height']=height
    use = data['breeds'][0]['bred_for']
    breed_info['use']=use
    group = data['breeds'][0]['breed_group']
    breed_info['group']=group
    temp = data['breeds'][0]['temperament']
    breed_info['temp']=temp
    lifespan = data['breeds'][0]['life_span']
    breed_info['lifespan']=lifespan
    image = data['url']
    breed_info['image']=image

    
breed_stats(29)  
breed_names()
# print(breed_info) 
# print(breed_list) 
    

