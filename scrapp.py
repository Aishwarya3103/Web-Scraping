import pandas
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/pylib')
def pylib():
	return render_template('pylib.html')

@app.route('/procedure')
def procedure():
	return render_template('procedure.html')

@app.route('/op')
def op():
	filename="products.csv"
	data=pandas.read_csv(filename,header=0)
	products=list(data.values)
	return render_template('op.html',products=products)

if __name__=="__main__":
	app.run(debug=True)