from flask import Flask, redirect, render_template, url_for, request, jsonify
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

@app.route("/login_done")
def login_done():
    pass

# http://0.0.0.0:5000/signin_done?email=gjlee0802@naver.com&id=gjlee0802&pwd=08023384&name=이경주
@app.route("/signin_done", methods = ["GET"])
def signin_done():
    email = request.args.get("email")
    uid = request.args.get("id")
    pwd = request.args.get("pwd")
    name = request.args.get("name")
    print(email, uid, pwd, name)
    return "success"
    '''
    if DB.signin(email, uid, pwd, name):
        return http_response_code['success200']
    else:
        return http_response_code['error401']
    '''

@app.route("/plant_list", methods = ["GET"])
def plant_list():
    uid = request.args.get("uid")
    if DB.get_user(uid):
        pass

@app.route("/create_plant", methods = ["GET", "POST"])
def create_plant():
    uid = request.args.get("uid")
    plantname = request.args.get("plantname")
    plantkind = request.args.get("plantkind")
    if DB.get_user(uid):
        pass

@app.route("/grow_rate", methods = ["GET"])
def grow_rate():
    uid = request.args.get("uid")
    plantname = request.args.get("plantname")
    pass

@app.route("/plant_age", methods = ["GET"])
def plant_age():
    uid = request.args.get("uid")
    plantname = request.args.get("plantname")
    pass

@app.route("/plant_liferate", methods = ["GET"])
def plant_liferate():
    uid = request.args.get("uid")
    plantname = request.args.get("plantname")
    pass

@app.route("/sensor_data", methods = ["GET", "POST"]) 
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
