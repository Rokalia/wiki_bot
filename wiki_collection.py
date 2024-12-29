import chromadb

def get_wiki_collection():
  client = chromadb.PersistentClient(path="./database")
  return client.get_collection(name="wiki_collection")
