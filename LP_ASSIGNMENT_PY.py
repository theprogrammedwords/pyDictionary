import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open(r"C:\Users\admin\Downloads\data.json"))
#dictionary of 49537 words

#.............................................................................................................................
#                                               Word search segment                                                    
#.............................................................................................................................
def translate(word) :
    word = word.lower()
    if word in data :
        print("---------------\nMatch found !\n---------------\n")
        return data[word]
    
    elif word.title() in data:
        print("---------------\nMatch found !\n---------------\n")
        return data[word.title()]
    
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    
    elif len(get_close_matches(word,data.keys()))>0 :
        user_input = input("Did you mean %s instead ?\n\n----Enter YES or NO----\n" % get_close_matches(word,data.keys())[0])
        
        if user_input == "YES"  :
            return data[get_close_matches(word,data.keys())[0]]
        
        elif user_input =="NO" :
            print("No problem. Suggest us some usage:)")
            define_usage(data,word)
            return data[word]
        
        else :
            print("We didn't get you !\n")
            define_usage(data,word)
            return data[word]
    
    else:
        return "invalid query"

#.............................................................................................................................
#                                               Word entry segment                                                    
#.............................................................................................................................


def define_usage(data, word):
    msg = 'Enter usage for word [%s]: '
    if not data.get(word):                 
        data[word] = []                     
        usage = input(msg % word)           
        data[word].append(usage)    
        with open(r"C:\Users\admin\Downloads\data.json", 'w') as outfile:
            json.dump(data, outfile)          

#.............................................................................................................................
#                           Driver segment
#.............................................................................................................................        

print("*****************\nMY DICTIONARY\n*****************")
word = input(".....................\nEnter search terms\n.....................\n\n")


output = translate(word)

print("---------------\nRESULT -->\n---------------\n")

if type(output) == list :
    for item in output :
        print(item)

else :  
    print(output)



    
#    test segments    
#    In [1]: import json
#       ...: d = json.load(open("data.json"))
#    
#    In [2]: def define_usage(data, word):
#       ...:     msg = 'Enter usage for word [%s]: '
#       ...:     if not data.get(word):                 # does this word NOT already exist?
#      ...:         data[word] = []                     # if yes, then create a new word
#       ...:     usage = input(msg % word)              # get the new usage from the user
#       ...:     data[word].append(usage)               # store the new usage for this word
#      ...:
#     
#    In [3]: define_usage(d, 'cow')                     # the word 'cow' already exists
#       ...: d.get('cow')
#    Enter usage for word [cow]: Says "moo" a lot.
#    ['To inspire fear or hesitation due to fear.',
#     'Female bovine animal (Bos taurus) of the subfamily Bovinae of the family Bovidae.',
#     'Any domestic bovine regardless of sex or age.',
#     'Says "moo" a lot.']
#     
#    In [4]: define_usage(d, 'foobar')                  # the word 'foobar' is a brand new word
#       ...: d.get('foobar')
#    Enter usage for word [foobar]: Nothing at all.
#    ['Nothing at all.']
