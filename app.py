from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    preguntas = {
        'fondo': request.form['fondo'],
        'deudas': request.form['deudas'],
        'seguros': request.form['seguros']
    }

    puntaje = sum([
        int(preguntas['fondo']),
        int(preguntas['deudas']),
        int(preguntas['seguros'])
    ])

    if puntaje <= 3:
        nivel = "Bajo"
        mensaje = "Tu preparación es baja. Estás en riesgo si ocurre una emergencia."
    elif puntaje <= 6:
        nivel = "Medio"
        mensaje = "Tienes cierta preparación, pero podrías mejorar mucho más."
    else:
        nivel = "Alto"
        mensaje = "¡Excelente! Tienes una buena base para enfrentar emergencias."

    # Enlace WhatsApp con mensaje personalizado
    nombre = request.form.get('nombre', 'Usuario')
    texto = f"Hola, soy {nombre}. Mi nivel de preparación financiera es: {nivel}. Me gustaría recibir una evaluación gratuita."
    texto_encoded = texto.replace(" ", "%20").replace("\n", "%0A")
    whatsapp_link = f"https://wa.me/17866719903?text={texto_encoded}"  # ← Cambia TU_NUMERO

    return render_template("resultado.html", nombre=nombre, nivel=nivel, mensaje=mensaje, whatsapp_link=whatsapp_link)



'''
if __name__ == '__main__':
    app.run(debug=True)
'''

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

