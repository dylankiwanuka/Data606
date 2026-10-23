import pymongo
import requests

import pymongo
import requests

client = pymongo.MongoClient("mongodb://localhost:27017")

# Pick the database, then the collection inside it
db = client["starwars"]
characters = db["characters"]
starships = db["starships"]

def get_starships():
    url = "https://swapi.dev/api/starships/"
    response = requests.get(url)
    #turn into a dictionary
    data = response.json()
    return data

def get_pilot_ids(starship):
    # Empty list to collect the ObjectIds
    list_of_ids = []

    # Go to the pilots key: it's a list of web links
    for pilot_url in starship["pilots"]:
        # Visit the link and turn the response into a dictionary
        pilot_info = requests.get(pilot_url).json()

        # Get the name out of that dictionary
        name = pilot_info["name"]

        # Search our own collection by name, only return the _id
        # find_one gives back a dictionary, or None if nothing matches
        result = characters.find_one({"name": name}, {"_id": 1})

        # Only add it if we actually found the character
        if result is not None:
            # result is {"_id": ObjectId(...)}, so grab the value inside
            list_of_ids.append(result["_id"])
        else:
            # Shows which pilots didn't match
            print("Not found in characters:", name)

    return list_of_ids

def replace_pilots_and_insert(starship):
    updated_starship = starship
    updated_starship["pilots"] = get_pilot_ids(starship)
    # insert_one because this is ONE starship (a single dictionary)
    starships.insert_one(updated_starship)  
    #test
    #print(updated_starship["name"], updated_starship["pilots"])  


#data is a dictionary (count, next, previous, results)
data = get_starships()

# The list of starships lives inside the "results" key
starship_list = data["results"]

# Go through the list, one starship (dictionary) at a time
for starship in starship_list:
    replace_pilots_and_insert(starship)




