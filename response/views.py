from wsgiref import headers
from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.
def token(request,code):
    client_id="45668d094cc568a80fe2"
    client_secret="a302ce5b33b473bd543fa395010e82803915e786"
    
    if(code != None):
        
        userToken=requests.post("https://github.com/login/oauth/access_token?client_id=45668d094cc568a80fe2&client_secret=a302ce5b33b473bd543fa395010e82803915e786&code={}".format(code))
        userToken=userToken.text
        tokenAndScope=userToken.split('=',1)
        token_only=tokenAndScope[1].split('&',1)
        token=token_only[0]
        if token!=None:
            headers={
                'Authorization': 'token {}'.format(token)
            }
            user_object=requests.get("https://api.github.com/user?",headers=headers)
        

    return HttpResponse(user_object,content_type='application/json')

def user(request,token):
    if token!=None:
            headers={
                'Authorization': 'token {}'.format(token)
            }
            user_object=requests.get("https://api.github.com/user?",headers=headers)
            print(user_object)

    return HttpResponse(user_object,content_type='application/json')
