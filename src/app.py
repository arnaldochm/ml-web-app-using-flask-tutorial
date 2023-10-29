from flask import Flask, request, render_template
from pickle import load
import pandas as pd

app = Flask(__name__)
model = load(open("../models/decisiontreeregressor.pkl", "rb"))


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        
        carat = float(request.form["carat"])
        cut = str(request.form["cut"])
        color = str(request.form["color"])
        clarity = str(request.form["clarity"])
        depth = float(request.form["depth"])
        table = float(request.form["table"])
        x = float(request.form["x"])
        y = float(request.form["y"])
        z = float(request.form["z"])
        colums = ['carat','cut','color','clarity','depth','table','x','y','z']

        data = pd.DataFrame([[carat, cut, color, clarity, depth, table, x, y, z]], columns=colums)
        print(data)
        prediction = str(model.predict(data)[0])
        print(prediction)
    else:
        prediction = None
    
    return render_template("index.html", prediction = prediction)