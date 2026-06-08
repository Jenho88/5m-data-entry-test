def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    temp_dct = dct
    if key in temp_dct:
        print(temp_dct.get(key))
        temp_dct[key] = value
    return temp_dct



tmpdct1 = update_dictionary({}, "name", "Alice")
tmpdct2 = update_dictionary({"age": 25}, "age", 26)
print(tmpdct1)
print(tmpdct2)



# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
