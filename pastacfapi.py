#!/opt/local/bin/python3.4
# pastacfapi.py
# https://github.com/camilleeyries/pasta.cf-python-API

import requests

SELF_BURNING = "self_burning"
EDITABLE = "editable"
STANDARD = "standard"

def create(paste_title, paste_text, paste_type):
    print(paste_type)
    data = {'filename': {paste_title}, 'content': {paste_text}, 'pasta_type': {paste_type}}
    r = requests.post('https://pasta.cf/api/create', data=data)
    
    # Parsing the obtained informations
    # Process line by line, starting from the end.
    paste = {'type': paste_type}
    
    # Split by line the response obtained by the server
    response = r.text.split('\n') 
    
    while len(response) != 0:
        index = len(response) - 1
        print(index)
        print(response)
        
        if len(response[index].split(': ')) == 2:
            tmp = response[index].split(': ')
            print(tmp)
            paste[tmp[0]] = tmp[1]
        
        # Removing last object from the array
        response = response[:-1]
        
    return paste