from owlready2 import *

onto_path.append('.')
onto = get_ontology('http://127.0.0.1:8000/gott2.owl')

with onto:
    class Pub(Thing):
        pass
    class Description(Pub):
        pass
    class CID(Pub):
        pass
    class Seqno(Pub):
        pass
    class Topic(Pub):
        pass
    class Tags(Pub):
        pass
    class Date(Pub):
        pass
    class Author(Pub):
        pass
    class has_description(ObjectProperty):
        domain = [Pub]
        range = [Description]
    class has_topic(ObjectProperty):
        domain = [Pub]
        range = [Topic]
    class has_CID(ObjectProperty):
        domain = [Pub, Topic]
        range = [CID]
    class has_Seqno(ObjectProperty):
        domain = [Pub]
        range = [Seqno]
    class has_tags(ObjectProperty):
        domain = [Pub]
        range = [Tags]
    class has_author(ObjectProperty):
        domain = [Pub]
        range = [Author]
    class has_date(ObjectProperty):
        domain = [Pub]
        range = [Date]

onto.save()
onto.save(file = "gott2.owl", format = "rdfxml")