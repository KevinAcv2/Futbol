from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/promedio-goles', methods=['GET', 'POST'])
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

    return render_template('promedio_goles.html', promedio=promedio)

if __name__ == '__main__':
    app.run(debug=True)
