import cloudpickle

with open('model.pkl', 'rb') as file_in:
  model_loaded = cloudpickle.load(file_in)

print(model_loaded.predict(['péssimo']))