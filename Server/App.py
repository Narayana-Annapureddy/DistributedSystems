from flask import Flask
from flask import jsonify, request
import os
app = Flask(__name__)

@app.route("/",methods = ["GET"])
@app.route("/home",methods = ["GET"])
def hello_world():
    
    # server_id = os.environ.get('server_id')
    # no_of_servers = os.environ["no_of_servers"]
    server_id =1
    no_of_servers =1
    msg = {
        "message": f"Hello, From Server{server_id}",
        "no_of_servers" : no_of_servers,
        "status" : "Successful"
    }
    return jsonify(msg),200

@app.errorhandler(404)

def errorPage(k):
    return "Page not found"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)