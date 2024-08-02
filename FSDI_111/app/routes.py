from flask import Flask     # from the flask (lower-case = ) module import the Flask ( = title-case) class  

app = Flask(__name__)       # create an instance of the Flask class (an object)

@app.get("/")               # flask decorator that "wraps" our view function
def index():                # view function
    me= {                   # python3 dictionary (key-value pairs)
        "first_name": "Brandon",
        "last_name": "Bennington",
        "hobbies": "movies, video games, and comic books",
        "is_online": True
    }
    return me               # returning a dict from a view function auto-converts to JSON!