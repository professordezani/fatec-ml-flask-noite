import cloudpickle
from flask import Flask, render_template, request

with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', nome='Análise se cancer maligno ou beligno')

@app.route('/predicao', methods=['POST'])
def predicao():
  radius_mean = request.form['radius_mean']
  texture_mean = request.form['texture_mean']
  perimeter_mean = request.form['perimeter_mean']
  area_mean = request.form['area_mean']
  smoothness_mean = request.form['smoothness_mean'] 
  compactness_mean = request.form['compactness_mean']
  concavity_mean = request.form['concavity_mean']

  array=[[str(radius_mean),str(texture_mean), str(perimeter_mean), str(area_mean), str (smoothness_mean), str (compactness_mean), str(concavity_mean)]]

  predicao = model.predict([array])


  return render_template('resposta.html', predicao=predicao[0])

app.run(debug=True)

# pip install -r requirements.txt (instala as bibliotecas)
# python app.py (para executar)
