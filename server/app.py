from flask import Flask, request, make_response
from flask_cors import CORS, cross_origin
#from flask_pymongo import PyMongo
from ipfs import IPFS, Onto

#import pymongo
import os
import json

app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb://localhost:27017/drss"
cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'
ipfs = IPFS()
onto = Onto()

#mongo = PyMongo(app)

@app.route('/uploads', methods=['POST'])
def upload_files():

    res = []

    if request.method == 'POST':

        for e in request.files:
            path = "./bucket/{}".format(e)
            file = open(path, "wb")
            file.write(request.files[e].read())
            file.close()
            conn = ipfs.conn()
            res.append(ipfs.add(conn, path))
            onto.insert_pub(res)
            conn.close()

    return {'res': res}


@app.route('/upload', methods=['POST'])
#@cross_origin()
def upload_file():
    """ 
    uploads single file
    """
    print(request.method)
    #if request.methods == 'OPTIONS':
    #    return _build_cors_prelight_response()
    if request.method == 'POST':

        obj = {}
        req = request.form.to_dict(flat=False)
        req = json.loads(req['state'][0])
        obj['title'] = req['title']
        obj['description'] = req['description']
        obj['tags'] = req['tags']
        #obj['topic'] = req['topic']
        for e in request.files:
            path = "./bucket/{}".format(e)
            file = open(path, "wb")
            file.write(request.files[e].read())
            file.close()
            obj['cid'] = ipfs.add(path)
        print(obj)
        cid = ipfs.add_json(obj)
        obj['cid_json'] = cid
        ipfs.insert_json_into_topic('Philosophy', cid)
        #ipfs.publish('Philosophy', obj)
        onto.insert_pub(obj)
        ipfs.update_ontology()
        onto.update()
    return {'res': obj }

@app.route('/feed', methods=['GET'])
def feed():

    res = ipfs.get_dir_jsons('Philosophy')
    return { 'res' : res }

@app.route('/ontology', methods=['GET'])
def ontology():
    res = ipfs.client.files.stat('/ontology/gott')['Hash']
    return {'res' : res }

@app.route('/search', methods=['POST'])
def search():
    res = onto.search()
    return { 'res' : res }

@app.route('/login', methods=['POST'])
def login():
    """ 
    check for login credentials (simple)
    """
    pass

@app.route('/register', methods=['POST', 'OPTIONS'])
@cross_origin(origin='*')
def register():
    """ 
    register user (simple)
    """
    
    res = 'test'
    return { 'res' : res }



def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
