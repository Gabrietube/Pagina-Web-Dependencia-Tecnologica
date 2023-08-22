from flask import Flask
import random

app = Flask(__name__)

facts_list = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
              "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
              "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas",
              "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo"
]
@app.route("/")
def hello_world():
    return '<h1>Dependencia Tecnologica</h1>  <a href="/random_facts">¡Ver un dato aleatorio!</a> <a href="/Lanza_Monedas">¡Lanzar Moneda!</a>'

@app.route("/random_facts")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/Lanza_Monedas")
def Lanzador():
    number = ["Cara", 
            "Sello"]
    return f'<p>{random.choice(number)}</p>'

app.run(debug=True)
