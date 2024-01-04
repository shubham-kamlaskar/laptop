from flask import Flask,request,render_template
import pickle
import numpy as np

with open("model.pkl","rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("laptop.html")

@app.route("/price",methods=['POST'])
def pred():
    if request.method == "POST":
        Company = request.form['Company']
        TypeName = request.form['TypeName']
        Inches = request.form['Inches']
        Ram = request.form['Ram']
        OpSys = request.form['OpSys']
        # cpu = request.form['cpu']

        try:
            prediction = model.predict(np.array([[Company,TypeName,Inches,Ram,OpSys,0,0,0,0,0,0,0]]))
        except Exception as e:
            prediction =e

    return render_template("laptop.html",Price=str(prediction))

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
