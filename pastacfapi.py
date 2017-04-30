#!/opt/local/bin/python3.4
# pastacfapi.py
# https://github.com/camilleeyries/pasta.cf-python-API

import requests

SELF_BURNING = "self_burning"
EDITABLE = "editable"
STANDARD = "standard"

def create(pasta_title, pasta_text, pasta_type):
    """create a pasta of any type, and return it's properties"""
    print(pasta_type)
    data = {'filename': {pasta_title}, 'content': {pasta_text}, 'pasta_type': {pasta_type}}
    r = requests.post('https://pasta.cf/api/create', data=data)
    
    # Parsing the obtained informations
    # Process line by line, starting from the end.
    pasta = {'type': pasta_type}
    
    # Split by line the response obtained by the server
    response = r.text.split('\n') 
    
    while len(response) != 0:
        index = len(response) - 1
        print(index)
        print(response)
        
        if len(response[index].split(': ')) == 2:
            tmp = response[index].split(': ')
            print(tmp)
            pasta[tmp[0]] = tmp[1]
        
        # Removing last object from the array
        response = response[:-1]
        
    return pasta

def remove(pasta_token, pasta_password):
    """ Remove an editable pasta from pasta.cf with the password and token of the pasta."""
    data = {'password': {pasta_password}}
    r = requests.post('https://pasta.cf/' + pasta_token + '/remove2', data=data)

def edit(pasta_token, pasta_password, pasta_title, pasta_text):
    """ Edit an editable pasta from pasta.cf with the password and token of the pasta. """
    """ You need to provide the new title and the new text of the pasta. """
    data = {'password': {pasta_password}, 'filename': {pasta_title}, 'content': {pasta_text}}
    r = requests.post('https://pasta.cf/' + pasta_token + '/edit2', data=data)