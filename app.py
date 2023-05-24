from flask import Flask, render_template, request
import tkinter as tk

import pandas as pd 
import plotly.graph_objects as go

data = pd.read_csv('table.csv')
def my_function():
    l1=data[data['FMAX[-]_ref']<data['FMAX[-]_cur']]
    print(l1['Testcase'])
    print([1,2,3,4])


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/execute', methods=['POST'])
def execute():
    if request.method == 'POST':
        my_function()
    return 'Function executed successfully!'

if __name__ == '__main__':
    app.run(debug=True)
