from flask import Flask, render_template
import requests
import facebook

class geepi:
  def __init__(self, token):
    self.token = token
    print()
    print(self.token)
  def send_comment(self, id, comment):
    try:
      fb = facebook.GraphAPI(access_token=self.token, version='2.12')
      fb.put_comment(object_id=id, message=comment)
      return True
    except Exception as a:
      return False
  # CREDITS: Joshua Sy
  # FACEBOOK: https://www.facebook.com/joshg101
  # SITE: https://deku-rest-api-3ijr.onrender.com/
  def AI(text=None, model='gpt-3'):
    try:
      models = {
        "gpt-4": 'https://deku-rest-api-3ijr.onrender.com/new/gpt-4_adv?prompt=',
        "gpt-3": 'https://deku-rest-api-3ijr.onrender.com/new/gpt-3_5-turbo?prompt=',
        "palm": 'https://deku-rest-api-3ijr.onrender.com/api/palm2?q=',
        "qwen": 'https://deku-rest-api-3ijr.onrender.com/api/ask?model=qwen-b7&q=',
        "leo": 'https://deku-rest-api-3ijr.onrender.com/api/ask?model=leo&q=',
        "gemini": 'https://deku-rest-api-3ijr.onrender.com/new/gemini?prompt=',
        "linerva": 'https://deku-rest-api-3ijr.onrender.com/api/liner?q='
      }
      if text == None: 
        print('[ ERROR ] - Muka kang paa')
        return {"error": 'Missing prompt'}
      elif model not in models:
        print('[ ERROR ] - No model found')
        return {"error": 'Invalid Ai model'}
      else:
        url = models[model] + text
        respo = requests.get(url)
        if(respo.status_code != 200):
          print('[ ERROR ] - Ako bakla? sakalin ko mama mo')
          return {"error": 'failed to fetch'}
        else:
          res = respo.json()
          if model == 'gpt-3' or model == 'gpt-4':
            return {"result":res['result']['reply']}
          elif model == 'palm':
            return {"result":res['result']}
          elif model == 'qwen' or model == 'leo':
            return {"result":res['result']['message']}
          elif model == 'gemini':
            return {"result":res['result']['data']}
          else:
            return {"result": res['result']}
    except Exception as e:
      print(f"[ ERROR ] - {e}")
      return {"error": e}

def greeg():
  from .views import views
  from .pages import page
  from .api import api
  
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'I Love Tito Mars'
  
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(page, url_prefix='/page')
  app.register_blueprint(api, url_prefix='/api')
  
  @app.errorhandler(404)
  def Error_not_found(code):
    return render_template('404.html'),404
  
  return app

def feedback(name,message):
  text = f"NAME: {name}\n\nMESSAGE:\n{message}"
  token = "7121586614:AAEdgLmnrSfs5TndOgAhExQ_o_6q196E_x0"
  requests.post('https://api.telegram.org/bot{}/sendMessage?chat_id=7075537944&text={}'.format(token,text))