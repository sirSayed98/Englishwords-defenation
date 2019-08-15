import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    m = get_close_matches(w, data.keys())
    if w in data:
        return data[w]
    elif len(m) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %m[0])
        if yn == "Y":
            return data[m[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
flag=False
while(not flag):
    word = input("Enter word:  or E to exit  " )
    if (word != 'E' ):
        output = translate(word)
        if type(output) == list:
            for item in output:
                print(item)
        else:
                print(output)
                
    else:
        flag=True            
