import json
#To check for matches
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json", 'r'))
#print(data["rain"])


def translate(w):
    #Converts all the inputs to lowercase
    w = w.lower()
    check = get_close_matches(w, data.keys(), n=1, cutoff=0.8)
    if w in data:
        return data[w]
    elif len(check) > 0:
        choice = input(
            "Did you mean %s instead. Enter Y for yes or N for no." % check)
        if choice == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        if choice == "Y":
            return "Try another word"
        else:
            return "Sorry we don't understand your selection."
    else:
        return "Try another word."


word = input("Enter word : ")
output = translate(word)

if type(output) == list:
    for items in output:
        print(items)
else:
    print(output)