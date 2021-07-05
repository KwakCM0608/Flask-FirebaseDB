import pyrebase
import json

class DBModule:
    def __init__(self):
        with open("./auth/firebaseAuth.json") as f:
            config = json.load(f)

        self.firebase = pyrebase.initialize_app(config)

    def login(self, id, pwd):
        pass
    def signin(self, id, pwd, email):
        pass
    def write_post(self, writer, contents):
        pass
    def post_list(self):
        pass
    def post_detail(self, pid): # post id
        pass
    def get_user(self, uid): # user id
        pass