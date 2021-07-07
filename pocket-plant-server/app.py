from flask import Flask, redirect, render_template, url_for, request, jsonify, session
from DB_handler import DBModule

from http_codes import http_response_code

app = Flask(__name__)
DB = DBModule()

@app.route("/")
def index():
    return "homepage"

@app.route("/postlist")
def post_list():
    pass

@app.route("/post/<int>")
def post(pid):
    pass

# http://192.168.0.43:5000/login_done?id=gjlee0802&pwd=08023384
@app.route("/login_done")
def login_done():
    uid = request.args.get("id")
    pwd = request.args.get("pwd")
    if DB.login(uid,pwd):
        return http_response_code['success200']
    else:
        return http_response_code['error401']

# http://192.168.0.43:5000/signin_done?id=gjlee0802&pwd=08023384&name=이경주&email=gjlee0802@naver.com
@app.route("/signin_done", methods = ["GET"])
def signin_done():
    uid = request.args.get("id")
    pwd = request.args.get("pwd")
    name = request.args.get("name")
    email = request.args.get("email")
    if DB.signin(uid, pwd, name, email):
        return http_response_code['success200']
    else:
        return http_response_code['error401']

@app.route("/plant_list", methods = ["/GET"])
def plant_list():
    uid = request.args.get("uid")
    if DB.get_user(uid):
        pass

@app.route("/create_plant", methods = ["/GET"])
def create_plant():
    uid = request.args.get("uid")
    plantname = request.args.get("plantname")
    plantkind = request.args.get("plantkind")
    if DB.get_user(uid):
        pass

@app.route("/grow_rate", methods = ["/GET"])
def grow_rate():
    uid = request.args.get("uid")
    plantname = request.args.get("plantname")
    pass

@app.route("/plant_age", methods = ["/GET"])
def plant_age():
    uid = request.args.get("uid")
    plantname = request.args.get("plantname")
    pass

@app.route("/plant_liferate", methods = ["/GET"])
def plant_liferate():
    uid = request.args.get("uid")
    plantname = request.args.get("plantname")
    pass

@app.route("/sensor_data", methods = ["/GET"]) 
def sensor_data():
    # json_data : {temp : value, hum : value, light : value, dusthum : value}
    uid = request.args.get("uid")
    reqjson = json.loads(request.get_data().decode())
    temp = reqjson['temp']
    hum = reqjson['hum']
    light = reqjson['light']
    dusthum = reqjson['dusthum']
    if DB.put_sensor_data(uid, reqjson, temp, hum, light, dusthum):
        pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)