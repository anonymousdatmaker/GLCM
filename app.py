import numpy as np
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
	return "[[0. 0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0. 0.]]\n [[2 2 3 4]\n [3 1 5 3]\n [2 3 4 6]\n [2 3 2 4]]\n 2 3 1 3\n 6 3\n [[0. 0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0. 0.]]"
