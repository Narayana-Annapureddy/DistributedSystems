from flask import Flask
from flask import jsonify, request,redirect,url_for
import os
import ast
import subprocess
 
app = Flask(__name__)
app.config.from_object('config.Config')
 
@app.route("/rep",methods = ["GET"])
def rep():
    try:
            result = subprocess.run(["python","Helper.py",],stdout=subprocess.PIPE, text=True, check=True)
            print(result)
            replicas = result.stdout.splitlines()
            # if()
            # print(result)
    except:
        msg = {
        "message":"<Error>  Unable to remove some container(s)",
        "status" : "Faliure"
        }
        return jsonify(msg),400
    print(replicas)
    app.config['REPLICAS'] = replicas
    app.config["N"] = len(replicas)
    msg = {
        "message":
        {           
            "N" : app.config["N"],
            "replicas" :  app.config["REPLICAS"]
        },
        "status" : "Successful"
    }
    return jsonify(msg),200

@app.route("/rem",methods = ["POST"])
def rem():
    try:
        servers = ast.literal_eval(request.args['replicas'])
    except:
        msg = {
            "message":"<Error>  Unable to remove some container(s)",
            "status" : "Faliure"
            }
        return jsonify(msg),400
    n = int(request.args['n'])
    if(n<len(servers)):
        msg = {
        "message":"<Error>  Length of hostname list is more than removable instances",
        "status" : "Faliure"
        }
        return jsonify(msg),400
    elif(n>len(servers)):
        msg = {
        "message":"<Error>  Length of hostname list is less than removable instances",
        "status" : "Faliure"
        }
        return jsonify(msg),400

    for i in servers:
        try:
            result = subprocess.run(["python","Helper.py",str(i),"remove"],stdout=subprocess.PIPE, text=True, check=True)
        except:
            msg = {
            "message":"<Error>  Unable to remove some container(s)",
            "status" : "Faliure"
            }
            return jsonify(msg),400
    return redirect(url_for("rep"))
    # replicas = Helper.get_docker_processes()
    # app.config['REPLICAS'] = replicas
    # app.config["N"] = len(replicas)
    # msg = {
    #     "message":
    #     {
    #         "N" : app.config["N"],
    #         "replicas" : app.config['REPLICAS']
    #     },
    #     "status" : "Successful"
    # }
    # return jsonify(msg),200



@app.errorhandler(404)

def errorPage(k):
    return "Page not found"

if __name__ == "__main__":
    app.run(host = "0.0.0.0",debug = True)
