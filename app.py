from flask import Flask, render_template, request
import cloudpickle

with open('model.pkl', 'rb') as file_in:
  model_loaded = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
  comentario = request.form['comentario']
  sentimento = model_loaded.predict([comentario])[0]
  print(sentimento)
  return render_template('resposta.html', resposta=sentimento)

# @app.route("/<frase>")
# def predict(frase):

#   if model_loaded.predict([frase])[0] == 0:
#     return 'Comentário negativo'
#   else:
#     return 'Comentário positivo'

app.run(debug=True)