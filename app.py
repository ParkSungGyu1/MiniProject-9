import hashlib
from flask import Flask, render_template, jsonify, request, Response
from pymongo import MongoClient
import json
import jwt
from datetime import datetime, timedelta
import certifi
from googleapiclient.discovery import build


def build_youtube_search(developer_key):
  DEVELOPER_KEY = developer_key
  YOUTUBE_API_SERVICE_NAME="youtube"
  YOUTUBE_API_VERSION="v3"
  return build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

def get_search_response(youtube, query):
  search_response = youtube.search().list(
    q = query,
    order = "relevance",
    part = "snippet",
    maxResults = 10
    ).execute()
  return search_response

def get_video_info(search_response):
  result_json = {}
  idx =0
  for item in search_response['items']:
    if item['id']['kind'] == 'youtube#video':
      result_json[idx] = info_to_dict(item['id']['videoId'], item['snippet']['title'], item['snippet']['description'], item['snippet']['thumbnails']['medium']['url'])
      idx += 1
  return result_json

def info_to_dict(videoId, title, description, url):
  result = {
      "videoId": videoId,
      "title": title,
      "description": description,
      "url": url
  }
  return result

app = Flask(__name__)
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.dm2wy.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

SECRET_KEY = 'SPARTA'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main')
def main_page():
    return render_template('page_main.html')

@app.route('/signup')
def login_page():
    return render_template('signup.html')

@app.route('/sign_in', methods=['POST'])
def sign_in():
    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'id': username_receive, 'password': pw_hash})

    print(result)

    if result is not None:
        payload = {
            'id': username_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

@app.route("/check", methods=["POST"])
def check_post():
    id_receive = request.form['id_give']
    user = db.users.find_one({'id': id_receive})
    if user is not None:
        return jsonify({'msg': 0})
    else:
        return jsonify({'msg': 1})

@app.route("/signup", methods=["POST"])
def bucket_done():
    id_receive = request.form['id_give']
    password_receive = request.form['pw_give']
    name_receive = request.form['name_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "id": id_receive,  # 아이디
        "password": password_hash,  # 비밀번호
        "username": name_receive,  # 프로필 이름 기본값은 아이디
    }
    db.users.insert_one(doc)
    return jsonify({'msg': 'POST(완료) 연결 완료!'})

@app.route('/video_list', methods=['POST'])
def get_video_list():
  developer_key = "AIzaSyC-Fl9ZYqK1t98RqKb1xWQ4AtGLnLrz9CI"
  query = request.form['search_give']
  youtube = build_youtube_search(developer_key)
  search_response = get_search_response(youtube, query)
  res = json.dumps(get_video_info(search_response), ensure_ascii=False)
  return Response(res, content_type='application/json; charset=utf-8')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)