from matplotlib.font_manager import json_dump
from numpy import delete
import requests
import json

URL="http://127.0.0.1:8000/studentapi/"

# def get_data(id=None):
#     data={}
#     if id is not None:
#      data={'id':id}
# json_data=json.dumps('data')

# r=requests.get(url=URL,data=json_data)
# data=r.json()
# print(data)

# get_data()

post data
def post_data():
    data={
        'name':'Ravi',
        'roll':105,
        'city':'Delhi'
    }
    
    json_data=json.dumps(data)
    
    r=requests.post(url=URL,data=json_data)
    data=r.json()

post_data()

def update_data():
    data={
        'id':69,
        'name':'Alex',
        'city':'Satara'
    }
    
    json_data=json.dumps(data)
    
    r=requests.put(url=URL,data=json_data)
    data=r.json()

# update_data()

# def delete_data():
#     data={'id':2}
    
#     json_data=json.dumps(data)
    
#     r=requests.delete(url=URL,data=json_data)
#     data=r.json()

