from flask import Flask
from flask import jsonify, request,redirect,url_for
import os 
import ast
import requests
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


@app.route("/add",methods = ["POST"])
def add():
    try:
        servers = ast.literal_eval(request.args['replicas'])
    except:
        msg = {
                "message":"<Error> Unable to create some container(s)",
                "status" : "Faliure"
                }
        return jsonify(msg),400
    
    n = int(request.args['n'])
    if(n<len(servers)):
        msg = {
        "message":"<Error> Length of hostname list is more than newly added instances",
        "status" : "Faliure"
        }
        return jsonify(msg),400
    elif(n>len(servers)):
        msg = {
        "message":"<Error> Length of hostname list is less than newly added instances",
        "status" : "Faliure"
        }
        return jsonify(msg),400

    for i in servers:
        try:
            result = subprocess.run(["python","Helper.py",str(i),"distributedsystems_net1","flaskserver1","add"],stdout=subprocess.PIPE, text=True, check=True)
            
        except:
            msg = {
                "message":"<Error> Unable to create some container(s)",
                "status" : "Faliure"
                }
            return jsonify(msg),400
            
    #add here
    return redirect(url_for("rep"))
    # msg = {
    #     "message":
    #     {
            
    #         "N" : app.config["N"],
    #         "replicas" : app.config['REPLICAS']
    #     },
    #     "status" : "Successful"
    # }
    # return jsonify(msg),200

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

@app.route("/<path>",methods = ["GET"])
def pathRoute1(path):
    #loadbalancer should be implemented here
    # server_name = loadbalancer()
    server_name = "s21"
    target_url = f'server1/{path}'
    response = requests.get(f'http://{server_name}:5000/home/{server_name}')
    return jsonify(response.json())
    # return "HI"
    # return redirect(url_for(target_url))
    # return "hi"



    # return redirect(url_for(target_url))
    # return "hi"
@app.errorhandler(404)

def errorPage(k):
    return "Page not found"

if __name__ == "__main__":
    app.run(host = "0.0.0.0",debug = True)
