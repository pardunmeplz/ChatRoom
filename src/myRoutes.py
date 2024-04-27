from flask import render_template, request, session, redirect, url_for
from src.mySocket import myApp
import src.myData as d

@myApp.route('/chat')
def chat():
    if 'name' in session:
        return render_template("index.jinja")
    return redirect(url_for('landing'))

@myApp.route('/', methods=['GET', 'POST'])
def landing():
    if request.method == 'POST':
        session['name'] = request.data.decode('utf-8')
    if 'name' in session:    
        return redirect(url_for('chat'))
    return render_template("landing.jinja")
    