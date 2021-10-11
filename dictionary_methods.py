myDict = {
    "fast": "In a Quick Manner",
    "harish": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'harish': 'Player'},
    1: 3
}

# Dictionary Methods
print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.values()) # Prints the values of the dictionary
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Shruti": "Friend",
    "Sanika": "Friend",
    "harish": "A writer"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)
print(myDict.get("harish")) # Prints value associated with key "harish"
print(myDict.get("harish2")) # Returns None as harish2 is not present in the dictionary

