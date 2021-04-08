#importing json
import json
import code


#accessing JSON file with open file object.
with open ('code.json') as j:
    data = json.load(j)

# object accessed
#print(data)

#objective is to flatten out the inputted json data and return it as a json object.
#print(type(data))
#The data is recieved as a dict, i need to extract the values out of the object.

def flatten_object(argu):

    #delcaing new dictionary
    result = {}

    #function to extract values from dict object
    def flatten(xkey, value=''):
        #conditional statement to check type of data 
        if type(xkey) is dict:
            for key in xkey:
                #new print statement
                #as requested the . is seperating characters
                flatten(xkey[key],  value +  key + '.' )
                
            #if the object is already a list , it will iterate through value and reprint it a key and vlaye seperated by .
        elif type(xkey) is list:
            i = 0
            for key in xkey:
                flatten( key,  value + str(i) +  '.')
                
                i + 1
        else:
            result[value[:-1]] = xkey
    flatten(argu)
    return result

#print statment with JSON object passed in as parameter
flatten_json=(flatten_object(data))

#print for function testing.
print(flatten_json)

# will use dump to write back to new JSON file

#open new file and 'write' to file , will declare as j 

with open('flatten_json_code.json', 'w') as j:
    #json dump , added the data you want to write to file , e.g. write flatten_json to j file
    #need to add indent to get correct print 
    json.dump(flatten_json,j,indent=1)



