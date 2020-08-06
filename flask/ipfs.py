# https://pypi.org/project/ipfshttpclient/#documentation
# https://ipfs.io/ipns/12D3KooWEqnTdgqHnkkwarSrJjeMP2ZJiADWLYADaNvUb6SQNyPF/docs/http_client_ref.html

from owlready2 import *
from datetime import datetime
import ipfshttpclient
#import libp2p
import base64
import base58
import urllib
import io
import json
import os


class IPFS:
    def __init__(self):
        self.client = ipfshttpclient.connect('/ip4/0.0.0.0/tcp/5001/http')
        #self.client = ipfshttpclient.connect('/ip4/ipfs/tcp/5001/http')
        #self.client = ipfshttpclient.connect('/dns4/ipfs/tcp/5001/')
        #self.client = ipfshttpclient.connect('/dns4/ipfs/tcp/5001/http')

    """ 
    client methods
    """

    def add(self, path):
        return self.client.add(path)['Hash']

    def mkdir(self, directory):
        return self.client.add(directory, recursive=True)

    def add_json(self, payload):
        return self.client.add_json(payload)

    def get_json(self, cid):
        return self.client.get_json(cid)

    def cat(self, _hash):
        return self.client.cat(_hash)

    def get(self, _hash):
        return self.client.get(_hash)

    def close(self):
        return self.client.close()

    def data(self, _hash):
        return self.client.object.data(_hash)

    def pin(self):
        return self.client.pin.ls(type='all')

    """ 
    pubsub methods
    """

    def sub_list(self):
        return self.client.pubsub.ls()['Strings']

    def subscribe(self, topic):
        return self.client.pubsub.subscribe(topic)

    def publish(self, topic, payload):
        return self.client.pubsub.publish(topic, json.dumps(payload))

    def get_posts(self, topic):
        arr = []
        sub = self.client.pubsub.subscribe(topic)
        for msg in sub:
            arr.append(msg)
            break
        return arr

    def listen1(self, topic):
        sub = self.client.pubsub.subscribe(topic)
        for msg in sub:
            print(msg)

    def listen2(self, topic):
        sub = self.client.pubsub.subscribe(topic)
        for msg in sub:
            self.client.pubsub.publish(topic, msg)
    """ 
    files methods
    """

    def topics(self):
        return self.client.files.ls('/')

    def initialize_ontology(self, topic):
        if not (self.client.files.ls('/')['Entries']):
            self.client.files.mkdir('/{}'.format(topic))
            self.update_ontology()
        else:
            self.update_ontology()

    def insert_topic(self, topic):
        if not ([e['Name'] for e in self.client.files.ls('/')['Entries']].__contains__(topic)):
            return self.client.files.mkdir('/{}'.format(topic))
        else:
            return 404

    def rm_topic(self, topic):
        return self.client.files.rm('/{}'.format(topic))

    def insert_file_into_topic(self, path, _bytes):
        return self.client.files.write(path, io.BytesIO(_bytes, create=True))

    def insert_json_into_topic(self, topic, cid):
        return self.client.files.write('/{}/{}'.format(topic, cid), io.BytesIO(self.client.cat(cid)), create=True)

    def files_read(self, topic, cid):
        return self.client.files.read("/{}/{}".format(topic, cid))

    def files_stat(self, topic):
        return self.client.files.stat("/{}".format(topic))

    def get_dir_cids(self):
        return [self.client.files.stat('/{}'.format(e))['Hash'] for e in [e['Name'] for e in self.client.files.ls('/')['Entries']]]

    def get_dir_jsons(self, topic):
        return [json.loads(self.client.cat(e)) for e in [e['Name'] for e in self.client.files.ls('/{}'.format(topic))['Entries']]]

    """  
    upload ontology ipfs/blockchain
    """

    def update_ontology(self):
        ontology = open('./ontology/umwelt.owl', 'rb')
        data = ontology.read()
        return self.client.files.write('/ontology/umwelt', io.BytesIO(data), create=True)

    """ 
    base64 decode base58 encode
    """

    def base64_decode(self, msg):
        #  base64.b64decode(e['data']) from pubsub msgs
        return base64.b64decode(msg)

    def base58_encode(self, msg):
        return base58.b58encode(base64.b64decode(msg))


class P2P():
    def peer_info(self, id, addresses):
        return libp2p.peer.peerinfo.PeerInfo(id, addresses)

    def pubsub_cache(self, topic):
        return libp2p.pubsub.mcache.MessageCache(100, 100).window(topic)


class Onto():
    # def __init__(self):
    #    self.sparql = SparqlQueries()

    def insert_pub(self, payload):
        # urllib.parse.quote()
        print(payload)
        onto_path.append('./ontology')
        onto = get_ontology('./ontology/umwelt.owl').load()
        onto.load()

        pub = onto.Pub(urllib.parse.quote(payload['title']))
        description = onto.Description(
            urllib.parse.quote(payload['description']))
        date = onto.Date(urllib.parse.quote(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        tags = []
        for e in payload['tags']:
            tags.append(onto.Tags(urllib.parse.quote(payload['tags'])))

        #topic = onto.Topic(payload['topic'])
        file_cid = onto.CID(urllib.parse.quote((payload['file_cid'])))
        json_cid = onto.CID(urllib.parse.quote((payload['json_cid'])))

        pub.has_description = [description]

        for e in tags:
            pub.has_tags = [e]

        #pub.has_topic = [topic]
        pub.has_file_CID = [file_cid]
        pub.has_json_CID = [json_cid]
        pub.has_date = [date]

        onto.save()


class SparqlQueries():
    # https://stackoverflow.com/questions/47111939/how-to-query-a-owl-file-from-protege-using-owlready-library-in-python-3-6
    def __init__(self):
        my_world = World()
        # path to the owl file
        my_world.get_ontology("./ontology/umwelt.owl").load()
        # sync_reasoner(my_world)
        self.graph = my_world.as_rdflib_graph()

    def search(self, term):

        term = term.lower()
        query = (
            "SELECT DISTINCT ?cid WHERE { \
            OPTIONAL {?subject <http://127.0.0.1:8000/umwelt.owl#has_json_CID> ?object.} \
            OPTIONAL {?subject  <http://127.0.0.1:8000/umwelt.owl#has_description> ?description.} \
            OPTIONAL {?subject  <http://127.0.0.1:8000/umwelt.owl#has_tags> ?tags.} \
            OPTIONAL {?subject  <http://127.0.0.1:8000/umwelt.owl#has_date> ?date.} \
            \
            BIND (STR(?subject) AS ?s) . \
            BIND (STR(?tags) AS ?t) . \
            BIND (STR(?description) AS ?d) . \
            \
            FILTER ( \
            CONTAINS (LCASE(?d), ENCODE_FOR_URI('%s')) || \
            CONTAINS (LCASE(?t), ENCODE_FOR_URI('%s')) || \
            CONTAINS (LCASE(?s), ENCODE_FOR_URI('%s'))) \
            \
            BIND (STRAFTER(STR(?object), 'http://127.0.0.1:8000/umwelt.owl#') AS ?cid) . }" % (term, term, term)
            )

        # runs query
        resultsList = self.graph.query(query)

        # json object
        response = []
        for item in resultsList:
            cid = str(item['cid'].toPython())
            cid = re.sub(r'.*#', "", cid)

            response.append({'cid': cid})
        print("search")
        print(term)
        print(response)
        return response

    def feed(self):
        # Search query is given
        # Base URL
        query = (
                "SELECT ?cid WHERE { \
                        OPTIONAL { ?subject <http://127.0.0.1:8000/umwelt.owl#has_json_CID> ?object. } \
                        BIND (STRAFTER(STR(?date), 'http://127.0.0.1:8000/umwelt.owl#') AS ?dateLabel) . \
                        BIND (STRAFTER(STR(?object), 'http://127.0.0.1:8000/umwelt.owl#') AS ?cid) . \
                } ORDER BY DESC(?dateLabel)"
                )
        # runs query
        resultsList = self.graph.query(query)
        print('feed')
        # json object
        response = []
        for item in resultsList:
            cid = str(item['cid'].toPython())
            cid = re.sub(r'.*#', "", cid)

            response.append({'cid': cid})

        return response
