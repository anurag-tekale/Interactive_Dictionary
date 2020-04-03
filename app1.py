import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
            return data[word]
    elif word.title() in data:
        return data[word.title()]   
    elif word.upper() in data:
        return data[word.upper()]         
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead ? Enter Y if YES, or N if no :" % get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]       
        elif yn == "N":
            return "\nThe word doesn't exist !! Please double check it ." 
        else :
         ab = input("We didn't understand your entry. Please try again !!\n Did you mean %s instead ? Enter Y if YES, or N if no :" % get_close_matches(word,data.keys())[0])
        if ab == "Y":
            return data[get_close_matches(word,data.keys())[0]]         
        else :
            return input("We didn't understand your entry. Please try again !!\n Did you mean %s instead ? Enter Y if YES, or N if no :" % get_close_matches(word,data.keys())[0])    
    else :
        return "The word doesn't exist !! Please double check it ."        

word = input("Enter a word : ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)        