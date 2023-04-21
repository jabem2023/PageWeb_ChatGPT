from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_url_path='/static')

# Rutas de la página web
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        # Aquí se podrían agregar código para enviar el correo electrónico
        return redirect(url_for("contacto_confirmacion"))
    else:
        return render_template("contacto.html")

@app.route("/contacto-confirmacion")
def contacto_confirmacion():
    return render_template("contacto_confirmacion.html")

if __name__ == "__main__":
    app.run(debug=True, port=5017)

