import pickle

# Object to be pickled
data = {"name": "Alice", "age": 30, "city": "New York"}

# Pickle the object and write it to a file
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)
