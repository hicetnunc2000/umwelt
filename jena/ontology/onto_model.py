from owlready2 import *

onto_path.append('.')
onto = get_ontology('http://127.0.0.1:8000/gott.owl')


class Pub(Thing):
    namespace = onto


class Title(Pub):
    namespace = onto


class Description(Pub):
    namespace = onto


class CID(Pub):
    namespace = onto


class Seqno(Pub):
    namespace = onto


class Topic(Pub):
    namespace = onto


class Tags(Pub):
    namespace = onto


class Date(Pub):
    namespace = onto


class Author(Pub):
    namespace = onto


class has_title(ObjectProperty):
    domain = [Pub]
    range = [Title]


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
onto.save(file="gott.owl", format="rdfxml")
