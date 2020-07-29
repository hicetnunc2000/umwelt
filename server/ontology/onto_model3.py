from owlready2 import *

onto_path.append('.')
onto = get_ontology('http://127.0.0.1:8000/gott2.owl')

with onto:
    class Pub(Thing):
        pass
    class has_description(DataProperty, FunctionalProperty):
        domain = [Pub]
        range = [str]
    class has_topic(DataProperty, FunctionalProperty):
        domain = [Pub]
        range = [str]
    class has_files_CID(DataProperty, FunctionalProperty):
        domain = [Pub]
        range = [str]
    class has_json_CID(DataProperty, FunctionalProperty):
        domain = [Pub]
        range = [str]
    class has_Seqno(DataProperty, FunctionalProperty):
        domain = [Pub]
        range = [str]
    class has_tags(DataProperty, FunctionalProperty):
        domain = [Pub]
        range = [str]
    class has_author(DataProperty, FunctionalProperty):
        domain = [Pub]
        range = [str]
    class has_date(DataProperty, FunctionalProperty):
        domain = [Pub]
        range = [str]

onto.save()
onto.save(file = "gott2.owl", format = "rdfxml")