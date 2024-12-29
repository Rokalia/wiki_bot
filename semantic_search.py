def prepare_query(query: str, retriever) -> list:
    return retriever.encode(query).tolist()

def retrieve_results(collection, retriever, query, top_k):
  q_embs = prepare_query(query, retriever)
  retrieved_results = collection.query(
      query_embeddings=q_embs,
      n_results=top_k,
      include= ['documents', 'uris']
  )
  return retrieved_results['documents'][0], retrieved_results['uris'][0]

def get_reranked_result_id(reranker, query, docs, top_k):
  reranked_results = reranker.rank(query=query,documents= docs, top_k=top_k)
  return reranked_results[0]['corpus_id']

def search_page(query: str, wiki, retriever, reranker, top_k=10):
  docs, urls = retrieve_results(wiki, retriever, query, top_k*10)
  id = get_reranked_result_id(reranker, query, docs,top_k)
  return docs[id], urls[id]

def get_answer(qa, query, doc):
  qa_response = qa(question = query, context = doc)
  return qa_response['answer']
