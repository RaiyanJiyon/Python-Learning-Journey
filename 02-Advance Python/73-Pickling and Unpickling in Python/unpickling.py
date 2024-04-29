import pickle

# Unpickle the object from the file
with open("data.pkl", "rb") as file:
    data = pickle.load(file)
    print(data)
