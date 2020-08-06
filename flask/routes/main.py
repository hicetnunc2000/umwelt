
from flask import Blueprint, request, session

from flask import Flask
from flask_restx import fields, Resource, Api, Namespace

import distutils.util
import requests
import urllib
import json
import sys

from ipfs import IPFS, Onto, SparqlQueries

#ipfs = IPFS()
#onto = Onto()
sparql = SparqlQueries()
#ipfs.initialize_ontology('ontology')

api = Namespace('api', description='main route')   

@api.route('/uploads', methods=['POST'])
class upload_files(Resource):
    def post(self):
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


@api.route('/upload')
class upload_file(Resource):
    def post(self):
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
            #onto.update()
        return {'res': obj }

@api.route('/feed', methods=['GET'])
class feed(Resource):
    def get(self):
        res = sparql.feed()
        print([ ipfs.get_json(e['cid']) for e in res ])
        return { 'res' : [ ipfs.get_json(e['cid']) for e in res ] }

@api.route('/ontology', methods=['GET'])
class ontology(Resource):
    def get(self):
        res = ipfs.client.files.stat('/ontology/umwelt')['Hash']
        return {'res' : res }

@api.route('/search', methods=['POST'])
class search(Resource):
    def post(self):
        res = sparql.search(json.loads(request.data)['search'])
        return { 'res' : [ ipfs.get_json(e['cid']) for e in res ] }