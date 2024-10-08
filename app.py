from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/procesar", methods=['POST'])
def converter():
    value = float(request.form["a"]) 
    op1 = request.form["op1"]
    op2 = request.form["op2"]

    result = 0

    if op1 == op2:
        result = value
    else:
        if op1 == "kilometers" and op2 == "meters":
            result = Km_a_m(value)
        elif op1 == "meters" and op2 == "kilometers":
            result = m_a_km(value)
        elif op1 == "meters" and op2 == "feet":
            result = m_a_ft(value)
        elif op1 == "feet" and op2 == "meters":
            result = ft_a_m(value)
        elif op1 == "kilometers" and op2 == "miles":
            result = Km_a_mi(value)
        elif op1 == "miles" and op2 == "kilometers":
            result = mi_a_km(value)


        elif op1 == "kilograms" and op2 == "pounds":
            result = kg_a_lb(value)
        elif op1 == "pounds" and op2 == "kilograms":
            result = lb_a_kg(value)
        elif op1 == "grams" and op2 == "ounces":
            result = g_a_oz(value)
        elif op1 == "ounces" and op2 == "grams":
            result = oz_a_g(value)


        elif op1 == "celsius" and op2 == "fahrenheit":
            result = c_a_f(value)
        elif op1 == "fahrenheit" and op2 == "celsius":
            result = f_a_c(value)
        elif op1 == "celsius" and op2 == "kelvin":
            result = c_a_k(value)
        elif op1 == "kelvin" and op2 == "celsius":
            result = k_a_c(value)
        else:
            result = None
    results = f"{value} {op1} = {result} {op2}"

    return render_template("result.html", results=results)


def Km_a_m(km):
    return km * 1000

def m_a_km(m):
    return m / 1000

def Km_a_mi(km):
    return km * 0.621371

def mi_a_km(mi):
    return mi / 0.621371

def m_a_ft(m):
    return m * 3.28084

def ft_a_m(ft):
    return ft / 3.28084

def kg_a_lb(kg):
    return kg * 2.20462

def lb_a_kg(lb):
    return lb / 2.20462

def g_a_oz(g):
    return g * 0.035274

def oz_a_g(oz):
    return oz / 0.035274


def c_a_f(c):
    return (c * 9/5) + 32

def f_a_c(f):
    return (f - 32) * 5/9

def c_a_k(c):
    return c + 273.15

def k_a_c(k):
    return k - 273.15

if __name__ == "__main__":
    app.run(debug=True)
