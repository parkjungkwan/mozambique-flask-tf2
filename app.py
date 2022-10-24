from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    a = {"a": "b", "c": "d"}
    return a

if __name__=="__main__":
    app.run()