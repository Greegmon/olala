import requests as req
from . import geepi
from flask import request, Blueprint, jsonify
from flask_cors import CORS

api = Blueprint('api',__name__)
CORS(api)

@api.route('/ai',methods=['GET'])
def AIs():
  Model = request.args.get('model')
  query = request.args.get('q')
  if Model is None or query is None:
    return jsonify({"status": 400, "message": 'Missimg parameters value'}),400
  ai = geepi.AI(text=query, model=Model)# default gpt-3, pede kahit wag na lagyan mg model
  if 'error' in ai:
    return jsonify({"error": ai['error']}),403
  else:
    return jsonify({"message": ai['result'], "model": Model}),200

@api.get('/auto-comment')
def auto_comment():
  token = request.args.get('token')
  comment = request.args.get('comment')
  post_id = request.args.get('postId')
  count = request.args.get('count')
  print(token, comment, post_id, count)
  if not token or not comment or not post_id:
    print("Error una")
    return jsonify({'status': 'error', 'error_msg': 'Invalid parameter value'}),403
  else:
    fb = geepi(token)
    i = 0
    while i < int(count):
      graph = fb.send_comment(post_id, comment)
      if not graph:
        print("Errkr Dalawa")
        return jsonify({'status': 'error'}),403
      else:
        i += 1
    return jsonify({'status': 'success', 'total': i}),200