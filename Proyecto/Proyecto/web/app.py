from flask import Flask, request, render_template_string
from model import funciones

app = Flask(__name__)

# ...existing code...
TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Calculadora Taylor</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
<h2>Calculadora Matemática</h2>
<form method="post">
    Función:
    <select name="funcion">
        <option value="exp">e^x</option>
        <option value="sin">sin(x)</option>
        <option value="cos">cos(x)</option>
        <option value="arcsin">arcsin(x)</option>
        <option value="arccos">arccos(x)</option>
        <option value="sinh">sinh(x)</option>
        <option value="cosh">cosh(x)</option>
    </select>
    <br><br>
    x: <input type="text" name="x">
    <input type="submit" value="Calcular">
</form>
<p>{{ resultado }}</p>
</body>
</html>
"""
# ...existing code...

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    if request.method == "POST":
        funcion = request.form["funcion"]
        x = float(request.form["x"])
        f = getattr(funciones, funcion)
        resultado = f"Resultado: {f(x)}"
    return render_template_string(TEMPLATE, resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
