import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("./teaching/data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        y_n = input('Did you mean to say %s instead? Enter y/n: ' % get_close_matches(word, data.keys())[0])
        y_n = y_n.lower()
        newWord = get_close_matches(word, data.keys())[0]
        if y_n == "y":
            return data[newWord]
        elif y_n == 'n':
            return 'Please enter a new word'
        else:
            return "Sorry, I didn't recognize that command."
    else:
        return 'Oops! It looks like that word does not exist.'

word = input('Enter word: ')

output = print(translate(word))

if type(output) == list:
    for item in output:
        print(output[item])
else:
    print(output)