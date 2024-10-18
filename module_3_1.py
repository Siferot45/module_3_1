#Function calls are counted automatically.
def count_calls():
    global calls
    calls += 1
       
# Returns a tuple of: the length of this string, an uppercase string, and a lowercase string.
def string_info(string):
    count_calls()
    return (len(string), string.lower(), string.upper()) 

# Returns "True" if the row is in this list, "False" if it is missing
def is_contains(string, list_to_search):
    count_calls()
    # Default, there are no matches
    is_faind = False
    
    for x in list_to_search:
        if x.lower() == string.lower():
            is_faind = True
            
    return is_faind


print(string_info('Capybara'))
print(string_info('Cat'))
print(string_info('Dog'))
print(string_info('Cat-dog-capybar'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) 
print(is_contains('cycle', ['recycling', 'cyclic'])) 
print(is_contains('cat', ['CaT', 'DOg', 'CapYbara'])) 

calls = 0
print(calls)