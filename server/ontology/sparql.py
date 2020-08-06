from owlready2 import *
# https://stackoverflow.com/questions/47111939/how-to-query-a-owl-file-from-protege-using-owlready-library-in-python-3-6


class SparqlQueries:
    def __init__(self):
        my_world = World()
        my_world.get_ontology("./ontology/umwelt.owl").load()   #path to the owl file is given here
        sync_reasoner(my_world)                                 #reasoner is started and synchronized here
        self.graph = my_world.as_rdflib_graph()

    def search(self, term):
        #Search query is given here
        #Base URL of your ontology has to be given here
        query = """ 
        SELECT DISTRINCT ?cid
            WHERE {
            OPTIONAL {?subject <http://127.0.0.1:8000/umwelt.owl#has_json_CID> ?object.}
            OPTIONAL {?subject  <http://127.0.0.1:8000/umwelt.owl#has_description> ?description.}
            OPTIONAL {?subject  <http://127.0.0.1:8000/umwelt.owl#has_tags> ?tags.}
            OPTIONAL {?subject  <http://127.0.0.1:8000/umwelt.owl#has_date> ?date.}
            
            BIND (STR(?subject) AS ?s) .
            BIND (STR(?tags) AS ?t) .
            BIND (STR(?description) AS ?d) .

            OPTIONAL { FILTER CONTAINS ( LCASE(?s) , ENCODE_FOR_URI('{0}'))} .
            OPTIONAL { FILTER CONTAINS ( LCASE(?t) , ENCODE_FOR_URI('{0}'))} .
            OPTIONAL { FILTER CONTAINS ( LCASE(?d) , ENCODE_FOR_URI('{0}'))} .

            BIND (STRAFTER(STR(?object), 'http://127.0.0.1:8000/umwelt.owl#') AS ?cid) .

            }
        """.format(term)

        #query is being run
        resultsList = self.graph.query(query)

        #creating json object
        response = []
        for item in resultsList:
            cid = str(item['cid'].toPython())
            cid = re.sub(r'.*#',"",cid)

            response.append({'cid' : cid })

        print(response) #just to show the output

        #for e in response:
        #    if e['o'] == 'Philosophy':
        #        print(e)
        #        for e2 in response:
        #            if e['s'] == e2['s']:
        #                print(e2)

            

        return response


runQuery = SparqlQueries()
runQuery.search()
