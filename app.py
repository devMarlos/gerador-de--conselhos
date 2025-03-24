from flask import Flask, render_template, redirect, url_for
import urllib.request, json, requests


app = Flask(__name__)

@app.route('/')
def index():
	titulo = "Conselhos.net"

	#================ Consumindo API conselhos =========================

	# Atribuindo o endereço da API para a variável
	url = "https://api.adviceslip.com/advice"

	# Criando uma variável para receber a requisição da API
	api_response = urllib.request.urlopen(url)

	# Criando uma variável para ler o conteúdo da requisição da API
	data = api_response.read()

	# Criando uma variável para transformar o cónteudo em arquivo json
	jsondata = json.loads(data)

	conselhos = jsondata['slip']['advice']

	#==================== Tradução do conselho ==========================
	url_trad = f"https://api.mymemory.translated.net/get?q={conselhos}&langpair=en|pt"
	api_trad_response = requests.get(url_trad)
	traduct = api_trad_response.json()['responseData']['translatedText']



	return render_template('index.html', titulo=titulo, conselhos=traduct)


@app.route('/outro')
def outro_conselho():
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)