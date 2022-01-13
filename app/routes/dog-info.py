import requests
import json
# API Information
# breed_list = 'https://api.thedogapi.com/v1/breeds?48dbab43-41dd-4351-9528-5f3aa2a1bd39'
dog_info = 'https://api.thedogapi.com/v1/images/search?48dbab43-41dd-4351-9528-5f3aa2a1bd39&include_breed=1&breed_id='

def breed_list():
    """
    function to return the list of breeds from dog api
    """
    breed_list = 'https://api.thedogapi.com/v1/breeds?48dbab43-41dd-4351-9528-5f3aa2a1bd39'
    breeds = requests.get(breed_list)
    db_list = json.loads(breeds.text)
    for name in db_list:
        print(name['name'])
    
breed_list()