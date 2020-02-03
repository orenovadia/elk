from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from essential_generators import DocumentGenerator

INDEX = 'test'


def main():
    es = Elasticsearch()
    # es.bulk()
    actions = ({"_index": INDEX,
                "_type": "document",
                "_source": d}
               for d in get_docs())
    bulk(es, actions)
    print(f'count: {es.count(index=INDEX)}')


def get_docs():
    gen = DocumentGenerator()

    template = {
        'id': 'guid',
        'status': ['online', 'offline', 'dnd', 'anonymous'],
        'age': 'small_int',
        'homepage': 'url',
        'name': 'name',
        'headline': 'sentence',
        'about': 'paragraph'
    }

    gen.set_template(template)

    return gen.documents(1000)


if __name__ == '__main__':
    main()
