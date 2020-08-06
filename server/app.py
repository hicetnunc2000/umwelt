from flask import Flask, request, make_response
from flask_cors import CORS, cross_origin
#from flask_pymongo import PyMongo
from ipfs import IPFS, Onto
import threading
#import pymongo
import os
import json

app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb://localhost:27017/drss"
cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'
ipfs = IPFS()
onto = Onto()

ipfs.insert_topic('ontology')
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

        print(req)
        
        obj['title'] = req['title']
        obj['description'] = req['description']
        obj['tags'] = req['tags']
        #obj['topic'] = req['topic']
        for e in request.files:
            path = "./bucket/{}".format(e)
            file = open(path, "wb")
            file.write(request.files[e].read())
            file.close()
            obj['file_cid'] = ipfs.add(path)
        print(obj)
        cid = ipfs.add_json(obj)
        obj['json_cid'] = cid
        ipfs.insert_json_into_topic('Philosophy', cid)
        #ipfs.publish('Philosophy', obj)
        onto.insert_pub(obj)
        ipfs.update_ontology()
        onto.update()
    return {'res': obj }

@app.route('/feed', methods=['GET'])
def feed():
    """ 
    gets latests ontologies entries
    """
    res = ipfs.get_dir_jsons('Philosophy')
    return { 'res' : res }

@app.route('/ontology', methods=['GET'])
def ontology():
    """  
    gets ontology hash
    """
    res = ipfs.client.files.stat('/ontology/gott')['Hash']
    return {'res' : res }

@app.route('/search', methods=['POST'])
def search():
    """ 
    search for a term
    """
    res = onto.search()
    return { 'res' : res }

@app.route('/pubsub', methods=['POST'])
@cross_origin(origin='*')
def register():
    """ 
    insert data from ipfs pubsub (receives requests from listener service)
    """
    print(request.data)
    res = 'test'
    return { 'res' : res }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
