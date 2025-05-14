
info = {
    'key' : 'value',
    'name' : 'krishna',
    'age' : '20'
}
print(info)

# # 1.key method=================================================================================

print(info.keys()) 

print() # dict_keys(['key', 'name', 'age'])

# #2. Values Method===============================================================================

info = {
    'key' : 'value',
    'name' : 'krishna',
    'age' : '20'
}
print(info)

print(info.values())  #dict_values(['value', 'krishna', '20'])
print(list(info.values())) # ['value', 'krishna', '20']


# 3.fromkeys()=============================================================================

print()

keys = ['a', 'b', 'c']
default_value = 100
print(' -- With Single Value--')
my_dict = dict.fromkeys(keys, default_value)
print(my_dict)

print()

print(' -- With Mutliple Value--')
default_value = (100,200)
my_dict = dict.fromkeys(keys, default_value)
print(my_dict)

print()

keys = ['x', 'y', 'z']


print(' -- Default Value Is Not Given --')


my_dict = dict.fromkeys(keys)
print(my_dict)

print()
 

# 4.get()========================================================================================

info = {
    'key' : 'value',
    'name' : 'krishna',
    'age' : '20'
}
print(info)


print(info['name'])# krishna

print(info.get('name'))# krishna


print(info['name']) # error

print(info.get('name')) # none


## 5. Update()========================================================================================

print('----- Update() method -----')

dict1 = {'a': 1, 'b': 2}

dict2 = {'b': 3, 'c': 4}

dict1.update(dict2)

dict1.update({'d':'5'})

print(dict1)

print()



