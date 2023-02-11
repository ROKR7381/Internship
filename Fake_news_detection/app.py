from flask import Flask, escape, request, render_template
import pickle
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin


app = Flask(__name__)

@app.route('/')
@cross_origin()
def homePage():
    return render_template("index.html")

app=Flask(__name__,template_folder='templates')




if __name__=='__main__':
    app.run(debug=True)