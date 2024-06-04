from flask import Blueprint, render_template, request, redirect, url_for
from . import feedback

views = Blueprint('views',__name__)

@views.route('/')
def home():
  return render_template('home.html')

@views.route('/home')
def Home():
  return render_template('home.html')

@views.route('/dev', methods=['GET', 'POST'])
def developer():
  pfp = "https://graph.facebook.com/61555393773104/picture?height=720&width=720&access_token=6628568379%7Cc1e620fa708a1d5696fb991c1bde5662"
  if request.method == 'POST':
    name = request.form.get('name')
    message = request.form.get('message')
    feedback(name,message)
    return redirect('dev')
  return render_template('developer.html', tae=pfp)

@views.route('/geepi')
def api_list():
  return render_template('api.html')