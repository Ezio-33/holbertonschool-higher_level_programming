#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv
import sqlite3
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

def read_sqlite_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    conn.close()
    products = []
    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
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
    elif source == 'sql':
        try:
            products = read_sqlite_db()
        except sqlite3.Error as e:
            return render_template('product_display.html', error=f"Database error: {e}")
    else:
        return render_template('product_display.html', error="Wrong source. Use 'json', 'csv', or 'sql'.")

    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)