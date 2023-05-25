import numpy as np
import pandas as pd
import pickle

model = pickle.load(open('models/model.pkl', 'rb'))

data = pd.read_csv('data/cleaned_car_price.csv')

def classified(manufacturer,column):
    value = data[data['Manufacturer'] == manufacturer][column].unique()
    return value

from werkzeug.wrappers import Request, Response
from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import json

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/')
def main():
    manufacturers = list(data['Manufacturer'].unique())
    return render_template('main.html',manufacturers = manufacturers)

@app.route("/home", methods = ['POST'])
def home():
    manufacturer = request.form.get('manufacturer')
    session['my_var'] = manufacturer
    categories = classified(manufacturer, 'Category')
    prod = classified(manufacturer, 'Prod. year')
    cylinders = classified(manufacturer, 'Cylinders')
    colors = classified(manufacturer, 'Color')
    airbags = classified(manufacturer, 'Airbags')
    return render_template('index.html', prod=prod, categories=categories, cylinders=cylinders, colors=colors, airbags=airbags)
    return manufacturer

@app.route('/result', methods = ['POST'])
def result():
    manufacturer = session.get('my_var', None)
    
    levy = request.form.get('levy')
    prod = request.form.get('prod')
    category = request.form.get('category')
    leather = request.form.get('leather')
    fuel = request.form.get('fuel')
    engine = request.form.get('volume')
    mileage = request.form.get('mileage')
    cylinder = request.form.get('cylinder')
    gear = request.form.get('gear')
    drive = request.form.get('Drive')
    door = request.form.get('Doors')
    wheel = request.form.get('Wheel')
    color = request.form.get('color')
    airbags = request.form.get('airbag')
    turbo = 0
    
    data = [levy,manufacturer,prod,category,leather,fuel,engine,mileage,cylinder,gear,drive,door,wheel,color,airbags,turbo]
    result = np.array(data).reshape(1,-1)
    prediction = model.predict(result)
    prediction = np.exp(prediction)
    prediction = int(prediction)
    
    if prediction == 0:
        return 'Error'
    else :
        return render_template('result.html',prediction = prediction)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 9000, app)