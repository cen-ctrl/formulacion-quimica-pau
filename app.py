from flask import Flask, request, jsonify, render_template
import random
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("compuestos_inorganicos.csv")
compuestos = dict(zip(df["Nombre"], df["Fórmula"]))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/nombre")
def nombre_aleatorio():
    nombre = random.choice(list(compuestos.keys()))
    print(nombre)
    return jsonify({"nombre": nombre})

@app.route("/verificar", methods=["POST"])
def verificar():
    data = request.json
    nombre = data.get("nombre", "")
    print(nombre)
    respuesta = data.get("respuesta", "").strip().lower()
    correcta = compuestos.get(nombre)
    print(correcta)
    es_correcta = correcta and (correcta.lower() == respuesta.lower())
    return jsonify({"correcto": es_correcta, "esperada": correcta})

if __name__ == "__main__":
    app.run(debug=True)
