from owlready2 import *
# https://stackoverflow.com/questions/47111939/how-to-query-a-owl-file-from-protege-using-owlready-library-in-python-3-6


class SparqlQueries:
    def __init__(self):
        my_world = World()
        my_world.get_ontology("./gott2.owl").load() #path to the owl file is given here
        sync_reasoner(my_world)  #reasoner is started and synchronized here
        self.graph = my_world.as_rdflib_graph()

    def search(self):
        #Search query is given here
        #Base URL of your ontology has to be given here
        query = "base <http://127.0.0.1:8000/gott2.owl#> " \
                "SELECT ?s ?p ?o " \
                "WHERE { " \
                "?s ?p ?o . " \
                "}"

        #query is being run
        resultsList = self.graph.query(query)

        #creating json object
        response = []
        for item in resultsList:
            s = str(item['s'].toPython())
            s = re.sub(r'.*#',"",s)

            p = str(item['p'].toPython())
            p = re.sub(r'.*#', "", p)

            o = str(item['o'].toPython())
            o = re.sub(r'.*#', "", o)
            response.append({'s' : s, 'p' : p, "o" : o})

        print(response) #just to show the output

        for e in response:
            if e['o'] == 'Philosophy':
                print(e)
                for e2 in response:
                    if e['s'] == e2['s']:
                        print(e2)

            

        return response


runQuery = SparqlQueries()
runQuery.search()
