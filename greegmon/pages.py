from flask import render_template, Blueprint, redirect, url_for

page = Blueprint('page', __name__)

@page.get('/ai/<model>')
def gpt(model):
  try:
    if model == 'gpt4':
      return render_template(f'pages/ai/{model}.html', haha='gpt-4'),200
    elif model == 'gpt3':
      return render_template(f'pages/ai/{model}.html', haha='gpt-3'),200
    elif model == 'palm':
      return render_template(f'pages/ai/{model}.html', haha='palm'),200
    elif model == 'qwen':
      return render_template(f'pages/ai/{model}.html', haha='qwen'),200
    elif model == 'leo':
      return render_template(f'pages/ai/{model}.html', haha='leo'),200
    elif model == 'gemini':
      return render_template(f'pages/ai/{model}.html', haha='gemini'),200
    elif model == 'linerva':
      return render_template(f'pages/ai/{model}.html', haha='linerva'),200
    else:
      return render_template('404.html'),404
  except:
    return render_template('404.html'),404

@page.get('/fb/auto-comment')
def auto_comment():
  return render_template('pages/fb/comment.html')