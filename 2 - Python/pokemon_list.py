#!/usr/bin/env python

""" 

This program will generate a pokemon list in a .csv file 
including their name and id

"""

__author__ = "Patricio Henderson"
__email__ = "patriciohenderson@hotmail.com"
__version__ = "1.0"

import json
import requests
import csv
info  = []

def fetch():
    # First get how many pokemons are there listated
    url = 'https://pokeapi.co/api/v2/pokemon-form/'
    response = requests.get(url)
    data = json.loads(response.text)
    data = response.json()
    total_pokemon = (data['count'])

    # Once i get how many pokemons are, request all of them in just one page so
    # the program will run faster than reloading the page with many offsets.
    url= 'https://pokeapi.co/api/v2/pokemon-form/?offset=0&limit={}' .format(str(total_pokemon))
    response = requests.get(url)
    data = json.loads(response.text)
    data = response.json()
    # clean the data that is needed 
    filter_data = (data['results'])
    
    # Starting id count
    number = 0
    
    
    # Extract the information that is required.
    for i in filter_data:
        
        name = i['name']
        number += 1               
        information = ( name, number)
        # Stock all the information in 'info' list, so the program can work faster than writing line by line
        # once it gets the information required.
        info.append(information)
        
def info_downgrade():        
    # Writing down to a .csv file the infomation required.
    with open ("pokemons_details.csv" , "w",newline='') as fo:
            
        writer = csv.writer(fo)
        writer.writerows(info)
        
       
    

if __name__ == "__main__":
    fetch()

    info_downgrade()