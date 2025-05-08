from flask import Flask, render_template, request, url_for


app = Flask(__name__)

@app.route('/')
def inicio():
   return render_template('index.html')

@app.route('/liga')
def liga():
   return render_template('LigaBetplay.html')

@app.route('/copaB')
def copaB():
   return render_template('CopaBetplay.html')

@app.route('/ligaE')
def ligaE():
   return render_template('LigaEspaña.html')

@app.route('/premierL')
def premierL():
   return render_template('PremierLeage.html')

@app.route('/championsL')
def championsL():
   return render_template('ChampionsLeage.html')

@app.route('/promedio_goles', methods=['GET', 'POST'])
def promedio_goles():
    promedio = None
    if request.method == 'POST':
        try:
            goles = int(request.form['goles'])
            partidos = int(request.form['partidos'])
            if partidos > 0:
                promedio = round(goles / partidos, 2)
            else:
                promedio = "Error: No se puede dividir entre cero"
        except ValueError:
            promedio = "Error: Ingresa valores numéricos válidos"

    return render_template('LigaBetplay.html', promedio=promedio)

if __name__ == '__main__':
    app.run(debug=True)
