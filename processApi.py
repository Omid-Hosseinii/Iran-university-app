import requests
import sys
sys.path.insert(0, 'C:/Users/Omid/Desktop/soale32')
from model import *
#----------------------------------------------------------------
def get_Api(url):
    response= requests.get(url)
    if response.status_code == 200:
        JsonData=response.json()
        return JsonData


def get_stateInfo(jdata, state):
    uniList=[]
    for university in jdata:
        if university['state-province']==state:
            uni1=University(university['name'],university['web_pages'])
            uniList.append(uni1)
    return uniList        