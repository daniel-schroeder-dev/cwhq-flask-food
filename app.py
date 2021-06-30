from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/show_pizza", methods=["GET", "POST"])
def show_pizza():
    num_pizzas = request.form.get("num_pizzas", 1, int)
    return render_template("pizza.html", num_pizzas=num_pizzas)


@app.route("/show_tacos", methods=["GET", "POST"])
def show_tacos():
    num_tacos = request.form.get("num_tacos", 1, int)
    return render_template("tacos.html", num_tacos=num_tacos)
