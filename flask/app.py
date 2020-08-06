
from flask import Flask, session
from flask import jsonify
from flask import request, Blueprint
from flask_cors import CORS, cross_origin
#from flask_pymongo import PyMongo
from ipfs import IPFS, Onto, SparqlQueries
import threading
#import pymongo
import os
import json


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
#cors = CORS(app, origins=['127.0.0.1:3000'])
#app.config['CORS_HEADERS'] = 'Content-Type'
ipfs = IPFS()
onto = Onto()
ipfs.initialize_ontology('ontology')


@app.route('/api/upload', methods=['POST'])
@cross_origin() # allow all origins all methods.
def upload_file():
    """ 
    uploads single file
    """

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
        obj['file_cid'] = ipfs.add(path)
    print(obj)
    cid = ipfs.add_json(obj)
    obj['json_cid'] = cid
    #ipfs.insert_json_into_topic('Philosophy', cid)
    #ipfs.publish('Philosophy', obj)
    onto.insert_pub(obj)
    ipfs.update_ontology()
    # onto.update()
    return {'res': obj}


@app.route('/api/feed', methods=['GET'])
def feed():
    sparql = SparqlQueries()
    res = sparql.feed()
    print([ipfs.get_json(e['cid']) for e in res])
    return {'res': [ipfs.get_json(e['cid']) for e in res]}


@app.route('/api/ontology', methods=['GET'])
def ontology():
    res = ipfs.client.files.stat('/ontology/umwelt')['Hash']
    return {'res': res}


@app.route('/api/search', methods=['POST'])
def search():
    sparql = SparqlQueries()
    res = sparql.search(json.loads(request.data)['search'])
    return {'res': [ipfs.get_json(e['cid']) for e in res]}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
