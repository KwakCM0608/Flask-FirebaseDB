from flask import Flask, redirect, render_template, url_for, request, jsonify, session
from DB_handler import DBModule

from http_codes import http_response_code

from Plant_handler import PlantUpdate

app = Flask(__name__)
app.secret_key = 'abcdefghijklmnopqrstuvwxyz'
DB = DBModule()
PU = PlantUpdate()

@app.route("/")
def index():
    return "homepage"

@app.route("/postlist")
def post_list():
    pass

@app.route("/post/<int>")
def post(pid):
    pass

# http://0.0.0.0:5000/login_done?id=gjlee0802&pwd=08023384
@app.route("/login_done")
def login_done():
    uid = request.args.get("id")
    pwd = request.args.get("pwd")
    if DB.login(uid,pwd):
        session['user'] = uid
        return http_response_code['success200']
    else:
        return http_response_code['error401']

@app.route("/logout_done")
def logout_done():
    session.pop('user', None)
    return http_response_code['success200']

# http://0.0.0.0:5000/signin_done?id=gjlee0802&pwd=08023384&name=이경주&email=gjlee0802@naver.com
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

# http://0.0.0.0:5000/plant_list?id=gjlee0802
@app.route("/plant_list", methods = ["GET"])
def plant_list():
    uid = request.args.get("id")
    if 'user' in session:
        if session['user'] == uid:
            response = DB.plant_list(uid)
            return jsonify(response)                   # Should return json : { plantid1 : {...}, plantid2 : {...} }

    return http_response_code['error401']

# http://0.0.0.0:5000/create_plant?id=gjlee0802&plantname=MyPlant&plantkind=Cactus
@app.route("/create_plant", methods = ["GET", "POST"])
def create_plant():
    uid = request.args.get("id")
    plantname = request.args.get("plantname")
    plantkind = request.args.get("plantkind")
    if 'user' in session:
        if session['user'] == uid:
            return DB.create_plant(uid, plantname, plantkind)      # Return plant id
    return http_response_code['error401']

'''
Maybe unnecessary functions?
@app.route("/grow_rate", methods = ["GET"])
def grow_rate():
    uid = request.args.get("id")
    plantname = request.args.get("plantname")
    pass

@app.route("/plant_age", methods = ["GET"])
def plant_age():
    uid = request.args.get("id")
    plantname = request.args.get("plantname")
    pass

@app.route("/plant_liferate", methods = ["GET"])
def plant_liferate():
    uid = request.args.get("id")
    plantname = request.args.get("plantname")
    pass
'''

# Security Problem
@app.route("/sensor_data", methods = ["GET", "POST"]) 
def sensor_data():
    # json_data : {id : userid, pid : plantid, temp : value, hum : value, light : value, dusthum : value}
    reqjson = request.get_json()#json.loads(request.get_data().decode())   # Load json
    uid = reqjson['id']
    pid = reqjson['pid']
    temp = reqjson['temp']
    hum = reqjson['hum']
    light = reqjson['light']
    dusthum = reqjson['dusthum']
    if DB.put_sensor_data(uid, pid, reqjson, temp, hum, light, dusthum):     # Put json into DB
        return http_response_code['success200']
    else:
        return http_response_code['error401']

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
