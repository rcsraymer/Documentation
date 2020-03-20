NewDictionary = {}


d = {'Key1':'Value1',      # keys must be unique
     'Key2':'Value2'}




# Access values by key
ValueOut = d['Key1']
ValueOut2 = d.get('Key1')




# change values
d['Key1'] = 7




# add values
d['Key3'] = 2009




# remove values
d.pop("Key3")





"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and values
get()	Returns the value of the specified key
items()	Returns a list containing the a tuple for each key value pair
keys()	Returns a list contianing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

"""
