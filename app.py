import cloudpickle

with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

print(model.predict(['bom']))