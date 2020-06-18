from tqdm import tqdm
import json
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from sys import argv

INDEX = 'from_json'


def main():
    es = Elasticsearch()
    actions = ({"_index": INDEX,
                "_type": "document",
                "_source": d}
               for d in get_docs())
    bulk(es, actions)
    print(f'count: {es.count(index=INDEX)}')


def get_docs():
    with open('/Users/oren.ovadia/src/jupyter-mongo/yelp_business.json') as f:
        for row in tqdm(f):
            des = json.loads(row)
            yield dict(name=des['name'], geopoint=[des['longitude'], des['latitude']], city=des['city'])


if __name__ == '__main__':
    main()
