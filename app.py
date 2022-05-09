import cloudpickle

with open('model.pkl', 'rb') as file_in:
  model_loaded = cloudpickle.load(file_in)

frase = input('Digite uma frase: ')

if model_loaded.predict([frase])[0] == 0:
    print('Comentário negativo')
else:
    print('Comentário positivo')