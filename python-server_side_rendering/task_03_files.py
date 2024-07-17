#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def read_csv_file(filepath):
    products = []
    with open(filepath, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    if source == 'json':
        filepath = 'products.json'
        if os.path.exists(filepath):
            products = read_json_file(filepath)
        else:
            return render_template('product_display.html', error="JSON file not found.")
    elif source == 'csv':
        filepath = 'products.csv'
        if os.path.exists(filepath):
            products = read_csv_file(filepath)
        else:
            return render_template('product_display.html', error="CSV file not found.")
    else:
        return render_template('product_display.html', error="Wrong source. Use 'json' or 'csv'.")

    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)