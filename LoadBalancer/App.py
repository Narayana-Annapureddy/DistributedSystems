from flask import Flask
from flask import jsonify, request,redirect,url_for
import os 
import ast
import requests
import subprocess
import LoadBalancer as lb
import uuid
import random

app = Flask(__name__)
app.config.from_object('config.Config')
obj = lb.ConsistentHashing()


# resposes all the replicas of the servers


@app.route("/rep",methods = ["GET"])
def rep():
    try:
            result = subprocess.run(["python","Helper.py",],stdout=subprocess.PIPE, text=True, check=True)
            replicas = result.stdout.splitlines()
            # if()
            # print(result)
    except:
        msg = {
        "message":"<Error>  Unable to process your request",
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

#add servers based on the request

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
        # msg = {
        # "message":"<Error> Length of hostname list is less than newly added instances",
        # "status" : "Faliure"
        # }
        # return jsonify(msg),400
        k = n-len(servers)
        for i in range(k):
            servers.append("S"+str(obj.N+1+i))

    for i in servers:
        try:
            result = subprocess.run(["python","Helper.py",str(i),"distributedsystems_net1","flaskserver1","add"],stdout=subprocess.PIPE, text=True, check=True)
            if(obj.dic.get(i)==None):
                obj.N+=1
                obj.dic[i] = obj.N
            obj.add_server(obj.dic[i])
            #implement hashing
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
        k = n-len(servers)
        try:
            for i in servers:
                replicas.remove(i)
        except:
            pass
        result = subprocess.run(["python","Helper.py",],stdout=subprocess.PIPE, text=True, check=True)
        replicas = result.stdout.splitlines()
        servers = servers+random.sample(replicas, n)

    for i in servers:
        try:
            result = subprocess.run(["python","Helper.py",str(i),"remove"],stdout=subprocess.PIPE, text=True, check=True)
            obj.remove_server(obj.dic[i])
            #implement hashing
        except:
            msg = {
            "message":"<Error>  Unable to remove some container(s)",
            "status" : "Faliure"
            }
            return jsonify(msg),400
    return redirect(url_for("rep"))

# routes requests to one of the avaliable servers

@app.route("/<path>",methods = ["GET"])
def pathRoute1(path):

    #assigning uuid to each request
    # max_value = 10**(6) - 1
    # request_id = uuid.uuid4().int % max_value
    request_id =  random.randint(100000,999999)
    temp = 512
    while(temp>=0):
        server_id = obj.req_server(request_id)
        for i,j in obj.dic.items():
            if(j==server_id):
                server_name = i
                break
        
        #checkheartbeat
        res = requests.get(f'http://{server_name}:5000/heartbeat')
        if res.status_code == 404:
            obj.remove_server(obj.dic[server_id])
        else:
            break
        temp-=1
    response = requests.get(f'http://{server_name}:5000/home/{server_name}')
    return jsonify(response.json())

    #loadbalancer should be implemented here
    # server_name = loadbalancer()
    max_value = 10**(6) - 1
    request_id = uuid.uuid4().int % max_value
    server_id = obj.req_server(request_id)
    for i,j in obj.dic.items():
        if(j==server_id):
            server_name = i
            break
    
    #checkheartbeat
    response = requests.get(f'http://{server_name}:5000/home/{server_name}')
    return jsonify(response.json())


@app.errorhandler(404)

def errorPage(k):
    return "Page not found"

if __name__ == "__main__":
    for i in ["server1"]:
        # try:
        #     result = subprocess.run(["python","Helper.py",str(i),"distributedsystems_net1","flaskserver1","add"],stdout=subprocess.PIPE, text=True, check=True)
        if(obj.dic.get(i)==None):
            obj.N+=1
            obj.dic[i] = obj.N
        obj.add_server(obj.dic[i])
            #implement hashing
        # except:
        #     pass
    
    app.run(host = "0.0.0.0",debug = True)
