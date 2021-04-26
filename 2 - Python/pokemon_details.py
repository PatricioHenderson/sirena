#!/usr/bin/env python

""" 

This program will generate a detailed pokemon  list in a .csv file 
including their name , id , weight, height and base_hp.

Will use aiohttp to make a faster program: pip3 install aiohttp

"""

__author__ = "Patricio Henderson"
__email__ = "patriciohenderson@hotmail.com"
__version__ = "1.0"

import json
import requests
import csv
import aiohttp
import asyncio
info  = []
total_pokemon = (0)
asyncio.set_event_loop(asyncio.new_event_loop())




def extract():
    print("Starting, this could take a while")
    # First get how many pokemons are there listated
    url = 'https://pokeapi.co/api/v2/pokemon-form/'
    response = requests.get(url)
    data = json.loads(response.text)
    data = response.json()
    global total_pokemon
    total_pokemon =  total_pokemon + int((data['count']))
    

# Once i get how many pokemons are, request all of them 
async def transform():
    try:
        for i in range(1,total_pokemon):
            asyncio.set_event_loop(asyncio.new_event_loop())
            loop = asyncio.new_event_loop() 
            asyncio.get_event_loop()
            url= 'https://pokeapi.co/api/v2/pokemon/{}/' .format(str(i))
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()
                    # clean the data that is needed 
        
                    filter_data = ( data['id'] , data['name'], data['weight'] , data['height'] , data['stats'][0]['base_stat'] )
                    info.append(filter_data)
                    await asyncio.gather(load())
        
    except:
        
        pass
        

async def load():
    try:        
        # Writing down to a .csv file the infomation required.
        with open ("pokemons_details.csv" , "w",newline='') as fo:
            
            writer = csv.writer(fo)
            writer.writerows(info)
    except:
        pass

if __name__ == "__main__":
    

        
    extract()
    asyncio.run(transform())
    #load()