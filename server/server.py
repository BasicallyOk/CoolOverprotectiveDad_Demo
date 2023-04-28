from flask import Flask
from flask_cors import CORS
import json
import chromadb

from lifelike.toolkit.sequence_manager.tree_builder import SequenceTreeBuilder

CHROMA_CLIENT = chromadb.Client() 
CHROMA_CLIENT.reset()
CHROMA_CLIENT.create_collection(name="cool_overprotective_dad")

tree_builder = SequenceTreeBuilder.build_from_json("./cod.json")
tree_builder.write_db(CHROMA_CLIENT)

collection = CHROMA_CLIENT.get_collection(name="cool_overprotective_dad")

app = Flask(__name__)
CORS(app)

@app.route('/ping')
def ping():
    # You can just return the string, but I am assuming you'll be returning way more
    return {
        'message': 'ping'
    }

@app.route('/sequence/<embedding>/')
def get_next_sequence(embedding):
    """
    Query the next sequence in the database
    TODO: Some logic for neutral path
    """
    embedding = json.loads(embedding)
    embeddingList = [embedding[str(i)] for i in range(28)] # The incoming JSON is a dict
    print(embeddingList)
    # Query from chromadb
    response = collection.query(
        query_embeddings=embeddingList,
        n_results = 6, # Leave it for now
    )
    # Enable Access-Control-Allow-Origin
    # response.headers.add("Access-Control-Allow-Origin", "*")
    return response