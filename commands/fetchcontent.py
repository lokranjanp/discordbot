def getInsult():
    response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    return response.json()['insult']


def getCompliment():
    response = requests.get("https://complimentr.com/api")
    return response.json()['compliment']


#
def getJoke():
    response = requests.get("https://sv443.net/jokeapi/v2/joke/Any")
    if (response.json()['type'] == "twopart"):
        print([response.json()['setup'], response.json()['delivery']])
        return [response.json()['setup'], response.json()['delivery']]
    else:
        return response.json()['joke']
