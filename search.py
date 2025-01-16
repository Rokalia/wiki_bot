import wikipedia
import chromadb

CLIENT = chromadb.PersistentClient(path="./database")
if CLIENT.count_collections() == 0:
    wiki = CLIENT.create_collection(
        name="wiki_collection",
        metadata={
            "hnsw:space": "cosine"
        }
    )

wikipedia.set_lang('ru')

def create_collection(query: str, retriever):
    collection = CLIENT.get_collection(name="wiki_collection")
    docs = []
    urls = []
    embs = []
    ids = []
    i = 0
    for t in wikipedia.search(query):
        p = wikipedia.page(t)
        docs.append(p.content)
        urls.append(p.url)
        embs.append(retriever.encode(p.content))
        i+=1
        ids.append(f"id{i}")
    collection.add( documents= docs, uris = urls, embeddings=embs, ids=ids)
    return collection

def retrieve_results(query: str, retriever, top_k):
    collection = create_collection(query, retriever)
    cols = ['documents', 'uris']
    if top_k > collection.count():
        top_k = collection.count()
    q_embs = retriever.encode(query).tolist()
    retrieved_results = collection.query(
            query_embeddings = q_embs,
            n_results = top_k,
            include = cols
        )
    ids = collection.get()["ids"]
    collection.delete(ids)
    return retrieved_results[cols[0]][0], retrieved_results[cols[1]][0]

def get_reranked_result_id(reranker, query, docs, top_k):
    if top_k > len(docs):
        top_k = len(docs)
    reranked_results = reranker.rank(query=query,documents= docs, top_k=top_k)
    return reranked_results[0]['corpus_id']

def search_page(query: str, retriever, reranker, top_k=10):
  docs, urls = retrieve_results(query, retriever, top_k*10)
  id = get_reranked_result_id(reranker, query, docs, top_k)
  return docs[id], urls[id]

def get_answer_from_page(qa, query, doc):
  qa_response = qa(question = query, context = doc)
  return qa_response['answer']
